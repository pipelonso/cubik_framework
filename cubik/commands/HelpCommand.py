class HelpCommand:
    def __init__(self, command_registry):
        self.command_registry = command_registry

    def execute(self, *args):
        if args:
            command_name = args[0]
            command = self.command_registry.get(command_name)
            if command:
                return f"Help for {command_name}: {command.help_text}"
            else:
                return f"No help available for '{command_name}'."
        else:
            return "Available commands: " + ", ".join(self.command_registry.keys())