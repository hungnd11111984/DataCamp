# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select manager's and their employees names: stmt
stmt = select(
    [managers.columns.name.label('manager'),
     employees.columns.name.label('employee')]
)

# Match managers id with employees mgr: stmt
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Order the statement by the managers name: stmt
stmt = stmt.order_by(managers.columns.name)

print(stmt)
# Execute statement: results
results = connection.execute(stmt).fetchall()

# Print records
for record in results:
    print(record)

##############
Results 
SELECT employees_1.name AS manager, employees.name AS employee 
FROM employees AS employees_1, employees 
WHERE employees_1.id = employees.mgr ORDER BY employees_1.name
('FILLMORE', 'GRANT')
('FILLMORE', 'ADAMS')
('FILLMORE', 'MONROE')
('GARFIELD', 'JOHNSON')
('GARFIELD', 'LINCOLN')
('GARFIELD', 'POLK')
('GARFIELD', 'WASHINGTON')
('HARDING', 'TAFT')
('HARDING', 'HOOVER')
('JACKSON', 'HARDING')
('JACKSON', 'GARFIELD')
('JACKSON', 'FILLMORE')
('JACKSON', 'ROOSEVELT')