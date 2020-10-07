"""

"""
import pandas as pd
from definitions import ROOT_DIR

xls_loc = ROOT_DIR + "\\..\\..\\ccuo_analyser_data\\dimensions\\Realisation\\SIL0\\03 Architecture & Design\\C_Communication" \
          "\\3EST000237-0050 LOT TCMS IP Booking List.xlsm"

xls = pd.ExcelFile(xls_loc)

print(xls.sheet_names)

"""

bl = IPBookingList()

_dict = bl.read_signal_data(xls_loc)

print(_dict.keys())

_signal_keys = list(_dict['201 - CCUOman'].keys())
#print(len(_signal_keys))

for i in range(0, 11):

    print(_signal_keys[i], _dict['201 - CCUOman'][_signal_keys[i]])
"""


