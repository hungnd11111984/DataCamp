# == != > < >= <= is 
# and or not 

language = 'Java'

if language == 'Python':
	print('language is Python')
elif language == 'Java':
	print('language is Java')
elif language == 'JavaScript':
	print('language is Java')	
else: 
	print('Not match')

user = 'Admin'
logged_in = False 

if user	== 'Admin' or logged_in: 
	print('Admin Page')
else:
	print('Bad Creds')

if not logged_in:
	print('Please log in')
else:
	pritn('Welcome')

a = [1,2,3]
#b = [1,2,3]
b = a 
print(id(a))
print(id(b))
print(a is b) # print(id(a)=id(b))

# False Value
	# False 
	# None
	# Zero of any numberic type 
	# Any empty sequancy / mapping '',().[],{}

condition1 = 0
condition2 = False
condition3 = None
condition4 = {}
if condition1 or condition1 or condition3 or condition4:
	print('True')
else:
	print('False')