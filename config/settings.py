import os

## Database PostgreSQL Credentials

# Creating the new user on database-postgreSQL
postgreSQL_db_new_usr = os.getenv("postgreSQL_db_new_usr", "project_google_reviews_usr")
postgresql_db_new_passwd = os.getenv("postgresql_db_new_passwd", "Oo51knSSV3OSwfuy8WFu")

# Creating the new database on PostgreSQL
postgresql_db_new_name = os.getenv("postgresql_db_new_name", "project_google_reviews")


postgresql_db_name = os.getenv("postgresql_db_name", "<name_here>")
postgresql_db_passwd = os.getenv("postgresql_db_passwd", "<passwd_here>")
postgresql_db_usr = os.getenv("postgresql_db_usr", "<user_here>")
postgresql_port = os.getenv("postgresql_port", "5432")      # Default port// Change if wanted
postgresql_host = os.getenv("postgresql_host", "localhost")      # Locally hosted db// Change if wanted

# Other credentials
