# Key and value pair 
student = {'name': 'John','age':25,'course':['Math','ComSci']}
#student['phone'] = '5555-555'
#student['name'] = 'James'
#print (student['name'])
#print (student['course'][0])

#print(student.get('phone','Not Found'))	# Get value in case of not exist.
# student.update({'name':'James','age':26,'phone':'55-555-5555'})		# Update various values

#del student['age'] # Delete value 
#print student

#age = student.pop('age')
#print student
#print age

# How many key 
#print(len(student))
#print(student.keys())
#print(student.values())
#print(student.items())

for key,value in student.items():
		print(key,value)