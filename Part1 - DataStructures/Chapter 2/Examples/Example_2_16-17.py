#Example 2-16. A riddle

t = (1, 2, [30, 40])
t[2] += [50, 60]

"""
What happens next? Choose the best answer:
A. t becomes (1, 2, [30, 40, 50, 60]).
B. TypeError is raised with the message 'tuple' object does not support item
assignment.
C. Neither.
D. Both A and B. -->  X
"""

#Example 2-17. The unexpected result: item t2 is changed and an exception is raised
"""
t = (1, 2, [30, 40])
t[2] += [50, 60]

Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

print (t)
(1, 2, [30, 40, 50, 60])

"""

