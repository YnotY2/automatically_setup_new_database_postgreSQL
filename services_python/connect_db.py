import psycopg2
from utils.colors import Colors
from utils.logger import setup_logger
from config.settings import postgresql_db_name, postgresql_db_passwd, postgresql_db_usr, postgresql_port, postgresql_host

# Set up logger with service name
service_name = "connect_db"
logger = setup_logger(service_name)


def connect_db():

    connection = psycopg2.connect(
        database=postgresql_db_name,
        user=postgresql_db_usr,
        host=postgresql_host,
        password=postgresql_db_passwd,
        port=postgresql_port)


    logger.info(f"{Colors.CYAN}Attempting to connect to the following database:{Colors.END}")
    logger.info(f"{Colors.BLUE}database:{Colors.END}{Colors.MAGENTA}        {postgresql_db_name}         {Colors.END}")
    logger.info(f"{Colors.BLUE}user:{Colors.END}{Colors.MAGENTA}            {postgresql_db_usr}         {Colors.END}")
    logger.info(f"{Colors.BLUE}password:{Colors.END}{Colors.MAGENTA}        {postgresql_db_passwd}         {Colors.END}")
    logger.info(f"{Colors.BLUE}host:{Colors.END}{Colors.MAGENTA}            {postgresql_host}         {Colors.END}")
    logger.info(f"{Colors.BLUE}port:{Colors.END}{Colors.MAGENTA}            {postgresql_port}         {Colors.END}")

    try:
        cursor = connection.cursor()
        logger.info(f"{Colors.GREEN}Successfully connected to the database.{Colors.END}")
    except Exception as e:
        logger.info(f"{Colors.RED}Error: {e}.{Colors.END}")


    logger.info(f"{Colors.CYAN}Attempting to return database cursor for future execute actions:{Colors.END}")
    try:
        logger.info(f"{Colors.GREEN}Successfully returned cursor corresponding to above database.{Colors.END}")
        # Print a blank line to the terminal
        print("")
        return cursor

    except Exception as e:
        logger.info(f"{Colors.RED}Error: {e}.{Colors.END}")



if __name__ == "__main__":
    connect_db()
