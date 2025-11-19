a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(a == b)

b[-1].append(99)
print(a == b)
print(b)

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

fixed_tuple = (10, 'alpha', [1, 2])
mutable_tuple = (10, 'alpha', [1, 2])

print(fixed(fixed_tuple))
print(fixed(mutable_tuple))
