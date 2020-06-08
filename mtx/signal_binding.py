"""

"""
from config.config_properties import ConfigProperties
from mtx.mtx_file_parser import MtxFileParser


class SignalBinding(MtxFileParser):

    def __init__(self, filename):
        super().__init__(filename)
        self.__external_connected_signals = None
        self.list_connections = None

    def get_pou_name(self):
        _pou = self._dom.getElementsByTagName('pou')
        if _pou > 0:
            return _pou[0].getAttribute('name')
        _func_group = self._dom.getElementsByTagName('function-group')
        if _func_group > 0:
            return _func_group[0].getAttribute('name')
        return ''

    def get_connection_list(self):
        if self.list_connections is None:
            self.list_connections = list()

            tag_connection_list = self._dom.getElementsByTagName('connection-list')[0]
            if len(tag_connection_list) > 0:
                connection_list = tag_connection_list.getElementsByTagName('connection')
            else:
                return self.list_connections

            for _conn in connection_list:
                self.list_connections.append({
                    'reference': _conn.getAttribute('reference'),
                    'type': _conn.getAttribute('type')
                })
        return self.list_connections

    def has_signal(self, signal):
        return (signal in self.get_variable_set()) \
               or (signal.split('_')[-1] in self.get_variable_set())

    #alterar
    def has_signal_type(self, signal, type):
        ct_eq=0
        ct_neq=0
        for signal in self.get_variable_dict():
            if type==self.variable_dict[signal]['type']:
                ct_eq+=1
                print("Signal type equal")
            else:
                ct_neq+=1
                print("Signal type not equal")


    def get_external_connected_signals(self, ccuo_data, usage=None):
        if self.__external_connected_signals is None:
            self.__external_connected_signals = dict()
            _interface = self._dom.getElementsByTagName('interface')
            if len(_interface) > 0:
                interface = _interface[0]
            else:
                return self.__external_connected_signals

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
