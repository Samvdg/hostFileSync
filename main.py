# from sysfunctions import *
from gui import *
from python_hosts import Hosts, HostsEntry
# from sys

def main():
    print("=== Hosts File Sync Tool ===")

    # g = open_gui()

    try:
        hosts = Hosts()
        print(hosts)
        print(DEFAULT_SYNC_SOURCE)
        hosts.import_url(DEFAULT_SYNC_SOURCE)
        print("TRUE")
        return True

    except  Exception as e:
        print(f"error: {e}")
    # g.mainloop()

if __name__ == "__main__":
    main()