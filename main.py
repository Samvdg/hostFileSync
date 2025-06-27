from hostSyncProj.sysfunctions import *
import os
import shutil
import sys
import urllib.request
import tkinter as tk
from yaml import *
from datetime import datetime

# def ensure_directories():
#     try:
#         file = urllib.request.urlretrieve(DEFAULT_SYNC_SOURCE, DEFAULT_SAVE_PATH)
#         print(f"[+] Downloaded hosts file from {DEFAULT_SYNC_SOURCE}")
#         print(file)
#     except Exception as e:
#         print(f"[!] Failed to download hosts file: {e}")
#     # if not os.path.exists(DEFAULT_SYNC_SOURCE):
#     #     print(f"[!] ERROR: Sync source file not found at {DEFAULT_SYNC_SOURCE}")
#     #     sys.exit(1)
#     if not os.path.exists(DEFAULT_WINDOWS_BACKUP_DIR) and not os.path.exists(DEFAULT_LINUX_BACKUP_DIR):
#         os.makedirs(DEFAULT_WINDOWS_BACKUP_DIR)

# def backup_hosts():
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     backup_file = os.path.join(DEFAULT_WINDOWS_BACKUP_DIR, f"hosts_backup_{timestamp}")
#     try:
#         shutil.copy(DEFAULT_WINDOWS_HOSTS_PATH, backup_file)
#         print(f"[+] Backup created: {backup_file}")
#     except Exception as e:
#         print(f"[!] Failed to back up hosts file: {e}")
#         sys.exit(1)

# def sync_hosts():
#     try:
#         shutil.copy(DEFAULT_SYNC_SOURCE, DEFAULT_WINDOWS_HOSTS_PATH)
#         print("[+] Hosts file synced successfully.")
#     except PermissionError:
#         print("[!] Permission denied. Please run this script as Administrator.")
#         sys.exit(1)
#     except Exception as e:
#         print(f"[!] Failed to sync hosts file: {e}")
#         sys.exit(1)

def open_gui():
    g = tk.Tk()
    g.title("Hosts File Sync Tool")

    sync_btn = tk.Button(g, text="start", command=g.destroy, width=10, height=1)
    sync_btn.grid(row=0, column=0, padx=5)

    stop_btn = tk.Button(g, text="Finish", command=g.destroy, width=10, height=1)
    stop_btn.grid(row=0, column=1)

    g.mainloop()

def main():
    print("=== Hosts File Sync Tool ===")
    check_config()
    # ensure_directories()
    # backup_hosts()
    # sync_hosts()
    open_gui()

if __name__ == "__main__":
    main()