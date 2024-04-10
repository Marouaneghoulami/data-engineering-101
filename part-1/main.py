import logging
from src.util.scheduler import Scheduler

logging.basicConfig(level = logging.INFO)
LOGGER = logging.getLogger(__name__)

def main():
    LOGGER.info("Welcome to your Data Engineering 101 guide!")
    scheduler = Scheduler()
    scheduler.schedule_jobs()

if __name__ == '__main__':
    main()
