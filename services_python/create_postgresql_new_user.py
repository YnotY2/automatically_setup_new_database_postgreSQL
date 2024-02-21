import subprocess
import os
from utils.logger import setup_logger
from utils.colors import Colors
from config.settings import postgreSQL_db_new_usr, postgresql_db_new_passwd

# Setup logger with service name
service_name = "create_postgresql_new_user"
logger = setup_logger(service_name)

def create_new_postgresql_user():
    # Set PGPASSWORD environment variable
    os.environ['PGPASSWORD'] = "postgres"

    # Command to create user with password
    create_user_command = f"sudo -u postgres psql -c \"CREATE USER {postgreSQL_db_new_usr} WITH PASSWORD '{postgresql_db_new_passwd}';\""

    # Log statement to terminal and "app.log"
    logger.info(f"{Colors.BLUE}Attempting to create a new database user with corresponding password:{Colors.END}")
    logger.info(f"{Colors.CYAN}User:            {Colors.MAGENTA}{postgreSQL_db_new_usr}{Colors.END}")
    logger.info(f"{Colors.CYAN}Password:        {Colors.MAGENTA}{postgresql_db_new_passwd}{Colors.END}")
    print("")

    # Execute the command
    try:
        subprocess.run(create_user_command, shell=True, check=True, env=os.environ)
        logger.info(f"{Colors.GREEN}User{Colors.END}{Colors.MAGENTA}  {postgreSQL_db_new_usr}{Colors.END}{Colors.GREEN} created successfully.{Colors.END}")

    except subprocess.CalledProcessError as e:
        logger.error(f"{Colors.RED}Error occurred: {e}{Colors.END}")


    # Confirm creation of user by attempting to login (this should fail)
    confirm_user_command = f"psql -U {postgreSQL_db_new_usr} -W"

    logger.info(f"{Colors.BLUE}Attempting to confirm creation of a new database user:{Colors.END}")
    logger.info(f"{Colors.CYAN}User:            {Colors.MAGENTA}{postgreSQL_db_new_usr}{Colors.END}")

    # Execute the command
    try:
        subprocess.run(confirm_user_command, shell=True, check=True, env=os.environ)

    except subprocess.CalledProcessError as e:
        logger.error(f"{Colors.RED}Error occurred: {e}{Colors.END}")

    print("")
    logger.info(f"{Colors.GREEN}The error should indicate: 'peer auth failed' because "
                f"we haven't yet added an entry to the 'pg_hba.conf' file for "
                f"the user database and the md5 authentication method.{Colors.END}")

    # Unset PGPASSWORD environment variable
    del os.environ['PGPASSWORD']
    print("")


if __name__ == "__main__":
    create_new_postgresql_user()
