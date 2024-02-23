import subprocess
import os
from utils.logger import setup_logger
from utils.colors import Colors
from config.settings import postgresql_db_new_name


# Setup logger with service name
service_name = "create_schema_new_database"
logger = setup_logger(service_name)

def create_schema_new_database():
    try:
        # Path to the init-db.psql file
        init_db_script = "./config/init-db.psql"

        # Command to execute the init-db.psql script
        command = f"psql -U postgres -d {postgresql_db_new_name} -a -f {init_db_script}"

        logger.info(f"{Colors.BLUE}Attempting to create specified schema for database:{Colors.END}")
        logger.info(f"{Colors.CYAN}Database:            {Colors.MAGENTA}{postgresql_db_new_name}{Colors.END}")
        print("")

        # Set PGPASSWORD environment variable
        os.environ['PGPASSWORD'] = "postgres"

        # Execute the command
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, env=os.environ)

            # Log the output
            logger.info(f"{Colors.BLUE}Output of creating schema for database {Colors.END} {Colors.MAGENTA}{postgresql_db_new_name}:{Colors.END}")
            logger.info(result.stdout)
            print("")

            logger.info(f"{Colors.GREEN}Schema for database: {Colors.END}{Colors.MAGENTA}{postgresql_db_new_name}{Colors.END}{Colors.GREEN} created successfully.{Colors.END}")
            print("")

        except Exception as e:
            logger.error(f"{Colors.RED}Error: Creating schema db; {e}{Colors.END}")



        # Unset PGPASSWORD environment variable
        del os.environ['PGPASSWORD']

        # Set PGPASSWORD environment variable
        os.environ['PGPASSWORD'] = "Oo51knSSV3OSwfuy8WFu"


        # Verify schema creation
        logger.info(f"{Colors.BLUE}Verifying schema creation...{Colors.END}")

        # Set a flag to keep track if all schema's have been created successfully
        all_schemas_created = True

        for schema_name in ["horca_parameters_client", "google_account_info", "standard_strings_review",
                            "created_horeca_reviews"]:
            verify_command = f"psql -U project_google_reviews_usr -d {postgresql_db_new_name} -c '\\dn {schema_name}'"
            verify_result = subprocess.run(verify_command, shell=True, check=True, capture_output=True, text=True, env=os.environ)

            # Check if the schema name is present in the output
            if schema_name in verify_result.stdout:
                logger.info(f"{Colors.GREEN}Schema:      {Colors.END}{Colors.MAGENTA}{schema_name}{Colors.END}{Colors.GREEN} verified to be created successfully.{Colors.END}")

            else:
                logger.error(f"{Colors.RED}Error: Schema {schema_name} not found.{Colors.END}")
                all_schemas_created = False

        print("")
        # Check if all schemas are created successfully
        if all_schemas_created:
            logger.info(
                f"{Colors.GREEN}All schemas created successfully!{Colors.END}")
        else:
            logger.error(f"{Colors.RED}Not all schemas created successfully.{Colors.END}")

    except subprocess.CalledProcessError as e:
        logger.error(
            f"{Colors.RED}Error occurred while creating schema for database {postgresql_db_new_name}: {e.stderr}{Colors.END}")

    except Exception as e:
        logger.error(f"{Colors.RED}An error occurred: {e}{Colors.END}")

    # Unset PGPASSWORD environment variable
    del os.environ['PGPASSWORD']
    print("")

if __name__ == "__main__":
    create_schema_new_database()
