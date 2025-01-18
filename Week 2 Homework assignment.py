# Task 1
x = 31
print(x, bin(x), (hex(x)))

# Task 2
x = 1.825
# print(bin(x))
# error :'float' object cannot be interpreted as an integer,
# as an option, we will have to convert the integer and decimal parts separately
# and then put them back together

x = 18
print(bin(x))

# Task 3
y = 0b1011
z = 0xA3
print(y, z)

# Task 4
x = 0b111011110
y = 0x16d
w = x + y
print("The sum of a and b: ", w)

# Task 5
w = x + y + z
print("The sum of x,y and z is", w)

# Compression

#Task 1
original_size = 167
dictionary_size = 16
compressed_text_size = 127
total = compressed_text_size + dictionary_size

percent_of_compression = (1 -((compressed_text_size +dictionary_size)/original_size))*100
# let us round the percent to 2 decimal places
percent_of_compression = round(percent_of_compression, 2)
print(percent_of_compression)

#Task 2

print(f"Compressed text size: {compressed_text_size} \n "
      f"Dictionary size: {dictionary_size}\n"
      f"Total: {total} \n "
      f"Original text size: {original_size}\n "
      f"Compression: {percent_of_compression} \n")

#Extra Credit Opportunity

user_input = int(input("Enter a number between -127 and 127: "))
def convert(number):
# remove 0b using indexing and add zeros so the number has an 8 bits representation

    binary = bin(abs(number))[2:].zfill(8)

    if number < -127 or number > 127:
        print("Error: Input out of range. Please enter a number between -127 and 127.")
    elif number == 0:
        return "Binary representation: 0"
    elif number > 0:
        return f"Binary representation: {binary}"
    else:
        # we converted into binary and now replace 0 with 1 and 1 with 0
        flipped = "".join("1" if bit == "0" else "0" for bit in binary)
        # convert the string to an integer and add 1
        flipped = int(flipped, 2) + 1
        # convert back to binary, remove 0b and make it 8 bits
        twos_complement = bin(flipped)[2:].zfill(8)
        return f"Two's complement representation: {twos_complement}"
print(convert(user_input))

