# DownloadCleanup
# Moves and/or renames files in the default Downloads folder

import os
import sys
import time
import ext
import json

from datetime import datetime

def _exit(msg):
    print(msg)
    exit()

if sys.platform not in ["win32", "win64"]: _exit("Filesorter only works on Windows")

config = json.load(open("./config.json"))

USER = os.getlogin()
DEST_FOLDER = config["DEST_DIR"]
USE_DEST_FOLDER = config["use_dest_dir"]
TARGET_FOLDER = config["TARGET_DIR"].format(USER)
os.chdir(TARGET_FOLDER)

# Destination folder for each file type
accepted = ext.extentions

# Command line arguments
# Multiple are allowed but will not work if they overlap
args = sys.argv

delete_all_flag = "-D" in args
auto_rename_flag = "-r" in args
custom_rename_flag = "-c" in args
delete_installers_flag = "-d" in args

if (delete_all_flag and delete_installers_flag) or (auto_rename_flag and custom_rename_flag): _exit("Overlapping arguments")

counter = 0
errors  = 0
deleted = 0

t = time.time()

for f in os.listdir(os.curdir):
    split = f.lower().split(".")
    if len(split) != 2:
        continue

    name, ext = split

    if ext == "ini":
        continue

    # Delete likely installers or all files
    if (ext == "exe" and delete_installers_flag) or delete_all_flag:
        os.system(f'del "{f}"')
        deleted += 1
        continue

    if ext in accepted:
        try:
            new_name = f

            # Rename file to date of edit / download
            if auto_rename_flag:
                mtime = os.path.getmtime(f)
                date = datetime.fromtimestamp(mtime).isoformat(" ").split(" ")[0]
                new_name = f"{date}({counter}).{ext}"
                os.renames(f, new_name)

            # Custom input file rename
            if custom_rename_flag:
                new_name = input(f"Rename '{f}' (without extention): ") + f".{ext}"
                os.renames(f, new_name if new_name != "" else f)
            
            # Create new downloads dir if it doesnt exist
            dest = f"C:/Users/{USER}{accepted[ext]}{DEST_FOLDER if USE_DEST_FOLDER else ''}"
            if not os.path.isdir(dest):
                os.system(f'mkdir "{dest}"')

            # Move file
            os.system(f'mv {new_name} "{dest}"')
            counter += 1
        except:
            errors += 1


# delta time
dt = round(time.time() - t, 2)

print(f"""
--- Finished in {dt} seconds ---
Moved{' and renamed' if auto_rename_flag or custom_rename_flag else ''} {counter} files.
Deleted {deleted} files. (flag {'set' if delete_installers_flag or delete_all_flag else 'unset'})
Found {errors} complications.
""")