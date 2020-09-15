"""

"""
import os
import xlsxwriter as xlsxwriter

from data_model import DataModel
from excel.excel import get_excel


class XLSXExporter:

    FILENAME = 'workitems_export'

    def __init__(self, filename):
        output_filename = filename + '.xlsx'
        output_filepath = os.path.join(os.getcwd(), output_filename)

        self.workbook = xlsxwriter.Workbook(output_filepath)

    def export_project_interface_comparison(self, pad_objects, sheet_name):
        # variable_set = set()
        variable_dict = dict()

        worksheet = self.workbook.add_worksheet(sheet_name)

        # Write header row
        worksheet.write(0, 0, 'Signal')
        worksheet.write(0, 1, 'Type')
        worksheet.write(0, 2, 'Usage')
        col = 2
        for key in pad_objects:
            pad_obj = pad_objects[key]
            # variable_set.update(pad_obj.get_variable_set())
            variable_dict.update(pad_obj.get_variable_dict())
            col = col+1
            worksheet.write(0, col, pad_obj.get_component_name())

        # Write worksheet body
        row = 1
        for _key in variable_dict:
            col = 0
            worksheet.write(row, col, _key)
            col = col + 1
            worksheet.write(row, col, variable_dict[_key]['type'])
            col = col + 1
            worksheet.write(row, col, variable_dict[_key]['usage'])

            for key in pad_objects:
                pad_obj = pad_objects[key]
                col = col + 1
                if _key in pad_obj.get_variable_set():
                    worksheet.write(row, col, 'Yes')
                else:
                    worksheet.write(row, col, 'No')
            row += 1

    def save(self):
        self.workbook.close()

    def export_connection_set(self, connection_set, sheet_name):

        worksheet = self.workbook.add_worksheet(sheet_name)
        worksheet.write(0, 0, 'Var Group:')
        worksheet.write(0, 1, 'Var:')
        worksheet.write(0, 2, 'Connected to:')
        row = 1
        for _var_group_key in connection_set.keys():
            for _var_key in connection_set[_var_group_key].keys():
                col = 0
                worksheet.write(row, col, _var_group_key)
                col = col + 1
                worksheet.write(row, col, _var_key)

                for _filename in connection_set[_var_group_key][_var_key]:
                    col = col + 1
                    worksheet.write(row, col, _filename)

                row += 1

    def export_connections_to_component(self, connection_set, sheet_name):
        worksheet = self.workbook.add_worksheet(sheet_name)
        worksheet.write(0, 0, 'filename:')
        worksheet.write(0, 1, 'Output Signal:')
        worksheet.write(0, 2, 'Connection count:')
        worksheet.write(0, 3, 'Found In:')
        row = 1
        for _filename in connection_set.keys():
            for _var_group_key in connection_set[_filename].keys():
                for _var_key in connection_set[_filename][_var_group_key].keys():
                    col = 0
                    worksheet.write(row, col, _filename)
                    col = col + 1
                    worksheet.write(row, col, _var_key)
                    #get_excel(_var_key)
                    col = col + 1
                    worksheet.write(row, col, len(connection_set[_filename][_var_group_key][_var_key]))

                    col = col + 1
                    # for _conn in connection_set[_filename][_var_group_key][_var_key]:
                    conn_list_as_str = '[' + ', '.join(connection_set[_filename][_var_group_key][_var_key]) + ']'
                    worksheet.write(row, col, conn_list_as_str)
                    row += 1
