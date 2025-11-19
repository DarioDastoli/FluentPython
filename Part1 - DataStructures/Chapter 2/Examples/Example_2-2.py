#Example 2-2. Build a list of Unicode code points from a string, using a listcomp

symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols]

print(codes)