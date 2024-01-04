import psycopg2

db_config = {
    'host': 'host',
    'database': 'db_name',
    'user': 'username',
    'password': 'pswrd',
    'port': 'port',
}
connection = psycopg2.connect(**db_config)
cursor = connection.cursor()
empl_cre = """CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    department_id INT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);"""
cursor.execute(empl_cre)
dp_cre = """CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL
);"""
cursor.execute(dp_cre)
projects_cre="""CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    employee_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);"""
cursor.execute(projects_cre)
query = """SELECT departments.department_name, MAX(e.salary) AS max_salary
FROM employees e
JOIN departments d ON employees.department_id = departments.department_id
GROUP BY departments.department_name
ORDER BY max_salary DESC
LIMIT 5;
"""

cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()
