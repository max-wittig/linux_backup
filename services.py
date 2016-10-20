import enum


class Services:
    DROPBOX = 1
    DRIVE = 2

    def get_service_from_string(string):
        if str(string).startswith("DROPBOX"):
            return Services.DROPBOX
        elif str(string).startswith("DRIVE"):
            return Services.DRIVE