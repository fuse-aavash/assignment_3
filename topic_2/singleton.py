import json

class ConfigurationManager:
    _instance = None
    _config_data = None

    @classmethod
    def get_instance(cls):
        """
        Get the singleton instance of ConfigurationManager.

        Returns:
            ConfigurationManager: The singleton instance.
        """
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        """
        Load the configuration data from the 'config.json' file.

        Returns:
            None
        """
        try:
            with open('config.json', 'r') as config_file:
                self._config_data = json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            self._config_data = {}

    def get_setting(self, section, setting_name):
        """
        Get the value of a setting in a specific section.

        Args:
            section (str): The section name.
            setting_name (str): The setting name.

        Returns:
            any: The value of the setting, or None if not found.
        """
        return self._config_data.get(section, {}).get(setting_name)

    def set_setting(self, section, setting_name, value):
        """
        Set the value of a setting in a specific section.

        Args:
            section (str): The section name.
            setting_name (str): The setting name.
            value (any): The value to be set for the setting.

        Returns:
            None
        """
        if section not in self._config_data:
            self._config_data[section] = {}
        self._config_data[section][setting_name] = value
        with open('config.json', 'w') as config_file:
            json.dump(self._config_data, config_file, indent=4)


if __name__ == '__main__':
    config_manager1 = ConfigurationManager.get_instance()
    config_manager2 = ConfigurationManager.get_instance()

    print(config_manager1 is config_manager2)

    setting1_value = config_manager1.get_setting('AppConfig', 'setting1')
    print(setting1_value)

    config_manager1.set_setting('AppConfig', 'setting1', 'new_value')

    setting1_updated_value = config_manager2.get_setting('AppConfig', 'setting1')
    print(setting1_updated_value)
