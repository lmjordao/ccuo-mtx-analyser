"""

"""
import logging
import os
import pandas as pd

from booking_list.device import Device
from definitions import BOOKING_LISTS_BASE_DIR


class XLSBookingList:

    def __init__(self, book_info):
        """
        Info according to json file
            "name": "booking list name",
            "filename": "path to booking list",
            "type": "ip, tdr, etc, etc",
            "min-offset": 5,
            "max-offset": 10
        """
        self.name = book_info['name']
        self.filename = book_info['filename']
        self.type = book_info['type']
        self.min_page_offset = book_info['min-offset']
        self.max_page_offset = book_info['max-offset']

        # This list contains a list of devices as objects from class Devices
        self.devices = list()

        self.xls_file = pd.ExcelFile(os.path.join(BOOKING_LISTS_BASE_DIR, book_info['filename']))
        # print(self.xls_file.sheet_names)

        self.load_devices()

    def load_devices(self):
        """
        This class will create a Device object for every page/sheet on book document/xls
        For every sheet name create a new device and pass sheet info into it
        :return:
        """
        for i in range(self.min_page_offset, self.max_page_offset+1):
            current_device_sheet_name = self.xls_file.sheet_names[i]
            logging.debug("Parsing Device sheet: " + str(current_device_sheet_name))
            df = pd.read_excel(self.xls_file, sheet_name=current_device_sheet_name)
            self.devices.append(Device(df))  # Passes the sheet data as a DataFrame

    """
    def read_signal_data(self, filename):
        _data = dict()
        workbook = xlrd.open_workbook(filename)

        min_sheet_offset = 6
        max_sheet_offset = 6  # 63

        # Iterate through the entire workbook
        for i in range(min_sheet_offset, max_sheet_offset+1):
            _sheet = workbook.sheet_by_index(i)
            _data[_sheet.name] = self.__get_xls_sheet_data(_sheet)
        print(_data)
        return _data
    """
