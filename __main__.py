from linux_backup import *
import argparse
from services import Services


def get_args():
    parser = argparse.ArgumentParser("Linux Backup")
    parser.add_argument("-s", "--service", help="dropbox|drive")
    return vars(parser.parse_args())


def main():
    options = get_args()
    service = Services.get_service_from_string(options["service"])
    linux_backup = LinuxBackup()
    linux_backup.backup()


if __name__ == '__main__':
    main()
