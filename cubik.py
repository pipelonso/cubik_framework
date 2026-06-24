import sys
from cubik.CommandHandler import CommandHandler

command_handler = CommandHandler(sys.argv)
command_handler.handle_command(sys.argv[1])
command_handler.execute()


