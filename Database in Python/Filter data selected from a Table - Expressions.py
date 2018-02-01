# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

print (stmt)

# Loop over the ResultProxy and print the state and its population in 2000
for a in connection.execute(stmt):
    print(a.state, a.pop2000)

