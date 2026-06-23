from cubik.commands.HelpCommand import HelpCommand

class CommandHandler:

    def __init__(self, raw_command: list[str]):
        self.raw_command = raw_command
        self.commands = {
            "help": HelpCommand,
        }

    def register_command(self, command_name, function):
        self.commands[command_name] = function

    def handle_command(self, command_string: str):
        

        if command_string in self.commands:
            return self.commands[command_string]
        else:
            return "Command not found."