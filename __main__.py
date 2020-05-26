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

TODO: Contagem das diferenças dos sinais entre projectos
Signals that are present among all projects: 2345
Signals that were not found in certain projects: 584
Check output spreadsheet

TODO: MTXFileParser, propriedades privadas

TODO: Analysis tools has a method that returns a set to signalbinding with which components contain a given signal

TODO: Merge ConfigLoader with configProperties

 ============== DEV NOTES ===============
 get folders on a given dir
  [ f.path for f in os.scandir(folder) if f.is_dir()]

"""

from config.config_loader import ConfigLoader
from config.config_properties import ConfigProperties
from data_model import DataModel
from model.ccuo_project_data import CcuoProjectData
from mtx.pad import PAD
from mtx.signal_binding import SignalBinding
from xlsx_exporter import XLSXExporter

EXPORT_FILENAME = 'export'

components = dict()


def _load_pad_out():
    # init pad here using sigbinding out
    pad_location = ConfigProperties.get_instance().config['base_project_dir'] \
                   + "\\PAD_P_LOTRAIN\\MTPE\\components\\PAD_P_LOTRAIN\\PAD_P_SignalBindingOut.mtx"
    return SignalBinding(pad_location)


def load_from_project():

    print("Parsing data...")
    ccuo_data = CcuoProjectData("lotrain")
    #pad_out = _load_pad_out()
    #res = pad_out.get_external_connected_signals(ccuo_data, "output")

    generic_pad_connections = dict()
    for _pad_filename in ccuo_data.components['generic_pad'].keys():
        generic_pad_connections[_pad_filename] = \
            ccuo_data.components['generic_pad'][_pad_filename].\
            get_external_connected_signals(ccuo_data, "output")

    # print(res)
    exporter = XLSXExporter(EXPORT_FILENAME)
    # exporter.export_connection_set(res, 'connections')
    exporter.export_connections_to_component(generic_pad_connections, 'genPAD-connections')
    exporter.save()
    print("Finished")


def main():
    # Load config file properties
    # config = ConfigProperties()
    # config.get_project_config("lotrain")
    load_from_project()


if __name__ == "__main__":
    main()


def load_local_pads():
    model = DataModel.get_instance()
    components_dir = ConfigLoader.getinstance().config_section_map('local')['components']

    # TODO: This does not make any sense, mtx should be loaded automatically
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
