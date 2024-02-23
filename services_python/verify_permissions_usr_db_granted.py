import psycopg2
from utils.logger import setup_logger
from utils.colors import Colors

# Setup logger with service name
service_name = "verify_permissions_usr_db_granted.py"
logger = setup_logger(service_name)


def verify_permissions_usr_db_granted(database_name, user):

    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        host="localhost",
        password="postgres",
        port="5432")

    logger.info(f"{Colors.CYAN}Attempting to connect to the following database:{Colors.END}")
    logger.info(f"{Colors.BLUE}database:{Colors.END}{Colors.MAGENTA}        'postgres'       {Colors.END}")
    logger.info(f"{Colors.BLUE}user:{Colors.END}{Colors.MAGENTA}            'postgres'         {Colors.END}")
    logger.info(f"{Colors.BLUE}password:{Colors.END}{Colors.MAGENTA}        'postgres'         {Colors.END}")
    logger.info(f"{Colors.BLUE}host:{Colors.END}{Colors.MAGENTA}            'localhost'         {Colors.END}")
    logger.info(f"{Colors.BLUE}port:{Colors.END}{Colors.MAGENTA}            '5432'        {Colors.END}")
    print("")

    try:
        connection.autocommit = True  # Disable autocommit
        cursor = connection.cursor()
        logger.info(f"{Colors.GREEN}Successfully connected to the database.{Colors.END}")

    except Exception as e:
        logger.info(f"{Colors.RED}Error: {e}.{Colors.END}")

    # Execute the SQL query to fetch permissions
    cursor.execute("""
        SELECT grantee, table_schema, table_name, privilege_type
        FROM information_schema.table_privileges
        WHERE grantee = %s;
    """, (user,))

    # Fetch all rows
    rows = cur.fetchall()

    # Print the output
    logger.info(f"{Colors.CYAN}   grantee   |      table_schema      |   table_name   | privilege_type {Colors.END}")
    logger.info(f"{Colors.CYAN}--------------+------------------------+----------------+----------------{Colors.END}")
    for row in rows:
        logger.info(f"{Colors.MAGENTA}{:<14}| {:<24}| {:<15}| {:<15}{Colors.END}".format(*row))

    # Close the cursor and connection
    cursor.close()
    cursor.close()

# Example usage
if __name__ == "__main__":
    verify_permissions_usr_db_granted()
