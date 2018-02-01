# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select managers and counts of their employees: stmt
stmt = select([managers.columns.name, func.count(employees.columns.id)])

# Append a where clause that ensures the manager id and employee mgr are equal
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Group by Managers Name
stmt = stmt.group_by(managers.columns.name)

print(stmt)
# Execute statement: results
results = connection.execute(stmt).fetchall()

# print manager
for record in results:
    print(record)

################
Results 
SELECT employees_1.name, count(employees.id) AS count_1 
FROM employees AS employees_1, employees 
WHERE employees_1.id = employees.mgr GROUP BY employees_1.name
('FILLMORE', 3)
('GARFIELD', 4)
('HARDING', 2)
('JACKSON', 4)