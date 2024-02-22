from utils.colors import Colors
from utils.logger import setup_logger

from services_python.start_postgresql import start_postgresql
from services_python.stop_postgresql import stop_postgresql
from services_python.restart_postgresql import restart_postgresql
from services_python.check_status_postgresql_service import check_status_postgresql_service
from services_python.connect_db import connect_db
from services_python.quit_db_connection import quit_db_connection
from services_python.create_postgresql_new_user import create_new_postgresql_user
from services_python.create_database_and_confirm_creation import create_database_and_confirm_creation
from services_python.edit_pg_hba_postgresql_config_file import edit_pg_hba_postgresql_config_file

from services_python.create_schema_new_database import create_schema_new_database

# Setup logger with service name
service_name = "main"
logger = setup_logger(service_name)

logger.info("HIIIIIIIIIIIIIIIIIIIIIII")
def main():
    try:

        logger.info(f"{Colors.CYAN}Starting{Colors.END}{Colors.YELLOW} main.py{Colors.END} {Colors.CYAN} python3 script ...{Colors.END}")


        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} start_posgresql.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        start_postgresql()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} create_new_postgresql_user.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        create_new_postgresql_user()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} create_database_and_confirm_creation.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        create_database_and_confirm_creation()

       # logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} connect_db.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
       # cursor = connect_db()

       # logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} quit_db_connection.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
       # quit_db_connection(cursor)

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} stop_postgresql.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        stop_postgresql()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} check_status_postgresql_service.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        check_status_postgresql_service()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} edit_pg_hba_postgresql_config_file.py.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        edit_pg_hba_postgresql_config_file()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} restart_postgresql.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        restart_postgresql()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} check_status_postgresql_service.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        check_status_postgresql_service()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} create_schema_new_database.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        create_schema_new_database()




    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}{Colors.END}")

if __name__ == "__main__":
    main()
