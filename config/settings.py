import os

## Database PostgreSQL Credentials

# Creating the new user on database-postgreSQL
postgreSQL_db_new_usr = os.getenv("postgreSQL_db_new_usr", "project_google_reviews_usr")
postgresql_db_new_passwd = os.getenv("postgresql_db_new_passwd", "Oo51knSSV3OSwfuy8WFu")

# Creating the new database on PostgreSQL
postgresql_db_new_name = os.getenv("postgresql_db_new_name", "project_google_reviews")

# Credentials used for admin command on PostgreSQL aka "psql" terminal
existing_postgresql_admin_usr = os.getenv("existing_postgresql_admin_usr", "postgres")
existing_postgresql_admin_usr_passwd = os.getenv("existing_postgresql_admin_usr_passwd", "postgres")
existing_postgresql_admin_db = os.getenv("existing_postgresql_admin_db", "postgres")
existing_postgresql_admin_db_port = os.getenv("existing_postgresql_admin_db_port", "5432")


## Other usefull cmds for manually login db //dont have any effect on code, no variables.
# psql -U <postgreSQL_db_new_usr> -d <postgresql_db_new_name>

## Drop user and database;
# dropdb -U <user> <db_name>
# dropuser -U <user> <db_name>