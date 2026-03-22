import sounddevice as sd
import speech_recognition as sr
import numpy as np
import io
import scipy.io.wavfile as wav

SAMPLE_RATE = 16000
CHUNK_DURATION = 0.1        # seconds per chunk (100ms)
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)

SILENCE_THRESHOLD = 500     # audio energy below this = silence
                            # raise this if it triggers too early
                            # lower this if it never stops listening

SILENCE_SECONDS = 1.0       # seconds of silence before stopping
SILENCE_CHUNKS = int(SILENCE_SECONDS / CHUNK_DURATION)  # = 10 chunks

MIN_SPEECH_SECONDS = 0.3    # ignore clips shorter than this
MIN_SPEECH_CHUNKS = int(MIN_SPEECH_SECONDS / CHUNK_DURATION)  # = 3 chunks

MAX_SECONDS = 10            # hard limit — stops even if no silence
MAX_CHUNKS = int(MAX_SECONDS / CHUNK_DURATION)


def is_silent(chunk):
    """Returns True if the audio chunk is below the silence threshold."""
    energy = np.abs(chunk).mean()
    return energy < SILENCE_THRESHOLD


def record_until_silence(timeout=5):
    """
    Records in small chunks and stops automatically after silence.
    Returns raw audio bytes or None if nothing was spoken.
    """
    print("Listening...")

    chunks = []
    silent_chunks = 0
    speech_started = False
    timeout_chunks = int(timeout / CHUNK_DURATION)
    waited = 0

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1,
                        dtype='int16', blocksize=CHUNK_SIZE) as stream:

        while True:
            chunk, _ = stream.read(CHUNK_SIZE)
            chunk = np.squeeze(chunk)
            silent = is_silent(chunk)

            if not speech_started:
                if not silent:
                    # Speech just began
                    speech_started = True
                    chunks.append(chunk)
                else:
                    waited += 1
                    if waited >= timeout_chunks:
                        # Nobody spoke within timeout
                        return None
            else:
                chunks.append(chunk)

                if silent:
                    silent_chunks += 1
                else:
                    silent_chunks = 0

                # Stop on sustained silence
                if silent_chunks >= SILENCE_CHUNKS:
                    break

                # Hard stop at max length
                if len(chunks) >= MAX_CHUNKS:
                    break

    # Ignore clips that are too short (likely just noise)
    if len(chunks) < MIN_SPEECH_CHUNKS:
        return None

    audio_np = np.concatenate(chunks, axis=0)
    return audio_np


def listen(timeout=5):
    """
    Main function — records until silence then converts speech to text.
    """
    recognizer = sr.Recognizer()

    try:
        audio_np = record_until_silence(timeout=timeout)

        if audio_np is None:
            return None

        # Convert numpy array → wav bytes → AudioData
        byte_io = io.BytesIO()
        wav.write(byte_io, SAMPLE_RATE, audio_np)
        byte_io.seek(0)

        with sr.AudioFile(byte_io) as source:
            audio = recognizer.record(source)

        print("Processing...")
        command = recognizer.recognize_google(audio)
        print(f"Heard: {command}")
        return command.lower()

    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

    except sr.RequestError as e:
        print(f"Speech service error: {e}")
        return None

    except Exception as e:
        print(f"Speech Error: {e}")
        return None