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
    context_formatted_string = f"local\t{postgresql_db_new_name}\t{postgreSQL_db_new_usr}\tmd5"

    logger.info(f"{Colors.BLUE}Attempting to add following line:{Colors.END}")
    logger.info(f"{Colors.CYAN}Database:            {Colors.MAGENTA}{postgresql_db_new_name}{Colors.END}")
    logger.info(f"{Colors.MAGENTA}{formatted_string}{Colors.END}")
    logger.info(f"{Colors.MAGENTA}{context_formatted_string}{Colors.END}")
    print("")

    # Define the pattern to match, within the "pg_hba.conf"-file.
    pattern_words = ["local", "all", "postgres", "md5"]

    try:
        # Read the content of pg_hba.conf
        with open(pg_hba_conf_path, "r") as file:
            lines = file.readlines()

        # Find the index of the line containing the pattern
        index = None
        for i, line in enumerate(lines):
            line_words = line.split()
            if all(word in line_words for word in pattern_words):
                index = i
                break

        if index is None:
            logger.error(f"{Colors.RED}: Pattern not found in pg_hba.conf.{Colors.END}")
            return

        # Insert the new line after the line containing the pattern
        lines.insert(index + 1, new_line)

        try:
            # Write the updated content back to pg_hba.conf
            with open(pg_hba_conf_path, "w") as file:
                file.writelines(lines)

            logger.info(f"{Colors.GREEN}Line added successfully to pg_hba.conf.{Colors.END}")
            print("")

        except Exception as e:
            logger.error(f"{Colors.RED}An error occurred while editing pg_hba.conf: {e}{Colors.END}")
            print("")



    except FileNotFoundError:
        logger.error("pg_hba.conf file not found.")
        print("")

    except Exception as e:
        logger.error(f"An error occurred while editing pg_hba.conf: {e}")
        print("")


if __name__ == "__main__":
    edit_pg_hba_postgresql_config_file()
