import subprocess
import os
from utils.logger import setup_logger
from utils.colors import Colors
from config.settings import postgresql_db_new_name


# Setup logger with service name
service_name = "log_successful_creation_db_layout"
logger = setup_logger(service_name)


def log_successful_creation_db_layout():
    try:

        # Read and log the contents of db_layout_visual.txt
        with open("./config/db_layout_visual.txt", "r") as file:
            db_layout_visual_contents = file.read()

        logger.info(f"{Colors.BLUE}Layout of created database::{Colors.END}")
        logger.info(f"{Colors.YELLOW}{db_layout_visual_contents}{Colors.END}")

    except FileNotFoundError:
        logger.error("db_layout_visual.txt not found.")

    except Exception as e:
        logger.error(f"An error occurred while reading db_layout_visual.txt: {e}")

if __name__ == "__main__":
    log_successful_creation_db_layout()