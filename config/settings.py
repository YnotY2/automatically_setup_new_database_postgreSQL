import os

## Database PostgreSQL Credentials

# Creating the new user on database-postgreSQL
postgreSQL_db_new_usr = os.getenv("postgreSQL_db_new_usr", "<postgreSQL_db_new_usr_here>")        # e.g; "clothing_sales_usr"
postgresql_db_new_passwd = os.getenv("postgresql_db_new_passwd", "<postgresql_db_new_passwd_here>")        # e.g; "super_secure_password"

# Creating the new database on PostgreSQL
postgresql_db_new_name = os.getenv("postgresql_db_new_name", "<postgresql_db_new_name_here>")          # e.g; "clothing_sales"

# Credentials used for admin command on PostgreSQL aka "psql" terminal
existing_postgresql_admin_usr = os.getenv("existing_postgresql_admin_usr", "postgres")                      # e.g; "postgres", default admin-usr.
existing_postgresql_admin_usr_passwd = os.getenv("existing_postgresql_admin_usr_passwd", "postgres")        # e.g; "postgres", default admin-usr postgres password.
existing_postgresql_admin_db = os.getenv("existing_postgresql_admin_db", "postgres")                        # e.g; "postgres", default postgres admin password.
existing_postgresql_admin_db_port = os.getenv("existing_postgresql_admin_db_port", "5432")                  # e.g; "5432", default port.


## Other usefull cmds for manually login db //dont have any effect on code, no variables.
# psql -U <postgreSQL_db_new_usr> -d <postgresql_db_new_name>

## Drop user and database;
# dropdb -U <user> <db_name>
# dropuser -U <user> <db_name>