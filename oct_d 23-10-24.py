# string functions
s = "pythn anyware"
# count() to find the number of characters
s1 = s.count('5')
print(s1)
# find() function
s2 = s.find('p')
print(s2)
a = "python in python"
b = a.find('a')
print(b)
#replace function
s = "python anyware"
s3 = s.replace('p','k')
print(s)
print(s3)
print(s[::1])
print('reversing')
print(s[::-1])
print(s[::-2])
print(s)
print(s.isdigit())
a = 'python 123'
print(a.isdigit())
print(a.isalpha())
s = 'python p1'
print(len(s))
h = s.strip()  # To removing the spaces in stating and ending of collection
print(len(h))
s = 'python anyware'
print(s)
# spilt data
print(s.split('n'))