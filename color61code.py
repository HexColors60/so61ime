# Define the TABLE and its uppercase version
TABLE = "qwertyuiopasdfghjkl;zxcvbnm,./_"
TABLE = TABLE.upper()
TABLE2 = "ＱＷＥＲＴＹＵＩＯＰＡＳＤＦＧＨＪＫＬ；ＺＸＣＶＢＮＭ，．／"
TABLE3 = "１２３４５６７８９０一二三四五六七八九十竹廾廿火乂手木人尸／"
TABLE4 = "中乙貝心彎女刀日月口一二三四五六土八九十竹草散火插手木人耳空"

# Read the data from the file
with open("so61utf8.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Split the data into lines
lines = data.split("\n")

# Create a dictionary to map TABLE keys to characters
table_dict = {}
for line in lines:
    if line:
        key, value = line[:3], line[3:]
        key = key.strip()
        value = value.strip()
        for i, char in enumerate(value):
            # Use modulo to ensure cyclic access to TABLE characters
            replaced_key = key.replace('_', TABLE[i % len(TABLE)], 1)
            if char in table_dict:
                table_dict[char].append(replaced_key)
            else:
                table_dict[char] = [replaced_key]

# Read the input string from stdin
try:
    input_str = input("Enter a string: ")
except EOFError:
    print("EOF reached. Exiting.")
    exit()

# Process the input string and replace characters with TABLE keys
output_str = ""
for char in input_str:
    if char in table_dict:
        output_str += char + " " + " ".join(table_dict[char]) + "\n"
    else:
        output_str += char + " (No TABLE key)\n"

# Print the output
print(output_str)

# Define the TABLE and its uppercase version
# TABLE = "qwertyuiopasdfghjkl;zxcvbnm,./_"
# TABLE = TABLE.upper()
TABLE2 = "ＱＷＥＲＴＹＵＩＯＰＡＳＤＦＧＨＪＫＬ；ＺＸＣＶＢＮＭ，．／﹏"
TABLE3 = "１２３４５６７８９０一二三四五六七八九十竹廾廿火乂手木人尸／﹏"
TABLE4 = "中乙貝心彎女刀日月口一二三四五六土八九十竹草散火插手木人耳空﹏"

def replace_chars_with_tables(input_str):
    # Initialize the output string
    output_str = ""
    str3 = ""
    str4 = ""

    # Iterate over each character in the input_str
    for char in input_str:
        # Find the index of the character in TABLE
        index = TABLE.find(char)
        
        if index != -1:
            # Replace the character with the corresponding character from TABLE2, TABLE3, or TABLE4
            output_str += " " + TABLE2[index] 
            str3 += " " + TABLE3[index] 
            str4 += " " + TABLE4[index]
        else:
            # If the character is not in TABLE, keep it as is
            output_str += char
            str3 += char
            str4 += char    
    return output_str, str3, str4

# Test the function with your example
# example = "輸 ;U_"
output_str2, out3, out4 = replace_chars_with_tables(output_str)
print(output_str2)
print(out3)
print(out4)



