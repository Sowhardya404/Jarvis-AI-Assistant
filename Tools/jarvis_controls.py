import os
import webbrowser
import screen_brightness_control as sbc
import subprocess

# Volume Control
def increase_volume():
    os.system(r"C:\nircmd-x64\nircmd.exe changesysvolume 5000")

def decrease_volume():
    os.system(r"C:\nircmd-x64\nircmd.exe changesysvolume -5000")
    
# Brightness Control
def increase_brightness():
    try:
        current = sbc.get_brightness(display=0)[0]
        new = min(current + 10, 100)
        sbc.set_brightness(new, display=0)
    except Exception as e:
        print(f"Brightness up error: {e}")

def decrease_brightness():
    try:
        current = sbc.get_brightness(display=0)[0]
        new = max(current - 10, 0)
        sbc.set_brightness(new, display=0)
    except Exception as e:
        print(f"Brightness down error: {e}")

def set_brightness(value):
    try:
        value = int(value)
        value = max(0, min(value, 100))
        sbc.set_brightness(value, display=0)
    except Exception as e:
        print(f"Set brightness error: {e}")

def open_application(app_name):
    app_name = app_name.lower()

    # Handle Notepad
    if "notepad" in app_name:
        try:
            subprocess.run(["notepad.exe"])
            return "Opening Notepad."
        except Exception as e:
            return f"Could not open Notepad. Error: {e}"

    # Handle Calculator
    elif "calculator" in app_name or "calc" in app_name:
        try:
            subprocess.run(["calc.exe"])
            return "Opening Calculator."
        except Exception as e:
            return f"Could not open Calculator. Error: {e}"

    # Handle folders (e.g., Documents, Downloads, D drive, etc.)
    else:
        # Attempt to open folder path based on command
        folders = {
            "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
            "documents": os.path.join(os.path.expanduser("~"), "Documents"),
            "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
            "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
            "videos": os.path.join(os.path.expanduser("~"), "Videos"),
            "music": os.path.join(os.path.expanduser("~"), "Music"),
            "d drive": "D:\\",
            "c drive": "C:\\"
        }

        for key in folders:
            if key in app_name:
                path = folders[key]
                try:
                    os.startfile(path)
                    return f"Opening {key}."
                except Exception as e:
                    return f"Could not open {key}. Error: {e}"

        return None

def open_website(site_name):
    site_name = site_name.lower().strip()

    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "amazon": "https://www.amazon.in",
        "wikipedia": "https://www.wikipedia.org",
        "linkedin": "https://www.linkedin.com"
    }

    for key in websites:
        if key in site_name:
            webbrowser.open(websites[key])
            return f"Opening {key}."

    # If not in predefined list → try generic website
    if "." not in site_name:
        site_name += ".com"

    url = f"https://www.{site_name}"
    webbrowser.open(url)
    return f"Opening {site_name}."

