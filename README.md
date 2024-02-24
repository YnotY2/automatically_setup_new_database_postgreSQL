# LambdaTest Environment Check Tool

## Overview

This tools allows you to automatically set-up a new PostgreSQl database with corresponding user, specified-schema and correct permissions *0-0*

## Prerequisites

Before using this tool, ensure you have the following prerequisites:

### Installed and set-up:

- Python 3.x
- PostgreSQL installed and set-up with a admin postgresql user. (e,g; "postgres")

## Usage
After you have successfully cloned the project into you're wanted directory on local machine you must set-up the following for the code/program to function correctly.

### Files:

- "init-db.psql" -file set-up within the ./config/<file_here> directory                 //make sure file name matches, currently a example file is present within the dir.
- "db_layout_visual.txt" -file set-up within the ./config/<file_here> direcory          //make sure file name matches, currently a example file is present within the dir.

### Settings: 

After setting up the needed file's you can navigate over the the; "./config/settings.py" direcory. This "settings.py" file is where you *need* specifiy the following; 

- New PostgreSQl user for you're datbase
- New PostgreSQL password for you're user 
- New PostgreSQL database (name)

  - Existing postgresql admin user
  - Existing postgresql admin password for you're user
  - Existing postgresql admin database (name)
  - Existing postgresql admin port (corresponing to admin database-name) 

  + Most systems have a default "postgresql" admin user and "postgresql" admin database, on default port "5432"

Settings.py file visualised; 
```python
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
```

### Finalise Set-Up:

1, Navigate to the following directory;  "path/to/dir/automatically_setup_new_datbase_postgreSQL" 
- Following files will be present within this directory:
  ```bash
  app.log  config  grant_permissions.py  main.py  requirements.txt  services_python  services_sh  utils  venv
  ```

2, Run the "grant_permissions.py" file located within the the directory to grant the nessecary permissions to our "services_python" and "services_sh" scripts.
  ```bash
  sudo python3 grant_permissions.py
  ```

3, Install the necessary dependencies, you can use pip:

   ```bash
   pip install -r requirements.txt
   ```


## Running code:
After you have completed full set-up listed above you are ready to utilise the tool! It is important to run the code "main.py" with sudo privledges, this is needed because we are adding a entry to the "pg_hba.conf" postgresql auth-file.

1, Navigate to the directory "path/to/dir/automatically_setup_new_datbase_postgreSQL"

2, 

```bash
sudo python3 main.py
```


#### YnotY2 
##### 𝕃𝕚𝕧𝕚𝕟𝕘 𝕚𝕤 𝔸 𝔻𝕪𝕚𝕟𝕘 𝔸𝕣𝕥  0-0
