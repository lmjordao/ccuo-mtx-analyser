"""

"""
from config.config_loader import ConfigLoader


class ConfigProperties:

    __instance = None

    def __init__(self):
        self.config = dict()
        # self.__load_dirs()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ConfigProperties, cls).__new__(cls)
        return cls.__instance

    @staticmethod
    def get_instance():
        if ConfigProperties.__instance is None:
            ConfigProperties()
        return ConfigProperties.__instance

    def get_project_config(self, project_name):

        #if self.config[project_name] is None:
        if project_name not in self.config:
            self.config[project_name] = dict()
            self.config[project_name]['ccuo_project_name'] = \
                ConfigLoader.getinstance().config_section_map(project_name)['ccuo_project_name']
            self.config[project_name]['base_project_dir'] = \
                ConfigLoader.getinstance().config_section_map(project_name)['project']
            self.config[project_name]['aventra_components'] = \
                self.config[project_name]['base_project_dir'] + "\\AVENTRA_CCUO\\MTPE\\components\\AVENTRA_CCUO"
            self.config[project_name]['project_components'] = \
                self.config[project_name]['base_project_dir'] + "\\" + self.config[project_name]['ccuo_project_name'] \
                                             + "\\LTABE0\\components\\" + self.config[project_name]['ccuo_project_name']
            self.config[project_name]['generic_pad'] = \
                ConfigLoader.getinstance().config_section_map(project_name)['generic_pad']
        return self.config[project_name]

    # TODO: Delete
    def __load_dirs(self):
        """
        # Load signal binding out from PAD
        # Load aventra modules
        # Load project Modules
        :return:
        """
        # Setting up dirs
        """
        CCUO_PROJECT_NAME = ConfigLoader.getinstance().config_section_map('DIR')['ccuo_project_name']
        BASE_PROJECT_DIR = ConfigLoader.getinstance().config_section_map('DIR')['project']
        AVENTRA_MODULES = BASE_PROJECT_DIR + "\AVENTRA_CCUO\MTPE\components\AVENTRA_CCUO"
        PROJECT_MODULES = BASE_PROJECT_DIR + "\\" + CCUO_PROJECT_NAME + "\LTABE0\components\\" + CCUO_PROJECT_NAME
        """

        self.config['ccuo_project_name'] = ConfigLoader.getinstance().config_section_map("lotrain")['ccuo_project_name']
        self.config['base_project_dir'] = ConfigLoader.getinstance().config_section_map("lotrain")['project']
        self.config['aventra_components'] = self.config['base_project_dir'] \
                                         + "\\AVENTRA_CCUO\\MTPE\\components\\AVENTRA_CCUO"
        self.config['project_components'] = self.config['base_project_dir'] + "\\" + self.config['ccuo_project_name'] \
                                         + "\\LTABE0\\components\\" + self.config['ccuo_project_name']

        self.config['generic_pad'] = ConfigLoader.getinstance().config_section_map("lotrain")['generic_pad']