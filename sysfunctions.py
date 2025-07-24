import os
import sys
import yaml
from datetime import datetime
from python_hosts import Hosts, HostsEntry

# Configuration
FIRST_RUN = True
INSTALL_LOCATION = os.path.dirname(os.path.abspath(__file__))

LOGS_PATH = f"{INSTALL_LOCATION}/logs"
ERR_PATH = f"{INSTALL_LOCATION}/errors"
CONFIG_PATH = f"{INSTALL_LOCATION}/config.yaml"

SYNC_SOURCE = r"https://crivian.nl/hosts"
WINDOWS_BTN = True
WINDOWS_HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
WINDOWS_BACKUP_DIR = r"C:\Windows\System32\drivers\etc\host_backups"
WINDOWS_SAVE_PATH = r"C:\Windows\Temp"

WSL_BTN = False
WSL_HOSTS_PATH = r"/mnt/c/Windows/System32/drivers/etc/hosts"
WSL_BACKUP_DIR = r"/mnt/c/Windows/System32/drivers/etc/host_backups"
WSL_SAVE_PATH = r"/mnt/c/Windows/Temp"

LINUX_BTN = False
LINUX_HOSTS_PATH = r"/etc/hosts"
LINUX_BACKUP_DIR = r"/etc/host_backups"
LINUX_SAVE_PATH = r"/etc/hosts/Temp"

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
    log(f"Error logged at {timestamp()}")

def make_config():
    try:
        with open(f"{INSTALL_LOCATION}/config.yaml", "w") as config_file:
                config_file.write("# Configuration file for Hosts File Sync Tool\n")
                config_file.write("FIRST_RUN: true\n")
                config_file.write("INSTALL_LOCATION: {}\n".format(INSTALL_LOCATION))
                config_file.write("\n# Windows config\n")
                config_file.write("WINDOWS_BTN: {}\n".format(WINDOWS_BTN))
                config_file.write("DEFAULT_SYNC_SOURCE: {}\n".format(SYNC_SOURCE))
                config_file.write("DEFAULT_WINDOWS_HOSTS_PATH: {}\n".format(WINDOWS_HOSTS_PATH))
                config_file.write("DEFAULT_WINDOWS_BACKUP_DIR: {}\n".format(WINDOWS_BACKUP_DIR))
                config_file.write("DEFAULT_WINDOWS_SAVE_PATH: {}\n".format(WINDOWS_SAVE_PATH))
                config_file.write("\n# WSL config\n")
                config_file.write("WSL_BTN: {}\n".format(WSL_BTN))
                config_file.write("WSL_HOSTS_PATH: {}\n".format(WSL_HOSTS_PATH))
                config_file.write("WSL_BACKUP_DIR: {}\n".format(WSL_BACKUP_DIR))
                config_file.write("WSL_SAVE_PATH: {}\n".format(WSL_SAVE_PATH))
                config_file.write("\n# Linux config\n")
                config_file.write("LINUX_BTN: {}\n".format(LINUX_BTN))
                config_file.write("DEFAULT_LINUX_HOSTS_PATH: {}\n".format(LINUX_HOSTS_PATH))
                config_file.write("DEFAULT_LINUX_BACKUP_DIR: {}\n".format(LINUX_BACKUP_DIR))
                config_file.write("DEFAULT_LINUX_SAVE_PATH: {}\n".format(LINUX_SAVE_PATH))
                config_file.write("DEFAULT_WINDOWS_SAVE_PATH: {}\n".format(WINDOWS_SAVE_PATH))
                log("Config created")

    except Exception as e:
        err("Failed to create config", e)


# This function checks if the necessary directories and configuration file exist.
def check_config():
    if not os.path.isdir(LOGS_PATH):
        os.makedirs(LOGS_PATH)
        log("Log directory created")

    if not os.path.isdir(ERR_PATH):
        os.makedirs(ERR_PATH)
        log("Error directory created")
    
    if not os.path.isfile(CONFIG_PATH):
        make_config()

def get_config():
    check_config()
    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)

    return config