import os

class FileSystemManager:
    
    def __init__(self):
        self.latest_error = ""
        pass

    def create_directory(self, path: str):
        
        try:
            os.makedirs(path, exist_ok=True)
            return True
        except Exception as e:
            self.latest_error = f"Error creating directory {path}: {e}"
            print(self.latest_error)
            return False
    
    def create_file(self, path: str, content: str = ""):
        try:
            with open(path, 'w') as f:
                f.write(content)
            return True
        except Exception as e:
            self.latest_error = f"Error creating file {path}: {e}"
            print(self.latest_error)
            return False
        
    def create_file_bytes(self, path: str, content: bytes):
        try:
            with open(path, 'wb') as f:
                f.write(content)
            return True
        except Exception as e:
            self.latest_error = f"Error creating file {path}: {e}"
            print(self.latest_error)
            return False
    
    def verify_path_exists(self, path: str) -> bool:
        return os.path.exists(path)
    
    def verify_file_exists(self, path: str) -> bool:
        return os.path.isfile(path)
    
    def get_file_content(self, path: str) -> str:
        try:
            with open(path, 'r') as f:
                return f.read()
        except Exception as e:
            self.latest_error = f"Error reading file {path}: {e}"
            print(self.latest_error)
            return ""
    
    def get_latest_error(self) -> str:
        return self.latest_error