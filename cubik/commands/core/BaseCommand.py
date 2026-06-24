class BaseCommand:
    def __init__(self):
        self.base_args = []
        self.name = 'base_command'

    def execute(self):
        raise NotImplementedError("Subclasses must implement the execute method.")

    def set_base_args(self, base_args: list[str]):
        self.base_args = base_args


    def get_docs(self) -> str:
        return f"""
        {self.name} command documentation:
        Documentation not implemented for this command.
        """