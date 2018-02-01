# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(select_stmt)
print(connection.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36: stmt
stmt = update(state_fact).values(fips_state=36)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(connection.execute(select_stmt).fetchall())


##### Results 
<script.py> output:
    SELECT state_fact.id, state_fact.name, state_fact.abbreviation, state_fact.country, state_fact.type, state_fact.sort, state_fact.status, state_fact.occupied, state_fact.notes, state_fact.fips_state, state_fact.assoc_press, state_fact.standard_federal_region, state_fact.census_region, state_fact.census_region_name, state_fact.census_division, state_fact.census_division_name, state_fact.circuit_court 
    FROM state_fact 
    WHERE state_fact.name = :name_1
    [('32', 'New York', 'NY', 'USA', 'state', '10', 'current', 'occupied', '', '0', 'N.Y.', 'II', '1', 'Northeast', '2', 'Mid-Atlantic', '2')]
    1
    [('32', 'New York', 'NY', 'USA', 'state', '10', 'current', 'occupied', '', '36', 'N.Y.', 'II', '1', 'Northeast', '2', 'Mid-Atlantic', '2')]
