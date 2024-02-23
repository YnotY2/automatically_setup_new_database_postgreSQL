import psycopg2
from utils.logger import setup_logger
from utils.colors import Colors
from config.settings import postgresql_db_new_name, postgreSQL_db_new_usr, postgresql_db_new_passwd

# Setup logger with service name
service_name = "verify_permissions_usr_db_granted.py"
logger = setup_logger(service_name)

def verify_permissions_usr_db_granted():
    try:
        # Establish connection to the PostgreSQL database
        connection = psycopg2.connect(
            dbname=postgresql_db_new_name,
            user=postgreSQL_db_new_usr,
            password=postgresql_db_new_passwd,
            host="localhost",
            port="5432"
        )

        logger.info(f"{Colors.CYAN}Attempting to connect to the following database:{Colors.END}")
        logger.info(f"{Colors.BLUE}database:{Colors.END}{Colors.MAGENTA}        '{postgresql_db_new_name}'       {Colors.END}")
        logger.info(f"{Colors.BLUE}user:{Colors.END}{Colors.MAGENTA}            '{postgreSQL_db_new_usr}'         {Colors.END}")
        logger.info(f"{Colors.BLUE}password:{Colors.END}{Colors.MAGENTA}        '{postgresql_db_new_passwd}'         {Colors.END}")
        logger.info(f"{Colors.BLUE}host:{Colors.END}{Colors.MAGENTA}            'localhost'         {Colors.END}")
        logger.info(f"{Colors.BLUE}port:{Colors.END}{Colors.MAGENTA}            '5432'        {Colors.END}")

        # Create a cursor object
        cursor = connection.cursor()
        logger.info(f"{Colors.GREEN}Successfully connected to the database.{Colors.END}")
        print("")


        # Execute the SQL query to fetch permissions
        cursor.execute("""
            SELECT DISTINCT privilege_type
            FROM information_schema.table_privileges
            WHERE grantee = %s;
        """, (postgreSQL_db_new_usr,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Extract unique privilege types
        unique_privileges = set(row[0] for row in rows)

        # Define expected privilege types
        expected_privileges = {"INSERT", "SELECT", "UPDATE", "DELETE", "TRUNCATE", "REFERENCES", "TRIGGER"}

        # Check if all expected privileges are present in the response
        missing_privileges = expected_privileges - unique_privileges

        logger.info(f"{Colors.BLUE}Attempting to check if all expected/needed privileges are granted to:{Colors.END}")
        logger.info(f"{Colors.CYAN}User:                {Colors.MAGENTA}{postgreSQL_db_new_usr}{Colors.END}")
        logger.info(f"{Colors.CYAN}On Database:         {Colors.MAGENTA}{postgresql_db_new_name}{Colors.END}")
        print("")

        # Print the result
        if not missing_privileges:
            logger.info(f"{Colors.GREEN}All expected privileges are present in the response.{Colors.END}")
            logger.info(f"{Colors.BLUE}Permissions:{Colors.END}")

            for privilege in sorted(expected_privileges):
                explanation = {
                    "INSERT": "Allow to add new rows to a table.",
                    "SELECT": "Allow to retrieve data from a table.",
                    "UPDATE": "Allow to modify existing rows in a table.",
                    "DELETE": "Allow to remove rows from a table.",
                    "TRUNCATE": "Allow to remove all rows from a table.",
                    "REFERENCES": "Allow to create a foreign key constraint.",
                    "TRIGGER": "Allow to create triggers on a table."
                }.get(privilege, "")
                logger.info(f"{Colors.CYAN}{privilege:<10}{Colors.MAGENTA}\t{explanation}{Colors.END}")
        else:
            logger.error(f"{Colors.RED}Missing privileges: {', '.join(missing_privileges)}{Colors.END}")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}.{Colors.END}")

    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}.{Colors.END}")

if __name__ == "__main__":
    verify_permissions_usr_db_granted()
