"""

"""
from mtx.mtx_file_parser import MtxFileParser


class PAD(MtxFileParser):

    list_connections = None

    def get_function_group_name(self):
        return self._dom.getElementsByTagName('function-group')[0].getAttribute('name')

    def get_connection_list(self):
        if self.list_connections is None:
            self.list_connections = list()
            tag_connection_list = self._dom.getElementsByTagName('connection-list')[0]
            connection_list = tag_connection_list.getElementsByTagName('connection')
            for _conn in connection_list:
                self.list_connections.append({
                    'reference': _conn.getAttribute('reference'),
                    'type': _conn.getAttribute('type')
                })
        return self.list_connections
