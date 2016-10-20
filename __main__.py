from linux_backup import *
from userdata_handler import *
import argparse
from services import Services
from userdata import *


def get_args():
    parser = argparse.ArgumentParser("Linux Backup")
    parser.add_argument("-u", "--username", help="Username input")
    parser.add_argument("-p", "--password", help="password input")
    parser.add_argument("-s", "--service", help="DROPBOX|DRIVE")
    return vars(parser.parse_args())

def main():
    options = get_args()
    username = options["username"]
    password = options["password"]
    service = Services.get_service_from_string(options["service"])
    userdata = UserData(username, password, service)
    backup = LinuxBackup(userdata)


if __name__ == '__main__':
    main()