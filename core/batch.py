from core.dispatcher import TaskDispatcher
from core.logger import logger


class BatchRunner:
    def __init__(self):

        self.dispatcher = TaskDispatcher()

        self.tasks = [
            "login",
            "screenshot",
            "scrape",
            "download"
        ]


    def run(self):
        logger.info("Batch started. ")

        print("\nStarting batch execution.... \n")

        for task in self.tasks:
            print(f"Running: {task} ")

            try:
                self.dispatcher.execute(task)
            except Exception as e:
                logger.error(e)

                print(f"Task {task} Failed")
        
        print("\n Batch Complete")
        
        logger.info("Batch finished! ")