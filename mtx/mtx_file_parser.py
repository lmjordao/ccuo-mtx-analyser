"""
mtx file parser
"""
import xml.dom.minidom
from xml.parsers.expat import ExpatError


class MtxFileParser:

    def __init__(self, filename):

        self._dom = None
        self.filename = filename
        self.dict_interface = None
        self.variable_set = None
        self.variable_dict = None

        self.parsed = self.load_file(filename)

    def get_component_name(self):
        return self.filename.split('/')[-2]

    def get_filename(self):
        return self.filename.split('\\')[-1]

    def load_file(self, filename):
        print("Parsin file: ", filename)
        parsed = True
        # try:
        self._dom = xml.dom.minidom.parse(filename)

        #except ExpatError:
            #self._dom = xml.dom.minidom.parse("empty.xml")
            #parsed = False

        return parsed

    def _get_interface(self, usage=None):
        if self.dict_interface is None:
            self.dict_interface = dict()
            self.variable_set = set()
            self.variable_dict = dict()
            _interface = self._dom.getElementsByTagName('interface')
            if len(_interface) > 0:
                interface = _interface[0]
            else:
                return self.dict_interface

            list_var_group = interface.getElementsByTagName('variable-group')

            for var_group in list_var_group:
                var_group_name = var_group.getAttribute('name')
                self.dict_interface[var_group_name] = list()
                list_vars = var_group.getElementsByTagName('variable')
                for _var in list_vars:
                    _var_name = _var.getAttribute('name')
                    _var_type = _var.getAttribute('type')
                    _var_usage = _var.getAttribute('usage')
                    self.dict_interface[var_group_name].append({
                        'name': _var_name,
                        'type': _var_type,
                        'usage': _var_usage
                    })
                    self.variable_set.add(_var_name)
                    self.variable_dict[_var_name] = {'type': _var_type, 'usage': _var_usage}

        return self.dict_interface

    # get all variables as a set (used to identify uniques later)
    def get_variable_set(self):
        if self.dict_interface is None:
            self._get_interface()
        if self.variable_set is None:
            self.variable_set = set()
            for key in self.dict_interface:
                for _var in self.dict_interface[key]:
                    self.variable_set.add(_var['name'])
        return self.variable_set

    # get all variables as a dictionary (used for performance gains)
    def get_variable_dict(self):
        if self.dict_interface is None:
            self._get_interface()
        if self.variable_dict is None:
            self.variable_dict = dict()
            for key in self.dict_interface:
                for _var in self.dict_interface[key]:
                    self.variable_dict[_var['name']] = {'type': _var['type'], 'usage': _var['usage']}
        return self.variable_dict
