"""

"""
import os

from tcms_related.config.config_properties import ConfigProperties
from tcms_related.mtx.signal_binding import SignalBinding


class CcuoProjectData:

    def __init__(self, project_name):

        self.config = ConfigProperties.get_instance().get_project_config(project_name)
        self.components = dict()
        print(self.config)
        self.components['aventra_components'] = self._load_components_from_dir(
            self.config['aventra_components']
        )
        print("3")
        self.components['project_components'] = self._load_components_from_dir(
            self.config['project_components']
        )
        print("4")
        self.components['generic_pad'] = self._load_components_from_dir(
            self.config['generic_pad']
        )
        print("5")

    def _load_components_from_dir(self, component_dir):
        """

        :param component_dir: Directory with MTX components
        :return:
        """
        print("ik "+str(component_dir))

        _dict = dict()


        for file in os.listdir(component_dir):

            if file.endswith(".mtx"):
                _dict[file] = SignalBinding(component_dir + '\\' + file)

        return _dict

    """
    def find_components_containing_signal(self, signal):
        _signal_set = set()
        for _component_group in self.components.keys():
            for filename in self.components[_component_group].keys():
                if self.components[_component_group][filename].has_signal(signal):
                    _signal_set.add(filename)
        return _signal_set
    """

    """
    def find_connections_to_signal(self, signal, interface_filename):
        _signal_set = set()
        for _component_group in self.components.keys():
            for filename in self.components[_component_group].keys():

                if interface_filename == filename:
                    continue
                # print(interface_filename, filename, interface_filename == filename)
                if self.components[_component_group][filename].has_signal(signal):
                    _signal_set.add(filename)
        return _signal_set
    """

    def find_connections_to_signal_type(self, signal, signal_type, interface_filename):
        _signal_set = set()
        for _component_group in self.components.keys():
            for filename in self.components[_component_group].keys():

                if interface_filename == filename:
                    continue
                # print(interface_filename, filename, interface_filename == filename)
                if self.components[_component_group][filename].has_signal_type(signal, signal_type):
                    _signal_set.add(filename)
        return _signal_set

    def get_master_compontents(self):

        return {**self.components['aventra_components'], **self.components['project_components']}
