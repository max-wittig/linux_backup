import enum


class Services(enum):
    DROPBOX = 1,
    DRIVE = 2

    @staticmethod
    def get_service_from_string(string):
        if str(string).startswith("DROPBOX"):
            return Services.DROPBOX
        elif str(string).startswith("DRIVE"):
            return Services.DRIVE