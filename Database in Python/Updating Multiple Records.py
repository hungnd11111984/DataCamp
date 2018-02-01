# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records
stmt = stmt.where(state_fact.columns.census_region_name == 'West')

print(stmt)
# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

Results 
UPDATE state_fact SET notes=:notes WHERE state_fact.census_region_name = :census_region_name_1
13
