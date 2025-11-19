#Example 2-3. The same list built by a listcomp and a map/filter composition
symbols = '$¢£¥€¤'

beyond_ascii_ListComp = [ord(s) for s in symbols if ord(s) > 127]

#Map & Filter
beyond_ascii_MAP = list(filter(lambda c: c > 127, map(ord, symbols)))

print(beyond_ascii_ListComp)
print(beyond_ascii_MAP)