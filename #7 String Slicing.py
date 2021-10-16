#slicing = create a substring by extracting elements from another existing string 
#    indexing[] or slice()
#    [start:stop:step]   


#indexing[] :
name = "Dayyan Ahmed"


first_name = name[0:6]  #You can also leave the starting point empty is starting from 0 
last_name = name[6:12]  #You can also leave the ending point empty if it ends at the end of the string
funky_name = name[0:12:2] #You can also leave start and stop empty if its slicing the entire value but keep the colons 
reversed_name = name[::-1] #This reverses a name only leave colons empty if you with to reverse the entire string 
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

#slice() : 
#Use negative slicing for an easier stop from the end of the value

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4,)

print(website1[slice])
print(website2[slice])

#https://www.youtube.com/watch?v=wGlnsJFnGAI&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=8





