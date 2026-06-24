from cubik.commands.core.BaseCommand import BaseCommand
from cubik.core.process.InitProcess import InitProcess

class InitCommand(BaseCommand):
     
    def __init__(self):
         super().__init__()
         self.name = 'init'


    def execute(self):

        init = InitProcess()
        init.run()
        
        return True
    
    def get_docs(self) -> str:
        return f"""
        The 'init' command initializes the project.
        Usage: cubik.py init [options]
        Options:
            --help      Show help for the 'init' command.
        """