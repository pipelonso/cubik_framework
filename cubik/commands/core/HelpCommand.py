from cubik.commands.core.BaseCommand import BaseCommand

class HelpCommand(BaseCommand):

    def __init__(self):    
        super().__init__()
        self.base_args = []
        self.name = 'help'

    def execute(self):
        if self.base_args:
            pass
        
    def set_base_args(self, base_args: list[str]):
        self.base_args = base_args