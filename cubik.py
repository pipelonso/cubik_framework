import sys
from cubik.CommandHandler import CommandHandler

command_handler = CommandHandler(sys.argv[1:])
command = command_handler.handle_command(sys.argv[1])

print(command)

