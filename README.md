# Team assembler

## Running the program locally

1. Clone the source code:

```bash
git clone https://github.com/MykytaKuzmytskyi/team_assembler.git
cd team_assembler
```

2. Install PostgresSQL and create DB.
3. Install modules and dependencies:

```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

4. `.env_sample`
   This is a sample .env file for use in local development.
   Duplicate this file as .env in the root of the project
   and update the environment variables to match your
   desired config. You can use [djecrety.ir](https://djecrety.ir/)

5. Use the command to configure the database and tables:

```bash
python manage.py migrate
```

6. Start the app:

```bash
python manage.py runserver
```

### Run with docker

Docker should be installed

```commandline
docker-compose up --build
```
Your app should now be accessible at http://localhost:8000/ in your web browser.
- You can use following superuser (or create another one by yourself using the admin page):
    - Email: `admin@admin.com`
    - Password: `Us2ddTX7`

*REST API documentation*
----
**Employee**

- POST:      `create_employee/`             - create employee
- GET:       `employees/`                   - get a list of employees
- GET:       `employee/<id>/`               - get employee's detail info
- PUT/PATCH: `employee/<id>/`               - update employee
- DELETE:    `employee/<id>/`               - delete employee

**Team**

- GET:       `team/`                        - get a list of teams
- POST:      `team/`                        - create team
- GET:       `team/<id>/`                   - get team's detail info
- PUT/PATCH: `team/<id>/`                   - update team
- POST:      `team/<id>/add_employees/ `    - add employees to team by employee_ids [1, 2 ...]
- POST:      `team/<id>/remove_employees/ ` - remove employees to team by employee_ids [1, 2 ...]
- DELETE:    `team/<id>/`                   - delete team
