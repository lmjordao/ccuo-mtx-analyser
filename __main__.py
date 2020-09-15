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
Exemplos:
Signals that are present among all projects: 2345
Signals that were not found in certain projects: 584
Check output spreadsheet

TODO: MTXFileParser, propriedades privadas


TODO: Merge ConfigLoader with configProperties

 ============== DEV NOTES ===============
 get folders on a given dir
  [ f.path for f in os.scandir(folder) if f.is_dir()]

"""

from config.config_loader import ConfigLoader
from comp.comp_values import comp_values
from model.ccuo_project_data import CcuoProjectData
from xlsx_exporter import XLSXExporter
from excel import excel
import os.path
from os import path

EXPORT_FILENAME = 'export'

# components = dict()

"""
def _load_pad_out():
    # init pad here using sigbinding out
    pad_location = ConfigProperties.get_instance().config['base_project_dir'] \
                   + "\\PAD_P_LOTRAIN\\MTPE\\components\\PAD_P_LOTRAIN\\PAD_P_SignalBindingOut.mtx"
    return SignalBinding(pad_location)
"""


def load_from_project():

    print("Parsing data...")
    project_name = ConfigLoader.getinstance().config_section_map("local")['project_to_load']  #lotrain
    ccuo_data = CcuoProjectData(project_name)

    #pad_out = _load_pad_out()
    #res = pad_out.get_external_connected_signals(ccuo_data, "output")
    print("CCUO_DATA")
    print(ccuo_data)
    print("NEXT point")
    generic_pad_connections = dict()
    for _pad_filename in ccuo_data.components['generic_pad'].keys():
        print(_pad_filename)
        print( ccuo_data.components['generic_pad'].keys())
        generic_pad_connections[_pad_filename] = \
            ccuo_data.components['generic_pad'][_pad_filename].\
            get_external_connected_signals(ccuo_data, "output")

    #on  method comp_values, "generic_pad_connections" is send to be compared with the IP Booking List values
    comp_values(generic_pad_connections)
    # print(res)
    exporter = XLSXExporter(EXPORT_FILENAME)
    # exporter.export_connection_set(res, 'connections')
    print(generic_pad_connections)
    print(exporter)
    exporter.export_connections_to_component(generic_pad_connections, 'genPAD-connections')
    exporter.save()
    print("Finished")
    print("Check " + EXPORT_FILENAME + ".xlsx")



def main():
    # Load config file properties
    #config = ConfigProperties()
    #config.get_project_config("lotrain")
    #print(path.exists("config.ini"))

    load_from_project()


if __name__ == "__main__":
    main()

"""
def load_local_pads():
    model = DataModel.get_instance()
    components_dir = ConfigLoader.getinstance().config_section_map('local')['components']

    # TODO: This does not make any sense, mtx should be loaded automatically
    # Load interface objects
    model.pad = {
        'eaa': SignalBinding(components_dir + '/PAD/PAD_P_EAA/PAD.mtx'),
        'eaa118': SignalBinding(components_dir + '/PAD/PAD_P_EAA118/PAD.mtx'),
        'lot': SignalBinding(components_dir + '/PAD/PAD_P_LOTRAIN/PAD.mtx'),
        'lot154': SignalBinding(components_dir + '/PAD/PAD_P_LOTRAIN154/PAD.mtx'),
        'swr': SignalBinding(components_dir + '/PAD/PAD_P_SWR/PAD.mtx'),
        'wml': SignalBinding(components_dir + '/PAD/PAD_P_WML/PAD.mtx')
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
"""
