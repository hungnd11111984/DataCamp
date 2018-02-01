# Simple Function 
# def hello_func(): 
#	return 'Hello Function.'

# Pass parameter
#def hello_func(greeting):
#	return '{} Function.'.format(greeting)
# print hello_func()
# Dry 

# Set default value 
def hello_func(greeting,name = 'You'):
	return '{}, {}'.format(greeting,name)



#print (hello_func())
#print (hello_func('Hello', name = 'Corey'))


def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

#student_info('Math','Art', name = 'John', age = 22)

courses = ['Math','Art']
infor = {'name':'John', 'age':22 }
student_info(courses,infor)
student_info(*courses,**infor)	# Unpack value 

month_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
	return year % 4 ==0 and (year % 100 != 0 or year % 400 ==0)

def days_in_month(year,month):
	if not 1 <= month <= 12:
		return 'Invalid month'
	if month == 2 and is_leap(year):
		return 29 
	return month_days[month]

print(is_leap(2020))
print(days_in_month(2017,1))