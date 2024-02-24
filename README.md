# LambdaTest Environment Check Tool

## Overview

This tools allows you to automatically set-up a new PostgreSQl database with corresponding user, specified-schema and correct permissions *0-0*
It is important to run the code "main.py" with sudo privledges, this is needed because we are adding a entry to the "pg_hba.conf" postgresql auth-file.

## Prerequisites

Before using this tool, ensure you have the following prerequisites:

### Installed and set-up:

- Python 3.x
- PostgreSQL installed and set-up with a admin postgresql user. (e,g; "postgres")

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


To install the necessary dependencies, you can use pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the **LamdaTest_Env_Check.py**, follow these steps:
1. **Upload your Application To LamdaTest-Platform**

   Documentation; https://www.lambdatest.com/support/docs/appium-java/

   Using App from local system:
   ```bash
   curl -u "LAMDATEST_USERNAME:LADMATEST_ACCESSKEY" -X POST "https://manual-api.lambdatest.com/app/upload/realDevice" -F "appFile=@"/Users/user/path/to/APP_NAME.apk"" -F "name="APP_NAME""
   ```
   
   You will recevie the needed credentials for following variables:
   `app_id`, `app_url`, `app_name`, `app_type`, 
   These parameters are used to check *your* LamdaTest Environment 0-0
   

2. **Install requirements**

   Within your saved LamdaTest_Env_Check.py directory, open terminal and paste command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set -credentials**

   You can easily set the credentials within LamdaTest_Env_Check.py:

   ```python
   LAMBDATEST_ACCESS_KEY = "LAMBDATEST_ACCESS_KEY_HERE"
   LAMBDATEST_USERNAME = "LAMBDATEST_USERNAME_HERE"
   BASE64_USERNAME_ACCESSKEY = "BASE64_USERNAME_ACCESSKEY_HERE"
   
   app_id = "UPLOADED_APP_ID_HERE"
   app_url = "UPLOADED_APP_URL_HERE"
   app_name = "UPLOADED_APP_NAME_HERE"
   app_type = "APP_TYPE_HERE"

   # Define the .json file available devices output directory:
   directory_path = "/Users/user/path/to/LamdaTest_Env_Check_results"
   
   # Define the "Real Devices" names we want to utilize
   real_device_name_01 = "Galaxy S23 Ultra"
   real_device_name_02 = "Galaxy S23 Ultra"
   real_device_name_03 = "Poco X3 Pro"
   real_device_name_04 = "Poco M4 Pro"
   real_device_name_05 = "Pixel 7"
   real_device_name_06 = "Pixel 7 Pro"
   ```

4. **Run LamdaTest_Env_Check.py**
   ```bash
   python3 LamdaTest_Env_Check.py
   ```
