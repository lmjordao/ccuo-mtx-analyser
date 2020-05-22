"""
mtx file parser
"""
import xml.dom.minidom


class MtxFileParser:

    def __init__(self, filename):

        self._dom = None
        self.dict_interface = None
        self.variable_set = None
        self.variable_dict = None

        self.load_file(filename)
        self.component_name = filename.split('/')[-2]

    def get_component_name(self):
        return self.component_name

    def load_file(self, filename):
        self._dom = xml.dom.minidom.parse(filename)
        return self._dom is not None

    def get_interface(self):
        if self.dict_interface is None:
            self.dict_interface = dict()
            _interface = self._dom.getElementsByTagName('interface')[0]
            list_var_group = _interface.getElementsByTagName('variable-group')

            for var_group in list_var_group:
                var_group_name = var_group.getAttribute('name')
                self.dict_interface[var_group_name] = list()
                list_vars = var_group.getElementsByTagName('variable')
                for _var in list_vars:
                    self.dict_interface[var_group_name].append({
                        'name': _var.getAttribute('name'),
                        'type': _var.getAttribute('type'),
                        'usage': _var.getAttribute('usage')
                    })
        return self.dict_interface

    # get all variables as a set (used to identify uniques later)
    def get_variable_set(self):
        if self.dict_interface is None:
            self.get_interface()
        if self.variable_set is None:
            self.variable_set = set()
            for key in self.dict_interface:
                for _var in self.dict_interface[key]:
                    self.variable_set.add(_var['name'])
        return self.variable_set

    # get all variables as a dictionary (used for performance gains)
    def get_variable_dict(self):
        if self.dict_interface is None:
            self.get_interface()
        if self.variable_dict is None:
            self.variable_dict = dict()
            for key in self.dict_interface:
                for _var in self.dict_interface[key]:
                    self.variable_dict[_var['name']] = {'type': _var['type'], 'usage': _var['usage']}
        return self.variable_dict
