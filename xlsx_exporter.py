"""

"""
import os
import xlsxwriter as xlsxwriter


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
