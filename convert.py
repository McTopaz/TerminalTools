'''
Convert input to different number base.

Example
    * convert.py 123            Converts from int 123 to hex 7B.
    * convert.py 123:4          Converts from int 123 to hex 0x007B.
    * convert.py 0x7B           Converts from hex 7B to 123.
    * convert.py Hello          Converts from string to hex, 48656C6C6F, will use ASCII as default encoding.
    * cpnvert.py Hello utf8     Converts from string to hex, 48656C6C6F, will use UTF8 as encoding.
    * convert.py 48656C6C6F     Convert from hex to string, Hello.

'''

import sys
import string
from encodings.aliases import aliases

if len(sys.argv) == 1:
    print("Error: Too few arguments.")
    sys.exit()

input = sys.argv[1]
#print("Input: " + input)

# Convert integer to hex with fixed length: 123:6 = 00007B.
# Check if input contains ':' with format: <number>:<length>.
if ":" in input and input[:input.index(":")].isdigit() and input[input.index(":")+1].isdigit():
    index = input.index(":")
    value = int(input[:index])
    length = int(input[index+1:])
    print("0x%0*X"%(length, value))
    
# Convert integer to hex: 123 = 7B.
elif input.isdigit():
    value = int(input)
    print("%X"%(value))

# Convert hex to int: 0x7B = 123.
elif input.startswith("0x"):
    value = input[2:]
    value = int(value, 16)
    print(value)
 
# Convert hex string to string.
elif all(c in string.hexdigits for c in input):
    data = []
    for start in range(0, len(input), 2):

        # Try to convert hex string to int.
        try:
            temp = int(sys.argv[1][start:start + 2], 16)
            data.append(temp)
        except:
            print("Error: '%s' contains a non hexadecimal number."%(input))
            sys.exit()
    value = "".join(chr(i) for i in data)
    print(value)
 
# Convert string to hex with custom encoding.
# Check if the input is string and of the given encoding exist.
elif isinstance(input, str) and len(sys.argv) >= 3 and isinstance(sys.argv[2], str) and sys.argv[2] in aliases:
    encoding = sys.argv[2]
    array = bytearray(input, encoding)
    hex = "".join("%02X"%(i) for i in array)
    print(hex)
 
# Convert string to hex with ASCII encoding.
elif isinstance(input, str):
    array = bytearray(input, 'ascii')
    hex = "".join("%02X"%(i) for i in array)
    print(hex)

# Unknown input type.
else:
    print("Error: Unknown type.")