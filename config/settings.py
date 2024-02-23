import os

## Database PostgreSQL Credentials

# Creating the new user on database-postgreSQL
postgreSQL_db_new_usr = os.getenv("postgreSQL_db_new_usr", "project_google_reviews_usr")
postgresql_db_new_passwd = os.getenv("postgresql_db_new_passwd", "Oo51knSSV3OSwfuy8WFu")

# Creating the new database on PostgreSQL
postgresql_db_new_name = os.getenv("postgresql_db_new_name", "project_google_reviews")


# Other usefull cmds for manually login db
# psql -U <postgreSQL_db_new_usr> -d <postgresql_db_new_name>
# dropdb -U <user> <db_name>
# dropuser -U <user> <db_name>