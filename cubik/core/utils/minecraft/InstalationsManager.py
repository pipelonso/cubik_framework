import os
import platform
from pathlib import Path

class InstallationManager:
    
    def __init__(self):
        pass

    def detect_base_minecraft_path():

        system = platform.system()
        home = Path.home()

        if system == "Windows":
            return home / "AppData/Roaming/.minecraft"
            
        elif system == "Linux":
            standard_path = home / ".minecraft"
            if standard_path.exists():
                return standard_path
            
            flatpak_path = home / ".var/app/com.mojang.minecraft/.minecraft"
            if flatpak_path.exists():
                return flatpak_path
                
            snap_path = home / "snap/minecraft/common/.minecraft"
            if snap_path.exists():
                return snap_path
                
        elif system == "Darwin":  
            return home / "Library/Application Support/minecraft"
        
        return None