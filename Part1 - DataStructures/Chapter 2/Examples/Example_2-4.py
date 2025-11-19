#Example 2-4. Cartesian product using a list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

#This generates a list of tuples arranged by color, then size.
tshirts = [(color, size) for color in colors 
                         for size in sizes]
print(tshirts)

#Note how the resulting list is arranged as if the for loops were nested in the same
#order as they appear in the listcomp.

for color in colors:
    for size in sizes:
        print((color,size))
