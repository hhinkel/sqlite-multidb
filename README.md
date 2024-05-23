**Alembic migrations in SQLite with multiple databases (and eventually Docker)**

1. Setup directory and virtual enviroment
2. Install packages
3. Create main.py with enough db engines for the databases you are going to create
4. Run main.py to create the databases
5. Install Alembic if you didn't in step 2
   - `pip install alembic`
6. Initialize Alembic using the multidb template
   - `alembic init --template multidb migrations
7. Open the alembic.ini file
8. make sure your databases match the names you gave them when you set them up
   - `databases = engine1, engine2`
9. If they dont change them in the databases line and the section heads that follow the databases line.
10. Under the engine sections change the default line `driver://user:pass@localhost/dbname` to the proper SQLite call
    - `sqlite:///db/sql_app.db`
11. Open the migrations/env.py file
12. If you want to be able to autogenerate you migrations
    - import your models
    - then create the target metadata
13. Create you models using the appropriate Base depending on what database you want the table in.
14. Run the following command to generate the migrations that will create the tables in the databases
    -`alembic revision --autogenerate -m "Create tables"`
    - You can add  `-n <dbname>` if you want the migration to be for a certain database.
15. Run `alembic upgrade head` to update the databases to the most recent alembic migration
    - You can also run `alembic upgrade <revision_number> to upgrade to a certain revision
    - And `alembic downgrade <revision_number>` to revert to a certain revision
