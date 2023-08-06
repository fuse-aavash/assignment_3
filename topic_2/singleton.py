# configuration_manager.py
import json

class ConfigurationManager:
    _instance = None
    _config_data = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            with open('config.json', 'r') as config_file:
                cls._config_data = json.load(config_file)
        return cls._instance

    def get_setting(self, section, setting_name):
        return self._config_data.get(section, {}).get(setting_name)

    def set_setting(self, section, setting_name, value):
        if section not in self._config_data:
            self._config_data[section] = {}
        self._config_data[section][setting_name] = value
        with open('config.json', 'w') as config_file:
            json.dump(self._config_data, config_file, indent=4)


if __name__ == '__main__':
    config_manager1 = ConfigurationManager()
    config_manager2 = ConfigurationManager()

    print(config_manager1 is config_manager2)  

    setting1_value = config_manager1.get_setting('AppConfig', 'setting1')
    print(setting1_value) 

   
    config_manager1.set_setting('AppConfig', 'setting1', 'new_value')

   
    setting1_updated_value = config_manager2.get_setting('AppConfig', 'setting1')
    print(setting1_updated_value)  
