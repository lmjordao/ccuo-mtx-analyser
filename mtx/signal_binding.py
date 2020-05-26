"""

"""
from mtx.mtx_file_parser import MtxFileParser


class SignalBinding(MtxFileParser):

    def __init__(self, filename):
        super().__init__(filename)
        self.__external_connected_signals = None

    def get_pou_name(self):
        return self._dom.getElementsByTagName('pou')[0].getAttribute('name')

    def has_signal(self, signal):
        return signal in self.get_variable_set()

    def get_external_connected_signals(self, ccuo_data, usage=None):

        if self.__external_connected_signals is None:
            self.__external_connected_signals = dict()
            _interface = self._dom.getElementsByTagName('interface')
            if len(_interface) > 0:
                interface = _interface[0]
            else:
                return self.dict_interface

            list_var_group = interface.getElementsByTagName('variable-group')

            for var_group in list_var_group:
                var_group_name = var_group.getAttribute('name')
                self.__external_connected_signals[var_group_name] = dict()
                list_vars = var_group.getElementsByTagName('variable')
                for _var in list_vars:
                    if usage is not None:
                        if _var.getAttribute('usage') != usage:
                            continue
                    self.__external_connected_signals[var_group_name][_var.getAttribute('name')] = \
                        ccuo_data.find_connections_to_signal(_var.getAttribute('name'), self.get_filename())

        return self.__external_connected_signals
