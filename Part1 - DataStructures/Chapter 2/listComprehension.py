symbols = '$¢£¥€¤'
codes = []

#A for loop may be used to do lots of different things
for symbol in symbols:
    codes.append(ord(symbol))

#Listcomps - the intent of creating a new list is clear. Its goal is always to build a new list.
codes = [ord(symbol) for symbol in symbols]

#If the list comprehension spans more than two
#lines, it is probably best to break it apart or rewrite it as a plain old for loop.

beyond_ascii_ListComp = [ord(s) for s in symbols if ord(s) > 127]

#Map & Filter
beyond_ascii_MAP = list(filter(lambda c: c > 127, map(ord, symbols)))