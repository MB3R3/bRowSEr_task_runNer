from tasks.open_site import open_site
from tasks.login import login
from tasks.screenshot import screenshot
from tasks.download import download
from tasks.scrape import scrape


class TaskDispatcher:
    def __init__(self):
        self.tasks = {
            "open": open_site,
            "login": login,
            "screenshot": screenshot,
            "download": download,
            "scrape": scrape
        }

    
    def execute(self, command):
        task = self.tasks.get(command)

        if task is None:
            print(f"Unrecognized command: {command}")
            print("\n Available Commands: ")
            for command in sorted(self.tasks):
                print(f"  {command}")
            
            return
        task()