import platform
import subprocess
from tempfile import gettempdir
from pathlib import Path
import hashlib
import os
import time

def get_current_wallpaper():
    if platform.system() == "Darwin":
        cmd = [
            "osascript", "-e",
            'tell application "System Events" to get picture of desktop 1'
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        wallpaper = result.stdout.strip()
        return wallpaper

LAST_WALLPAPER_FILE = Path(os.path.join(gettempdir(), "last_wallpaper.txt")) # this doesn't even get the /tmp/ folder what the hell
WAL_PATH = "/Users/mac/Library/Python/3.9/bin/wal" #TODO: find wal path automatically

def updateWallpaper():
    wallpaper = get_current_wallpaper()

    with open(wallpaper, 'rb') as f:
        current_hash = hashlib.md5(f.read()).hexdigest()

    last_hash = ""
    if LAST_WALLPAPER_FILE.exists():
        #print(LAST_WALLPAPER_FILE)
        last_hash = LAST_WALLPAPER_FILE.read_text().strip()

    if current_hash != last_hash:
        subprocess.run([WAL_PATH, "-i", wallpaper])
        LAST_WALLPAPER_FILE.write_text(current_hash)
        print(f"updated pywal: {wallpaper}")
        print(f"hash: {current_hash}")

def main():
    # make polling stuff idk
    while True:
        updateWallpaper()
        time.sleep(1)
        # make polling time configurable (i hate doing configs in python)

if __name__ == "__main__":
    main()