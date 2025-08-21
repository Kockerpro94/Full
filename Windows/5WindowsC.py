import platform
import subprocess

def get_windows_version():
    try:
        version = subprocess.check_output(
            ["wmic", "os", "get", "Caption"],
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore").split("\n")[1].strip()
        if version:
            return version
        else:
            return f"Windows {platform.release()}"
    except Exception:
        return f"Windows {platform.release()}"

def get_architecture():
    return platform.architecture()[0]

print("Windows Version:", get_windows_version())
print("System Architecture:", get_architecture())