"""
Notes:
Excel structure

File, Tag,

PAD Variable type usage


pad.mtx

function-group connection group signal type

PAD file, variable-group, variable type usage

might not be needed
pad_file, task instance connect-name
"""
from config_loader import ConfigLoader
from data_model import DataModel
from mtx.pad import PAD
from mtx.signal_binding import SignalBinding
from xlsx_exporter import XLSXExporter

EXPORT_FILENAME = 'export'


def main():
    model = DataModel.get_instance()
    components_dir = ConfigLoader.getinstance().config_section_map('DIR')['components']

    # Load interface objects
    model.pad = {
        'eaa': PAD(components_dir + '/PAD/PAD_P_EAA/PAD.mtx'),
        'eaa118': PAD(components_dir + '/PAD/PAD_P_EAA118/PAD.mtx'),
        'lot': PAD(components_dir + '/PAD/PAD_P_LOTRAIN/PAD.mtx'),
        'lot154': PAD(components_dir + '/PAD/PAD_P_LOTRAIN154/PAD.mtx'),
        'swr': PAD(components_dir + '/PAD/PAD_P_SWR/PAD.mtx'),
        'wml': PAD(components_dir + '/PAD/PAD_P_WML/PAD.mtx')
    }

    model.signal_binding_in = {
        'eaa': SignalBinding(components_dir + '/PAD/PAD_P_EAA/PAD_P_SignalBindingIn.mtx'),
        'eaa118': SignalBinding(components_dir + '/PAD/PAD_P_EAA118/PAD_P_SignalBindingIn.mtx'),
        'lot': SignalBinding(components_dir + '/PAD/PAD_P_LOTRAIN/PAD_P_SignalBindingIn.mtx'),
        'lot154': SignalBinding(components_dir + '/PAD/PAD_P_LOTRAIN154/PAD_P_SignalBindingIn.mtx'),
        'swr': SignalBinding(components_dir + '/PAD/PAD_P_SWR/PAD_P_SignalBindingIn.mtx'),
        'wml': SignalBinding(components_dir + '/PAD/PAD_P_WML/PAD_P_SignalBindingIn.mtx'),
    }

    model.signal_binding_out = {
        'eaa': SignalBinding(components_dir + '/PAD/PAD_P_EAA/PAD_P_SignalBindingOut.mtx'),
        'eaa118': SignalBinding(components_dir + '/PAD/PAD_P_EAA118/PAD_P_SignalBindingOut.mtx'),
        'lot': SignalBinding(components_dir + '/PAD/PAD_P_LOTRAIN/PAD_P_SignalBindingOut.mtx'),
        'lot154': SignalBinding(components_dir + '/PAD/PAD_P_LOTRAIN154/PAD_P_SignalBindingOut.mtx'),
        'swr': SignalBinding(components_dir + '/PAD/PAD_P_SWR/PAD_P_SignalBindingOut.mtx'),
        'wml': SignalBinding(components_dir + '/PAD/PAD_P_WML/PAD_P_SignalBindingOut.mtx'),
    }

    exporter = XLSXExporter(EXPORT_FILENAME)
    exporter.export_project_interface_comparison(model.pad, 'PAD_comparison')
    exporter.export_project_interface_comparison(model.signal_binding_in, 'SigBindIn_comparison')
    exporter.export_project_interface_comparison(model.signal_binding_out, 'SigBindOut_comparison')
    exporter.save()


if __name__ == "__main__":
    main()
