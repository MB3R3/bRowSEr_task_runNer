# from core.cli import CLI
# from tasks.open_site import open_site


# def main():
#     cli = CLI()
    
#     command = cli.get_command()

#     if command is None:

#         print("No command provided.\n")

#         print("Availabe commands: ")
#         print("  open")

#         return
#     if command == "open":

#         open_site()
#     else:
#         print(f"Unknown command: {command}")






# if __name__ == "__main__":
#     main()



from core.cli import CLI
from core.dispatcher import TaskDispatcher


def main():

    cli = CLI()

    command = cli.get_command()

    if command is None:

        print("No command provided.")

        print("\nAvailable commands:")

        print("  open")

        print("  login")

        print("  screenshot")

        print("  scrape")

        print("  download")

        return

    dispatcher = TaskDispatcher()

    dispatcher.execute(command)


if __name__ == "__main__":
    main()