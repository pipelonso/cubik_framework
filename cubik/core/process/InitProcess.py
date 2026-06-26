from cubik.core.registry.CubikRegistryManager import CubikRegistryManager
from cubik.system.storage.FileSystemManager import FileSystemManager

class InitProcess:

    def __init__(self):
        self.fileSystemManager: FileSystemManager = FileSystemManager()
        self.cubik_registry_manager: CubikRegistryManager = CubikRegistryManager()
        pass

    def run(self):

        print("""
              
             ▗▄▄▖▗▖ ▗▖▗▄▄▖ ▗▄▄▄▖▗▖ ▗▖    ▗▄▄▄▖▗▄▄▖  ▗▄▖ ▗▖  ▗▖▗▄▄▄▖▗▖ ▗▖ ▗▄▖ ▗▄▄▖ ▗▖ ▗▖
            ▐▌   ▐▌ ▐▌▐▌ ▐▌  █  ▐▌▗▞▘    ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌▗▞▘
            ▐▌   ▐▌ ▐▌▐▛▀▚▖  █  ▐▛▚▖     ▐▛▀▀▘▐▛▀▚▖▐▛▀▜▌▐▌  ▐▌▐▛▀▀▘▐▌ ▐▌▐▌ ▐▌▐▛▀▚▖▐▛▚▖ 
            ▝▚▄▄▖▝▚▄▞▘▐▙▄▞▘▗▄█▄▖▐▌ ▐▌    ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌▐▙▄▄▖▐▙█▟▌▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌
              
        """)

        print(" Scanning for existing project structure... ")

        exists = self._scan_for_existing_structure()

        if exists:
            print(" Project structure already exists. Initialization skipped.")
            return
        
        print(" Creating project structure... ")

        new_config = self.cubik_registry_manager.re_generate_default_config()

        project_name = None

        while project_name is None or project_name.strip() == "":
            project_name = input("✜ Enter the project name: ")

            if project_name is None or project_name.strip() == "":
                print(" Project name cannot be empty. Please try again.")

        new_config["project_name"] = project_name.strip()

        project_description = None

        while project_description is None or project_description.strip() == "":
            project_description = input("✜ Enter the project description (optional): ")

            if project_description is None or project_description.strip() == "":
                new_config["project_description"] = "Cubik framework datapack"

        new_config["project_description"] = project_description.strip()

        self.cubik_registry_manager.write_current_structure_to_file()

    def _scan_for_existing_structure(self) -> bool:
        
        exists = self.fileSystemManager.verify_file_exists(self.cubik_registry_manager.file_name)
        exists = self.fileSystemManager.verify_file_exists("cubik.config.json")
        exists = self.fileSystemManager.verify_path_exists("out")
        exists = self.fileSystemManager.verify_path_exists("src")

        return exists
