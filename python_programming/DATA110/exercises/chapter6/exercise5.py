# take the following python code that stores a sting:
# str = 'X-DSPAM-Confidence:0.8475'
# use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.
x_str = 'X-DSPAM-Confidence:0.8475'
start_float = x_str.find(':')
x_float = float(x_str[start_float+1:-1])
print(f'{x_float}')