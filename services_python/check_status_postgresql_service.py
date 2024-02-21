import subprocess
from utils.colors import Colors
from utils.logger import setup_logger

# Set up logger with service name
service_name = "check_status_postgresql_service"
logger = setup_logger(service_name)


def check_status_postgresql_service():
    try:
        # Construct the command to execute the shell script
        # The path has a "." to indicate the start dir in this case main.py is located.
        script_path = "./services_sh/check_status_postgresql_service.sh"  # Adjust the path as necessary
        logger.info(f"{Colors.CYAN}Executing check_status_postgresql_service.sh script{Colors.END}")

        # Execute the shell script using subprocess, print the output directly to terminal
        process = subprocess.Popen(script_path, shell=True)
        #logger.info(f"{Colors.GREEN} {process} {Colors.END}")
        try:
            process.communicate()
            logger.info(f"{Colors.GREEN}Status check on postgreSQL service completed successfully.{Colors.END}")

        except Exception as e:
            logger.error(f"Error: {e}")


    except Exception as e:
        logger.error(f"Error: {e}")
        logger.error(f"{Colors.RED}Error: Executing check_status_postgresql_service.sh {Colors.END}")

if __name__ == "__main__":
    check_status_postgresql_service()
