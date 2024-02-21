import psycopg2
from utils.colors import Colors
from utils.logger import setup_logger
from config.settings import postgresql_db_name, postgresql_db_passwd, postgresql_db_usr, postgresql_port, postgresql_host

# Set up logger with service name
service_name = "connect_db"
logger = setup_logger(service_name)

def quit_db_connection(cursor):

    connection = psycopg2.connect(
        database=postgresql_db_name,
        user=postgresql_db_usr,
        host=postgresql_host,
        password=postgresql_db_passwd,
        port=postgresql_port)

    logger.info(f"{Colors.CYAN}Attempting to quit connection to the following database:{Colors.END}")
    logger.info(f"{Colors.BLUE}database:{Colors.END}{Colors.MAGENTA}        {postgresql_db_name}         {Colors.END}")
    logger.info(f"{Colors.BLUE}user:{Colors.END}{Colors.MAGENTA}            {postgresql_db_usr}         {Colors.END}")
    logger.info(f"{Colors.BLUE}password:{Colors.END}{Colors.MAGENTA}        {postgresql_db_passwd}         {Colors.END}")
    logger.info(f"{Colors.BLUE}host:{Colors.END}{Colors.MAGENTA}            {postgresql_host}         {Colors.END}")
    logger.info(f"{Colors.BLUE}port:{Colors.END}{Colors.MAGENTA}            {postgresql_port}         {Colors.END}")

    try:
        # Close the cursor
        cursor.close()
        logger.info(f"{Colors.GREEN}Successfully quit cursor corresponding to the database.{Colors.END}")

    except Exception as e:
        logger.info(f"{Colors.RED}Error: {e}.{Colors.END}")

    try:
        # Close the connection
        connection.close()
        logger.info(f"{Colors.GREEN}Successfully quit connection to the database.{Colors.END}")

    except Exception as e:
        logger.info(f"{Colors.RED}Error: {e}.{Colors.END}")

    # Print a blank line to the terminal
    print("")

if __name__ == "__main__":
    quit_db_connection()
