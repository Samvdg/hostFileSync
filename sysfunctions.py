import os
import shutil
import sys
import urllib.request
import tkinter as tk
from yaml import *
from datetime import datetime

# Configuration
FIRST_RUN = True
INSTALL_LOCATION = os.getcwd()

WINDOWS_BTN = True
DEFAULT_SYNC_SOURCE = r"www.crivian.nl/hosts"
DEFAULT_WINDOWS_HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
DEFAULT_WINDOWS_BACKUP_DIR = r"C:\Windows\System32\drivers\etc\host_backups"
DEFAULT_WINDOWS_SAVE_PATH = r"C:\Windows\Temp"

LINUX_BTN = False
DEFAULT_LINUX_HOSTS_PATH = r"/mnt/c/Windows/System32/drivers/etc/hosts"
DEFAULT_LINUX_BACKUP_DIR = r"/mnt/c/Windows/System32/drivers/etc/host_backups"
DEFAULT_LINUX_SAVE_PATH = r"/mnt/c/Windows/Temp"

# This function returns the current timestamp in a formatted string.
def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# This function logs a message to a file and prints it to the console.
def log(message):
    log_file = f"{INSTALL_LOCATION}/logs/log.txt"
    with open(log_file, "a") as lf:
        lf.write(f"[{timestamp()}] {message}\n")
    print(f"[+] {message}")

# This function logs an error message to a file and prints it to the console.
def err(message, error = None):
    error_file = f"{INSTALL_LOCATION}/errors/errors.txt"
    with open(error_file, "a") as ef:
        ef.write(f"[{timestamp()}] {message}\n")
        if error:
            ef.write(f"\nError details: \n{error}\n")
    print(f"[!!!] {message}")
    log(f"Error logged at {timestamp()}.")

# This function checks if the necessary directories and configuration file exist.
def check_config():
    if not os.path.isdir(f"{INSTALL_LOCATION}/logs"):
        os.makedirs(f"{INSTALL_LOCATION}/logs")
        log("Log directory created.")

    if not os.path.isdir(f"{INSTALL_LOCATION}/errors"):
        os.makedirs(f"{INSTALL_LOCATION}/errors")
        log("Error directory created.")
    
    if not os.path.isfile(f"{INSTALL_LOCATION}/config.yaml"):
        with open(f"{INSTALL_LOCATION}/config.yaml", "w") as config_file:
            config_file.write("# Configuration file for Hosts File Sync Tool\n")
            config_file.write("FIRST_RUN: true\n")
            config_file.write("INSTALL_LOCATION: {}\n".format(INSTALL_LOCATION))
    sys.exit(1)
