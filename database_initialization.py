""" Endpoint to create SQLite data model """
import os
from database.interface.sql_operations import SQLOperations

# SQL scripts to be defined as routines
INIT_DATABASE_SQL_SCRIPTS = [os.path.join("init", init) for init in os.listdir("init")]

def main() -> None:
    for script in INIT_DATABASE_SQL_SCRIPTS:
        SQLOperations.execute_sql_script(script)

if __name__ == "__main__":
    main()
