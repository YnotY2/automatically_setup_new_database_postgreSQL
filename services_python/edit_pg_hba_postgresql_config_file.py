from config.settings import postgresql_db_new_name, postgreSQL_db_new_usr
from utils.logger import setup_logger
from utils.colors import Colors

# Setup logger with service name
service_name = "edit_pg_hba_postgresql_config_file.py"
logger = setup_logger(service_name)

def edit_pg_hba_postgresql_config_file():

    # Path to the pg_hba.conf file
    pg_hba_conf_path = "/etc/postgresql/16/main/pg_hba.conf"

    # Line to add for the new user with "md5" authentication method
    new_line = f"local\t{postgresql_db_new_name}\t{postgreSQL_db_new_usr}\tmd5\n"

    # Log statement to terminal and "app.log"
    logger.info(f"{Colors.BLUE}Attempting to add new entry within 'pg_hba.conf' postgreSQL authentication file:{Colors.END}")
    logger.info(f"{Colors.CYAN}Database:            {Colors.MAGENTA}{postgresql_db_new_name}{Colors.END}")
    logger.info(f"{Colors.CYAN}User:                {Colors.MAGENTA}{postgreSQL_db_new_usr}{Colors.END}")
    print("")

    formatted_string = "# TYPE  DATABASE  USER     ADDRESS     METHOD"
    context_formated_string = f"local	  {postgresql_db_new_name}	 {postgreSQL_db_new_usr}     md5"

    logger.info(f"{Colors.BLUE}Attempting to add following line:{Colors.END}")
    logger.info(f"{Colors.CYAN}Database:            {Colors.MAGENTA}{postgresql_db_new_name}{Colors.END}")
    logger.info(f"{Colors.MAGENTA}{formatted_string}{Colors.END}")
    logger.info(f"{Colors.MAGENTA}{context_formated_string}{Colors.END}")
    print("")

    try:
        # Open the pg_hba.conf file in append mode
        with open(pg_hba_conf_path, "a") as file:
            file.write(new_line)

        logger.info(f"{Colors.GREEN}Line added successfully to pg_hba.conf.{Colors.END}")

    except FileNotFoundError:
        logger.error("pg_hba.conf file not found.")
    except Exception as e:
        logger.error(f"An error occurred while editing pg_hba.conf: {e}")

if __name__ == "__main__":
    edit_pg_hba_postgresql_config_file()
