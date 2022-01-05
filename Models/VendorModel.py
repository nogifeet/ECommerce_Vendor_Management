import csv

VENDOR_FILE = "..\\config\\vendor.csv"


class VendorModel:

    def __init__(self):
        self.vendor_db = []
        self.login_data = dict()
        self._load_vendors()

    def _load_vendors(self):
        csv_data = csv.DictReader(open(VENDOR_FILE))
        for vendor in csv_data:
            self.vendor_db.append(vendor)
            self.login_data[vendor["User Name"]] = vendor["Password"]

    def is_correct_vendor(self, username, password):
        if (username in self.login_data):
            if (self.login_data[username] == password):
                return True
            else:
                return False
        else:
            return False
