import os
import yaml


class Configuration():
    config = ""

    def __init__(self, config_file="config.yaml"):
        self.config = self.read_config(config_file)
        self.config.user_data = self.config["user_data"]
        self.config.test_data = self.config["test_data"]
        self.config.run_options = self.config["run_options"]


    def read_config(self, file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)

        return config

    def find_file_by_name(name, path='.'):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
        return None

    def read_field_from_config(self, field_name):
        for key, value in self.config.items():
            if key == 'demo':
                break
        else:
            raise ValueError("Configuration not found in file.")

        field_value = self.config.get(field_name)
        if field_value is None:
            raise ValueError(f"Field '{field_name}' not found in configuration file.")

        return field_value

    def get_config_by_name(self, field_name, file_name='config.yaml'):
        file_path = self.find_file_by_name(file_name, 'config')
        print(file_path)
        if file_path is None:
            print(f"File '{file_name}' not found in 'config' directory.")
        else:
            try:
                field_value = self.read_field_from_config(field_name, file_path)
                print(f"{field_name}: {field_value}")
            except ValueError as e:
                print(str(e))
