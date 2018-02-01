# Build a statement to select the state, sum of 2008 population and census
# division name: stmt
stmt = select([
    census.columns.state,
    func.sum(census.columns.pop2008),
    state_fact.columns.census_division_name
])

# Append select_from to join the census and state_fact tables by the census state and state_fact name columns
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name)
)

# Append a group by for the state_fact name column
stmt = stmt.group_by(state_fact.columns.name)

print(stmt)
# Execute the statement and get the results: results
results = connection.execute(stmt).fetchall()

# Loop over the the results object and print each record.
for record in results:
    print(record)

################################
Results 

SELECT census.state, sum(census.pop2008) AS sum_1, state_fact.census_division_name 
FROM census JOIN state_fact ON census.state = state_fact.name GROUP BY state_fact.name
('Alabama', 4649367, 'East South Central')
('Alaska', 664546, 'Pacific')
('Arizona', 6480767, 'Mountain')
('Arkansas', 2848432, 'West South Central')
('California', 36609002, 'Pacific')
('Colorado', 4912947, 'Mountain')
('Connecticut', 3493783, 'New England')
('Delaware', 869221, 'South Atlantic')
('Florida', 18257662, 'South Atlantic')
('Georgia', 9622508, 'South Atlantic')
('Hawaii', 1250676, 'Pacific')
('Idaho', 1518914, 'Mountain')
('Illinois', 12867077, 'East North Central')
('Indiana', 6373299, 'East North Central')
('Iowa', 3000490, 'West North Central')
('Kansas', 2782245, 'West North Central')
('Kentucky', 4254964, 'East South Central')
('Louisiana', 4395797, 'West South Central')
('Maine', 1312972, 'New England')
('Maryland', 5604174, 'South Atlantic')
('Massachusetts', 6492024, 'New England')
('Michigan', 9998854, 'East North Central')
('Minnesota', 5215815, 'West North Central')
('Mississippi', 2922355, 'East South Central')
('Missouri', 5891974, 'West North Central')
('Montana', 963802, 'Mountain')
('Nebraska', 1776757, 'West North Central')
('Nevada', 2579387, 'Mountain')
('New Hampshire', 1314533, 'New England')
('New Jersey', 8670204, 'Mid-Atlantic')
('New Mexico', 1974993, 'Mountain')
('New York', 19465159, 'Mid-Atlantic')
('North Carolina', 9121606, 'South Atlantic')
('North Dakota', 634282, 'West North Central')
('Ohio', 11476782, 'East North Central')
('Oklahoma', 3620620, 'West South Central')
('Oregon', 3786824, 'Pacific')
('Pennsylvania', 12440129, 'Mid-Atlantic')
('Rhode Island', 1046535, 'New England')
('South Carolina', 4438870, 'South Atlantic')
('South Dakota', 800997, 'West North Central')
('Tennessee', 6202407, 'East South Central')
('Texas', 24214127, 'West South Central')
('Utah', 2730919, 'Mountain')
('Vermont', 620602, 'New England')
('Virginia', 7648902, 'South Atlantic')
('Washington', 6502019, 'Pacific')
('West Virginia', 1812879, 'South Atlantic')
('Wisconsin', 5625013, 'East North Central')
('Wyoming', 529490, 'Mountain')