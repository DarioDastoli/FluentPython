#Example 2-6. Cartesian product in a generator expression

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

#The generator expression yields items one by one; a list with all six T-shirt variations
#is never produced in this example.
