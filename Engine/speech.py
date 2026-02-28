import sounddevice as sd
import io
import scipy.io.wavfile as wav
import speech_recognition as sr

def listen(timeout=5):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 0.8

    fs = 44100

    try:
        print(" Listening...")
        recording = sd.rec(
            int(timeout * fs),
            samplerate=fs,
            channels=1,
            dtype='int16'
        )
        sd.wait()

        # Convert to bytes
        byte_io = io.BytesIO()
        wav.write(byte_io, fs, recording)
        byte_io.seek(0)

        with sr.AudioFile(byte_io) as source:
            audio = recognizer.record(source)

        command = recognizer.recognize_google(audio)
        print(f" Heard: {command}")
        return command.lower()

    except sr.UnknownValueError:
        print(" Could not understand audio")
        return None

    except sr.RequestError as e:
        print(f" Speech service error: {e}")
        return None

    except Exception as e:
        print(f" Speech Error: {e}")
        return None
