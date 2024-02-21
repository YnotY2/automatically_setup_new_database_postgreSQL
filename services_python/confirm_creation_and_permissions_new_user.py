from config.settings import postgresql_db_new_name, postgreSQL_db_new_usr
from utils.logger import setup_logger
from utils.colors import Colors

# Setup logger with service name
service_name = "confirm_creation_and_permissions_new_user"
logger = setup_logger(service_name)

def confirm_creation_and_permissions_new_user():

    # Log statement to terminal and "app.log"
    logger.info(f"{Colors.BLUE}Attempting to confirm creation of the new-user to corresponding new-database:{Colors.END}")
    logger.info(f"{Colors.CYAN}Database:            {Colors.MAGENTA}{postgresql_db_new_name}{Colors.END}")
    logger.info(f"{Colors.CYAN}User:                {Colors.MAGENTA}{postgreSQL_db_new_usr}{Colors.END}")
    print("")



if __name__ == "__main__":
    confirm_creation_and_permissions_new_user()
