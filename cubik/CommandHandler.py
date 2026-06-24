from cubik.commands.core.HelpCommand import HelpCommand
from cubik.commands.core.InitCommand import InitCommand
from cubik.commands.core.BaseCommand import BaseCommand

class CommandHandler:

    def __init__(self, raw_command: list[str]):
        self.raw_command = raw_command
        
        self.commands = {
            "help": HelpCommand,
            "init": InitCommand
        }

        self.selected_command = None

    def register_command(self, command_name, function):
        self.commands[command_name] = function

    def handle_command(self, command_string: str):

        if command_string in self.commands:
            command = self.commands[command_string]()
            command.set_base_args(self.raw_command[1:])
            self.selected_command = command
            return command            
        else:
            return "Command not found."

    def execute(self):
        if self.selected_command and isinstance(self.selected_command, BaseCommand):
            return self.selected_command.execute()
        else:
            return "No command selected."