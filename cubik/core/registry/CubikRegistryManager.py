from cubik.system.storage.FileSystemManager import FileSystemManager
import json


class CubikRegistryManager:

    def __init__(self):
        self.registry = {}
        self.file_name = "cubik.json"
        self.file_system_manager: FileSystemManager = FileSystemManager()

    def register(self, key, value):
        if key in self.registry:
            raise ValueError(f"Key '{key}' is already registered.")
        self.registry[key] = value

    def unregister(self, key):
        if key not in self.registry:
            raise KeyError(f"Key '{key}' is not registered.")
        del self.registry[key]

    def get(self, key):
        return self.registry.get(key)

    def list_keys(self):
        return list(self.registry.keys())
    
    def get_current_file_content(self):
        return self.file_system_manager.get_file_content(self.file_name)
    
    def re_generate_default_config(self):
        self.registry = {
            "version": "1.0",
            "minecraft_version": "-",
            "description": "-",
            "project_name": "-",
            "author": "-",
            "format_pack": 0,
            "resource_pack_format_pack": 0,     
            "builders": []
        }
        return self.registry
    
    def write_current_structure_to_file(self):
        content = json.dumps(self.registry, indent=4)
        self.file_system_manager.create_file(self.file_name, content)