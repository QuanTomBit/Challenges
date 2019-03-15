
from sys import argv

'''
    97-122
    32
    65-90

    "Hello World" reverse ascii = 001801411111782311180180110127
'''

def decode(nums: str) -> str:
    res = "" # String to append characters to and then return

    nums = nums[::-1] # Reverse operation
    code = '' # Will hold 0-3 digits (as strings). If len is 2 or 3, check ascii

    for n in nums:
        if len(code) < 3:
            code += n

        c = int(code) # Convert to int and store in new variable to check range

        if len(code) == 2:
            if 65 <= c <= 90 or 97 <= c <= 99 or c == 32: # Valid 2-digit range
                res += chr(c) # Append to result
                code = '' # Reset
        elif len(code) == 3:
            if 100 <= c <= 122: # Valid 3-digit range
                res += chr(c) # Append to result
                code = '' # Reset
            else:
                # If nothing found in 3-digit, reset to last 2 digits to check
                code = code[1:]

                # Now check these digit validity
                if 65 <= c <= 90 or 97 <= c <= 99 or c == 32: # Valid 2-digit range
                    res += chr(c) # Append to result
                    code = '' # Reset
                else:
                    # Again, nothing found. Thus, invalid
                    code = '' # Reset


    return res

if __name__ == "__main__":
    asciiNums = argv[1]
    print(decode(asciiNums))
