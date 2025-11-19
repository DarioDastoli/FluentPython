#Example 2-5. Initializing a tuple and an array from a generator expression

symbols = '$¢£¥€¤'

#If the generator expression is the single argument in a function call, there is no
#need to duplicate the enclosing parentheses.
tuple(ord(symbol) for symbol in symbols)

import array

#The array constructor takes two arguments, so the parentheses around the generator
#expression are mandatory. The first argument of the array constructor
#defines the storage type used for the numbers in the array
array.array('I', (ord(symbol) for symbol in symbols))