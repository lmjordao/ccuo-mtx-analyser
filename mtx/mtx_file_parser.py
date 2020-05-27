"""
mtx file parser
"""
import io

import xml.dom.minidom
from xml.parsers.expat import ExpatError
from lxml import etree
import re


class MtxFileParser:

    def __init__(self, filename):

        self._dom = None
        self.filename = filename
        self.dict_interface = None
        self.variable_set = None
        self.variable_dict = None

        self.corrected = self.load_file_v2(filename)

    def get_component_name(self):
        return self.filename.split('/')[-2]

    def get_filename(self):
        return self.filename.split('\\')[-1]

    def load_file_v2(self, filename):
        # print("Parsing file: ", filename)
        corrected = False
        try:
            self._dom = xml.dom.minidom.parse(filename)
        except ExpatError:
            # If Illegal chars have been found within XML file
            # they will be replaced with '', in order to ensure that the file is parsed
            escape_illegal_xml_characters = \
                lambda x: re.sub(u'[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]', '', x)
            with io.open(filename, 'r') as f:
                contents = f.read()
                contents = escape_illegal_xml_characters(contents)

                try:
                    self._dom = xml.dom.minidom.parseString(contents)
                except ExpatError:
                    # TODO: Generate a warning to the user if we ever get here
                    self._dom = self._dom = xml.dom.minidom.parse("empty.xml")

            corrected = True
        return corrected


    """
    def __apply_corrective_action(self):
        RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                         u'|' + \
                         u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
                         (unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff),
                          unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff),
                          unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff))
        x = u"<foo>text\u001a</foo>"
        x = re.sub(RE_XML_ILLEGAL, "?", x)
        dom = xml.dom.minidom.parseString(x.encode("utf-8"))
    """

    # Infeasible
    """
    def load_file(self, filename):
        print("Parsing file: ", filename)
        parsed = True
        try:
            self._dom = xml.dom.minidom.parse(filename)
        except ExpatError:
            self._dom = xml.dom.minidom.parse("empty.xml")
            parsed = False
        return parsed
    """

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
