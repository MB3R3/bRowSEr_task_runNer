from core.batch import BatchRunner
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

    if command == "batch":
        BatchRunner().run()
        return
    
    
    dispatcher = TaskDispatcher()

    dispatcher.execute(command)


if __name__ == "__main__":
    main()