# Define the TABLE and its uppercase version
TABLE = "qwertyuiopasdfghjkl;zxcvbnm,./_"
TABLE = TABLE.upper()
TABLE2 = "ＱＷＥＲＴＹＵＩＯＰＡＳＤＦＧＨＪＫＬ；ＺＸＣＶＢＮＭ，．／"
TABLE3 = "１２３４５６７８９０一二三四五六七八九十竹廾廿火乂手木人尸／"
TABLE4 = "中乙貝心彎女刀日月口一二三四五六土八九十竹草散火插手木人耳空"

green_positions = [3, 6, 13, 16, 23, 26]  # Updated to start from 1
color_table = "000000000000000000000000000000"

def apply_colors(word_table, color_table, green_positions):
    result = []
    for i in range(0, len(word_table), 10):
        word_line = word_table[i:i+10]
        color_line = color_table[i:i+10]
        colored_line = ""
        for j, char in enumerate(word_line):
            color_code = int(color_line[j])
            if j in green_positions and color_code == 0:
                colored_line += "\033[32m" + char + "\033[0m"
            elif color_code == 0:
                colored_line += char
            elif color_code == 1:
                colored_line += "\033[31m" + char + "\033[0m"
            elif color_code == 2:
                colored_line += "\033[33m" + char + "\033[0m"
            elif color_code == 3:
                colored_line += "\033[31m" + char + "\033[0m"
            elif color_code == 4:
                colored_line += "\033[34m" + char + "\033[0m"
            elif color_code == 5:
                colored_line += "\033[36m" + char + "\033[0m"
        result.append(colored_line)
    return result

# Read the data from the file
with open("so61utf8.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Split the data into lines
lines = data.split("\n")

# Create a dictionary to map TABLE keys to characters
table_dict = {}
raw_dict = {}
for line in lines:
    if line:
        key, value = line[:3], line[3:]
        key = key.strip()
        value = value.strip()
        key2 = key[:2]
        raw_dict[key2] = value
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
    input_str = input_str.strip()
except EOFError:
    print("EOF reached. Exiting.")
    exit()

# Process the input string and replace characters with TABLE keys
output_str = ""
for char in input_str:
    if char in table_dict:
        # output_str += char + " " + " ".join(table_dict[char]) + "\n"
        output_str += char + " " + " ".join(table_dict[char])
        if char in table_dict and table_dict[char]:  # Check if char is in table_dict and the list is not empty
            str2 = apply_colors(TABLE2, color_table, green_positions)
            str3 = "___ " + "".join(str2)
            print(str3)
            str2 = apply_colors(TABLE3, color_table, green_positions)
            str3 = "___ " + "".join(str2)
            print(str3)
            str2 = apply_colors(TABLE4, color_table, green_positions)
            str3 = "___ " + "".join(str2)
            print(str3)
        
            key3 = table_dict[char][0][0]
            # print(f"key3 is {key3}")
            for i in TABLE:
                str2 = raw_dict[key3 + i]
                str2 = apply_colors(str2, color_table, green_positions)
                # print(f"{key3}{i}_ {str2}")
                str3 = key3 + i + "_ " + "".join(str2)
                print(str3)
        else:
            # Handle the case where char is not in table_dict or the list is empty
            key3 = None
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



