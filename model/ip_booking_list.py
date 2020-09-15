"""

"""
import xlrd

from model.xls_booking_list import XLSBookingList


class IPBookingList(XLSBookingList):

    def __init__(self):
        """
        Dictionary Structure:
        { *spreadsheet name* :
            {*signal_name* :
                {'used' : *true/false*},
                {'type' : *type*}
            }
        }
        """
        self.signal_structure = dict()

    """
        Parse Signal stucture from excel file to dictionary
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

    def __get_xls_sheet_data(self, sheet):

        AP_NAME_OFFSET = 4
        AP_TYPE_OFFSET = 6
        IS_USED_OFFSET = 3

        """
            {*signal_name* :
                {'used' : *true/false*},
                {'type' : *signal_type*}
            }
        """
        sub_dict = dict()

        # sheet pointer row,col
        # sheet.cell_value(0, 0)
        for i in range(1, sheet.nrows):

            # Filter out garbage data
            if (sheet.cell_value(i, AP_NAME_OFFSET) != ""
                    and sheet.cell_value(i, AP_NAME_OFFSET) != "Ap Name") \
                and (sheet.cell_value(i, IS_USED_OFFSET) == 'x'
            or sheet.cell_value(i, IS_USED_OFFSET) == '') \
                    and sheet.cell_value(i, AP_TYPE_OFFSET) != '':

                # Import signal data
                sub_dict[sheet.cell_value(i, AP_NAME_OFFSET)] = {
                    'used': (sheet.cell_value(i, IS_USED_OFFSET) == 'x'),
                    'type': sheet.cell_value(i, AP_TYPE_OFFSET)
                }
        return sub_dict
