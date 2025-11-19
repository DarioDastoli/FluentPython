#Example 2-1. Build a list of Unicode code points from a string
symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)