# Print Welcome Mesage 
print('Hello World')

# Using value
message = 'Hello World'
print(len(message)) # Length of character 
print(message[0]) # Print first character
print(message[0:5]) # Print from 1 - 5 character 
print(message[6:]) # Print from 6 to the end 

print(message.lower()) # Display lower string 
print(message.find('World')) # Find character 

#message = message.replace('World','Universe') # Replace character 
#print message
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome!'
print message

message = '{}, {}. Welcome!'.format(greeting,name)
print message

print (dir(name))	# 
print (help(str))	# find all functions for string 
print (help(str.lower)) # Find help for lower function 

