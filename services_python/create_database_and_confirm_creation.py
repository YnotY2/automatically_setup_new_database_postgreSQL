import psycopg2
from config.settings import postgresql_db_new_name, existing_postgresql_admin_usr, existing_postgresql_admin_usr_passwd, existing_postgresql_admin_db, existing_postgresql_admin_db_port
from utils.logger import setup_logger
from utils.colors import Colors

# Setup logger with service name
service_name = "create_database_and_confirm_creation"
logger = setup_logger(service_name)

def create_database_and_confirm_creation():

    connection = psycopg2.connect(
        database=existing_postgresql_admin_db,
        user=existing_postgresql_admin_usr,
        host="localhost",
        password=existing_postgresql_admin_usr_passwd,
        port=existing_postgresql_admin_db_port)


    logger.info(f"{Colors.CYAN}Attempting to connect to the following database:{Colors.END}")
    logger.info(f"{Colors.BLUE}database:{Colors.END}{Colors.MAGENTA}        '{existing_postgresql_admin_db}'       {Colors.END}")
    logger.info(f"{Colors.BLUE}user:{Colors.END}{Colors.MAGENTA}            '{existing_postgresql_admin_usr}'         {Colors.END}")
    logger.info(f"{Colors.BLUE}password:{Colors.END}{Colors.MAGENTA}        '{existing_postgresql_admin_usr_passwd}'         {Colors.END}")
    logger.info(f"{Colors.BLUE}host:{Colors.END}{Colors.MAGENTA}            'localhost'         {Colors.END}")
    logger.info(f"{Colors.BLUE}port:{Colors.END}{Colors.MAGENTA}            '{existing_postgresql_admin_db_port}'        {Colors.END}")
    print("")

    try:
        connection.autocommit = True  # Disable autocommit
        cursor = connection.cursor()
        logger.info(f"{Colors.GREEN}Successfully connected to the database.{Colors.END}")

    except Exception as e:
        logger.info(f"{Colors.RED}Error: {e}.{Colors.END}")
        return False

    logger.info(f"{Colors.CYAN}Attempting to create database:{Colors.END}")
    logger.info( f"{Colors.GREEN}Database:{Colors.END}{Colors.MAGENTA}      '{postgresql_db_new_name}'{Colors.END}")

    try:
        # Create the specified database
        cursor.execute(f"CREATE DATABASE {postgresql_db_new_name};")

    except Exception as e:
        logger.error(f"{Colors.RED}An error occurred: {e}{Colors.END}")
        return False


    finally:
        # Revert autocommit to default
        connection.autocommit = False

    print("")
    logger.info(f"{Colors.CYAN}Attempting to confirm creation of database:{Colors.END}")
    logger.info(f"{Colors.GREEN}Database:{Colors.END}{Colors.MAGENTA}      '{postgresql_db_new_name}'{Colors.END}")

    try:

        # Confirm creation of the specified database
        cursor.execute(f"SELECT datname FROM pg_database WHERE datname = '{postgresql_db_new_name}';")
        result = cursor.fetchone()

        if result:
            logger.info(f"{Colors.GREEN}Database:{Colors.MAGENTA}     '{postgresql_db_new_name}'{Colors.END} {Colors.GREEN} created successfully.{Colors.END}")
            return True
        else:
            logger.info(f"{Colors.GREEN} '{postgresql_db_new_name}' creation failed.{Colors.END}")
            return False


    except Exception as e:
        logger.error(f"{Colors.RED}An error occurred: {e}{Colors.END}")
        return False


    finally:
        cursor.close()
        connection.close()
        print("")

if __name__ == "__main__":
    create_database_and_confirm_creation()
