import psycopg2
from utils.logger import setup_logger
from utils.colors import Colors
from config.settings import postgresql_db_new_name, postgresql_db_new_passwd, postgreSQL_db_new_usr


# Setup logger with service name
service_name = "log_successful_creation_db_layout"
logger = setup_logger(service_name)


def log_successful_creation_db_layout():
    try:
        logger.info(f"{Colors.YELLOW}Successfully created everything needed to access and utilise PostgreSQL datbase on following credentials:{Colors.END} ")
        logger.info(f"{Colors.BLUE}database:{Colors.END}{Colors.MAGENTA}        {postgresql_db_new_name}       {Colors.END}")
        logger.info(f"{Colors.BLUE}user:{Colors.END}{Colors.MAGENTA}            {postgreSQL_db_new_usr}         {Colors.END}")
        logger.info(f"{Colors.BLUE}password:{Colors.END}{Colors.MAGENTA}        {postgresql_db_new_passwd}         {Colors.END}")
        logger.info(f"{Colors.BLUE}host:{Colors.END}{Colors.MAGENTA}            localhost         {Colors.END}")
        logger.info(f"{Colors.BLUE}port:{Colors.END}{Colors.MAGENTA}            5432        {Colors.END}")
        print("")

    except Exception as e:
      logger.error(f"An error occurred while while trying to log to console {e}")

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
        logger.info(
            f"{Colors.BLUE}database:{Colors.END}{Colors.MAGENTA}        '{postgresql_db_new_name}'       {Colors.END}")
        logger.info(
            f"{Colors.BLUE}user:{Colors.END}{Colors.MAGENTA}            '{postgreSQL_db_new_usr}'         {Colors.END}")
        logger.info(
            f"{Colors.BLUE}password:{Colors.END}{Colors.MAGENTA}        '{postgresql_db_new_passwd}'         {Colors.END}")
        logger.info(f"{Colors.BLUE}host:{Colors.END}{Colors.MAGENTA}            'localhost'         {Colors.END}")
        logger.info(f"{Colors.BLUE}port:{Colors.END}{Colors.MAGENTA}            '5432'        {Colors.END}")

        # Create a cursor object
        cursor = connection.cursor()
        logger.info(f"{Colors.GREEN}Successfully connected to the database.{Colors.END}")
        print("")

        # Execute the SQL query to fetch permissions
        cursor.execute("""
            SELECT grantee, table_schema, table_name, privilege_type
            FROM information_schema.table_privileges
            WHERE grantee = %s;
        """, (postgreSQL_db_new_usr,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Log the output of the command
        logger.info(
            f"{Colors.CYAN}Successfully granted all privileges to user{Colors.MAGENTA} '{postgreSQL_db_new_usr}'{Colors.END}{Colors.CYAN} on corresponding database{Colors.END}{Colors.MAGENTA} '{postgresql_db_new_name}':{Colors.END}")
        for row in rows:
            logger.info(f"{Colors.YELLOW} {row[0]} | {row[1]} | {row[2]} | {row[3]}{Colors.END}")

        print("")

    except psycopg2.Error as e:
        logger.error(f"{Colors.RED}Error: {e}{Colors.END}")

    except Exception as e:
        logger.error(f"{Colors.RED}Error: while attempting to log permissions of user to corresponding db: {e}.{Colors.END}")


    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


    try:

        # Read and log the contents of db_layout_visual.txt
        with open("./config/db_layout_visual.txt", "r") as file:
            db_layout_visual_contents = file.read()

        logger.info(f"{Colors.BLUE}Layout of created database::{Colors.END}")
        logger.info(f"{Colors.YELLOW}{db_layout_visual_contents}{Colors.END}")

    except FileNotFoundError:
        logger.error("db_layout_visual.txt not found.")

    except Exception as e:
        logger.error(f"An error occurred while reading db_layout_visual.txt: {e}")

if __name__ == "__main__":
    log_successful_creation_db_layout()