from cubik.system.storage.FileSystemManager import FileSystemManager

class InitProcess:

    def __init__(self):
        self.fileSystemManager = FileSystemManager()
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

        pass

    def _scan_for_existing_structure(self) -> bool:
        
        exists = self.fileSystemManager.verify_file_exists("cubik.json")
        exists = self.fileSystemManager.verify_file_exists("cubik.config.json")
        exists = self.fileSystemManager.verify_path_exists("out")
        exists = self.fileSystemManager.verify_path_exists("src")

        return exists
