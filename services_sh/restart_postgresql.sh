#!/bin/bash

restart_postgresql() {
    sudo systemctl restart postgresql
    echo "PostgreSQL restarted successfully."
}

# Call the function to start PostgreSQL
restart_postgresql
