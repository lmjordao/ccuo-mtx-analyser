"""
Singleton that holds all data ready to be exported
Model Structure:
{ _project: {
    _function-group: {
        _variable-group: {
            [{
                'name': _name
                'type': _type
                'usage': _usage
            }]
            }
        }
    }
}
"""


class DataModel:

    __instance = None

    def __init__(self):
        self.model = dict()
        self.pad = dict()
        self.pad_signal_binding_in = dict()
        self.pad_signal_binding_out = dict()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DataModel, cls).__new__(cls)
        return cls.__instance

    @staticmethod
    def get_instance():
        if DataModel.__instance is None:
            DataModel()
        return DataModel.__instance
