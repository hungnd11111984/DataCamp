#  List 
courses = ['History','Math','Physics','ComSci']

print(courses)

print(len(courses))

print(courses[-1])

print(courses[:2])

#courses.append('Art')
#print(courses)

#courses.insert(0,'Art')
#print(courses)

courses_2 = ['Art','Education']

#courses.extend(courses_2) # Add individual item 
#courses.append(courses_2)

#courses.remove('Math') # Remove item 
#pooped = courses.pop()
#print(pooped)
print (courses)
#courses.reverse()
print(courses)
# Reverse method 

print(courses.index('ComSci'))
print('Art' in courses)


for item in courses: 
		print item

for index,course in enumerate(courses,start=1):
	print(index,course)

course_str = ', '.join(courses)

new_lists =  course_str.split(', ')
print(course_str)
print new_lists




# Tuple: Can't modify , immutable.
# Mutable 
list_1 = ['History','Math','Physics','ComSci']
list_2 = list_1
print list_1
print list_2
list_1[0] = 'Art'
print list_1
print list_2

tuple_1 = ('History','Math','Physics','ComSci')
tuple_2 = tuple_1
print tuple_1
print tuple_2
#tuple_1.a = 'Art' Can't append.
print tuple_1
print tuple_2


# Set : unoder, no duplicate 

cs_courses = {'History','Math','Physics','ComSci','ComSci'}
cs_courses2 = {'History','Math','Art','Design','ComSci'}

print (cs_courses)
print ('Math' in cs_courses)
print (cs_courses.union(cs_courses2))