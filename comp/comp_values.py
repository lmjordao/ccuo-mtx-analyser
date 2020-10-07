import os

import xlsxwriter

from booking_list.ip_booking_list import IPBookingList

def comp_values(connection_set):
    #tem que te percorrer todos os devices
    xls_loc = "..\\dimensions\\Realisation\\SIL0\\03 Architecture & Design\\C_Communication" \
          "\\3EST000237-0050 LOT TCMS IP Booking List.xlsm"
    bl = IPBookingList()
    _dict = bl.read_signal_data(xls_loc)
    final_found = dict()
    final_not = dict()

    for i in _dict["201 - CCUOman"].keys():
        for _filename in connection_set.keys():
            for _var_group_key in connection_set[_filename].keys():
                for _var_key in connection_set[_filename][_var_group_key].keys():
                    if i == _var_key:
                        print(_var_key + "exist on Generic")
                        final_found[_var_key] = 1
                    if i != _var_key:
                        print(_var_key + "Does not exits on Generic")
                        final_not[_var_key] = 0
                        #utilizar apenas o dicionario final_found
                        #por enquando está a ser usado apenas para visualizar mais rapidamente

    print("Keys Founded")
    print(final_found)
    print("Keys not Founded")
    print(final_not)
    excel_comparation(final_found, final_not, "result")


def excel_comparation(found, not_found, excel_name):

    output_filename = excel_name + '.xlsx'
    output_filepath = os.path.join(os.getcwd(), output_filename)

    workbook = xlsxwriter.Workbook(output_filepath)
    worksheet = workbook.add_worksheet("result")

    worksheet.write(0, 0, 'Output Signal:')

    row = 1
    for i in found.keys():
        worksheet.write(row, 0, i)
        row = row + 1

    workbook.close()


# ver problema de criaçao do export.xlsx (ultimas duas colunas)                 -
# melhorar a apresentaçao do codigo                                             X
# apresentar no excel ?                                                         X

