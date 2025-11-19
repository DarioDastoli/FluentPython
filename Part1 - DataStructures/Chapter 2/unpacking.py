lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates

print(latitude)
print(longitude)

a = 'Hello'
b = 'Word'

print(a)
print(b)

a, b = b, a
print('swap')

print(a)
print(b)

print('---------------------------------------------')
print(divmod(20,8))
t = (20, 8)
#print(divmod(t)) #--> divmod expected 2 arguments, got 1
print(divmod(*t)) 

quotient, remainder = divmod(*t)
print(quotient, remainder)


import os

_, filename = os.path.split('/home/dario/.ssh/id_rsa.pub')

print(filename)



num1 = *range(4), 4
num2 = [*range(4), 4]
num3 = {*range(4), 4, *(5, 6, 7)}
print(num1)
print(num2)
print(num3)