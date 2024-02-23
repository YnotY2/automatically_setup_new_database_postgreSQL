from utils.colors import Colors
from utils.logger import setup_logger

from services_python.start_postgresql import start_postgresql
from services_python.stop_postgresql import stop_postgresql
from services_python.restart_postgresql import restart_postgresql
from services_python.check_status_postgresql_service import check_status_postgresql_service

from services_python.create_postgresql_new_user import create_new_postgresql_user
from services_python.create_database_and_confirm_creation import create_database_and_confirm_creation
from services_python.edit_pg_hba_postgresql_config_file import edit_pg_hba_postgresql_config_file
from services_python.create_schema_new_database import create_schema_new_database
from services_python.verify_permissions_usr_db_granted import verify_permissions_usr_db_granted
from services_python.log_successful_creation_db_layout import log_successful_creation_db_layout

# Setup logger with service name
service_name = "main"
logger = setup_logger(service_name)

def main():
    try:

        logger.info(f"{Colors.CYAN}Starting{Colors.END}{Colors.YELLOW} main.py{Colors.END} {Colors.CYAN} python3 script ...{Colors.END}")


        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} start_posgresql.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        start_postgresql()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} create_new_postgresql_user.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        create_new_postgresql_user_returned = create_new_postgresql_user()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} create_database_and_confirm_creation.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        create_database_and_confirm_creation_returned = create_database_and_confirm_creation()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} stop_postgresql.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        stop_postgresql()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} check_status_postgresql_service.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        check_status_postgresql_service()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} edit_pg_hba_postgresql_config_file.py.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        edit_pg_hba_postgresql_config_file_returned = edit_pg_hba_postgresql_config_file()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} restart_postgresql.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        restart_postgresql()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} check_status_postgresql_service.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        check_status_postgresql_service()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} create_schema_new_database.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        create_schema_new_database_returned = create_schema_new_database()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} verify_permissions_usr_db_granted.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        verify_permissions_usr_db_granted_returned = verify_permissions_usr_db_granted()


        # Finally we will verify all needed code returns True before printing every detail successfully created to logger and terminal window!
        logger.info(f"{Colors.BLUE}Checking if all services have returned 'True' to confirm successful creation of everything {Colors.END}")
        print("")
        try:
            if create_new_postgresql_user_returned:
                try:
                    if create_database_and_confirm_creation_returned:
                        try:
                            if edit_pg_hba_postgresql_config_file_returned:
                                try:
                                    if create_schema_new_database_returned:
                                        try:
                                            if verify_permissions_usr_db_granted_returned:
                                                logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} log_successful_creation_db_layout.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
                                                # Call the actual success log!
                                                log_successful_creation_db_layout()

                                            else:
                                                logger.error(
                                                    f"{Colors.RED}Error: While attempting to confirm successful permission for user on database{Colors.END}")
                                        except Exception as e:
                                            logger.error(
                                                f"{Colors.RED}Error: While attempting to confirm successful permission for user on database {e} {Colors.END}")

                                    else:
                                        logger.error(
                                            f"{Colors.RED}Error: While attempting to confirm successful database-schema creation{Colors.END}")
                                except Exception as e:
                                    logger.error(
                                        f"{Colors.RED}Error: While attempting to confirm successful database-schema creation {e} {Colors.END}")

                            else:
                                logger.error(f"{Colors.RED}Error: While attempting to confirm successful edit of 'pg_hba.conf' postgreSQL auth-file{Colors.END}")
                        except Exception as e:
                            logger.error(f"{Colors.RED}Error: While attempting to confirm successful edit of 'pg_hba.conf' postgreSQL auth-file {e} {Colors.END}")

                    else:
                        logger.error(f"{Colors.RED}Error: While attempting to confirm database creation{Colors.END}")
                except Exception as e:
                    logger.error(f"{Colors.RED}Error: While attempting to confirm database creation {e} {Colors.END}")

            else:
                logger.error(f"{Colors.RED}Error: While attempting to confirm user creation{Colors.END}")
        except Exception as e:
            logger.error(f"{Colors.RED}Error: While attempting to confirm user creation {e} {Colors.END}")










    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}{Colors.END}")

if __name__ == "__main__":
    main()
