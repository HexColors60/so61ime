
# test_color5.py
# The sixone root characters with color
# Define the word table
# word_table = "川先質忠螺靠制書看告生鬥反由鬧片牡製史牌物盡毛劃數雖段失特牛"

XTABLE2 = "ＱＷＥＲＴＹＵＩＯＰＡＳＤＦＧＨＪＫＬ；ＺＸＣＶＢＮＭ，．／"
XTABLE3 = "１２３４５６７８９０一二三四五六七八九十竹廾廿火乂手木人尸／"
XTABLE4 = "中乙貝心彎女刀日月口一二三四五六土八九十竹草散火插手木人耳空"

# Define the color table
# color_table = "030000003003000000300003003000"
# xcolor_table = "000000000000000000000000000000"
xcolor_table = "0000000000000000000000000000000000000000"
xcolor_table6 = "0000000000001000010001000111000000000000"

# Define the positions where the default green color should be applied
xgreen_positions = [3, 6, 13, 16, 23, 26]  # Updated to start from 1
# xgreen_positions6 = [3, 6, 13, 16, 23, 26]  # Updated to start from 1
xgreen_positions6 = [2, 6, 7, 8, 11, 15]  # Updated to start from 1


# Color Code 0: No color (default)
# Color Code 1: Red text
# Color Code 2: Yellow text
# Color Code 3: Red text (again, it's the same as Color Code 1 in your provided code)
# Color Code 4: Blue text
# Color Code 5: Cyan text

# Function to apply colors to the word table
def xapply_colors(word_table, color_table, green_positions):
    result = []
    for i in range(0, len(word_table), 10):
        word_line = word_table[i:i+10]
        color_line = color_table[i:i+10]
        colored_line = ""
        for j, char in enumerate(word_line):
            color_code = int(color_line[j])
            if (j + i) in green_positions and color_code == 0:
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

# Display the colored word table
def xwork(xword_table):
    colored_lines = xapply_colors(xword_table, xcolor_table, xgreen_positions)
    for line in colored_lines[:3]:  # Print the first 3 lines
        print(line)
    print(f"")  

def xwork6(xword_table):
    colored_lines = xapply_colors(xword_table, xcolor_table6, xgreen_positions6)
    for line in colored_lines[:3]:  # Print the first 3 lines
        print(line)
    print(f"")  
    
def show_roots():
    print(f"https://hexcolors60.github.io/so61ime/ch0202.php.htm")
    xwork(TABLE2)
    xwork(TABLE3)
    xwork(TABLE4)
    xwork6(TABLE3) # Six code
    print("二為卄的代碼、３為三的代碼、六為手的代碼、")
    print("７為木的代碼、８為八的代碼、９為人的代碼\n")
    
# Test script for phrase.
import sys
import termios
import select
import time
import glob
import os

# str61code.py 
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
output_str = ""

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
# try:
#     input_str = input("Enter a string: ")
# except EOFError:
#    print("EOF reached. Exiting.")
#    exit()

# pip install opencc-python-reimplemented
import opencc

# converter = opencc.OpenCC('s2t.json')

# Process the input string and replace characters with TABLE keys
def show_str(input_str):
    output_str = ""
    for char in input_str:
        if char in table_dict:
            output_str += char + " " + " ".join(table_dict[char]) # + "\n"
        else:
            # output_str += char + " (No TABLE key)\n"
            converter = opencc.OpenCC('s2t')
            char2 = converter.convert(char)
            if char2 in table_dict:
                output_str += char2 + " " + " ".join(table_dict[char2])
            else:
                output_str += char + " (No TABLE key)\n"
                 
    # Print the output
    print(output_str)
    return output_str
    
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
def show_code(input_str):
    output_str = show_str(input_str)
    output_str2, out3, out4 = replace_chars_with_tables(output_str)
    print(output_str2)
    print(out3)
    print(out4)
    return


prompt_dict = {}  # Added prompt_dict
table1_dict = {}
tmp_ab_dict = {}
color_dict = {}

def parse_so61utf8(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')

    TABLE = "qwertyuiopasdfghjkl;zxcvbnm,./_"
    TABLE = TABLE.upper()

    # Create a dictionary to map TABLE keys to characters
    table_dict = {}
    for line in lines:
        if line: # and not line.startswith("___"):
            key, value = line[:3], line[3:]
            key = key.strip()
            value = value.strip()
            replaced_key = key.replace('_', '')
            prompt_dict[replaced_key] = value  # Populate prompt_dict as well
            for i, char in enumerate(value):
                # Use modulo to ensure cyclic access to TABLE characters
                replaced_key = key.replace('_', TABLE[i % len(TABLE)], 1)
                table1_dict[replaced_key] = char
                if char in table_dict:
                    table_dict[char].append(replaced_key)
                else:
                    table_dict[char] = [replaced_key]

    return table_dict

def parse_color(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')

    TABLE = "qwertyuiopasdfghjkl;zxcvbnm,./_"
    TABLE = TABLE.upper()

    # Create a dictionary to map TABLE keys to characters
    table_dict = {}
    for line in lines:
        if line: # and not line.startswith("___"):
            key, value = line[:3], line[3:]
            key = key.strip()
            value = value.strip()
            replaced_key = key.replace('_', '')
            table_dict[replaced_key] = value  # Populate prompt_dict as well
    return table_dict

def build_ab_dict_tmp(key, value):
    # my_dict = {key: value}
    # return my_dict
    # key, value = line.strip().split()  # Split the line into key and value
    # not # now = key  # Store the numeric part in 'now'
    # Extract the numeric part from the key and store it in 'now'
    tmp, now = "", 0
    for char in key:
        if char.isdigit():
            now = now * 10 + int(char)
        else:
            tmp += char

    key = tmp  # Update the key to exclude the numeric part
    
    # Check if the key already exists in the dictionary
    if key in tmp_ab_dict:
        next_number = tmp_ab_dict[key][0]  # Get the next_number for the key
    else:
        # Key doesn't exist, start with next_number = 1
        next_number = 1
        tmp_ab_dict[key] = {}  # Initialize an empty dictionary for the key

    if now == 0:
        now = next_number
        
    # Swap values between tmp_ab_dict[key][now] and tmp_ab_dict[key][next_number] if now exists
    if now in tmp_ab_dict[key]:
        temp = tmp_ab_dict[key][now]
        tmp_ab_dict[key][now] = value
        # print(f"Debug: {key} {now} => {value} {temp}")
        tmp_ab_dict[key][next_number] = temp
    else:
        tmp_ab_dict[key][now] = value

    # Increment next_number if it already exists
    while next_number in tmp_ab_dict[key]:
        next_number += 1

    # Update the next_number for the key
    tmp_ab_dict[key][0] = next_number

def build_ab_dict(ab_folder, table_dict):
    ab_dict = {}
    # for ab_file in glob.glob(os.path.join(ab_folder, '*.ab')):
    file_list = sorted(glob.glob(os.path.join(ab_folder, '*.ab')))
    for ab_file in file_list:
        with open(ab_file, 'r', encoding='utf-8') as file:
            lines = file.read().split('\n')

        ab_entry = ''
        for line in lines:
            if line:
                key, data = line.split(None, 1)
                if key == '_':
                    key = ''
                    for char in data:
                        if char in table_dict:
                            key += table_dict[char][0][0]
                    ab_entry = key.strip()
                    data = data.strip()
                    build_ab_dict_tmp(ab_entry, data)
                    # ab_dict[ab_entry] = data
                else:
                    build_ab_dict_tmp(key.upper(), data)
    
    return ab_dict

def debug_ab(ab_dict):
    for key, value in ab_dict.items():
        print(f'{key} => {value}')
        # time.sleep(1)

# Global variables
ab_folder = "ab"
so61utf8_dict = parse_so61utf8("so61utf8.txt")
color_dict = parse_color("so61color.txt")
ab_dict = build_ab_dict(ab_folder, so61utf8_dict)
ab_dict = tmp_ab_dict

tmp_ab_buffer = ""

def lookup_ab_dict(key, next_number):
    # Check if the key exists in ab_dict
    tmp, now = "", 0
    for char in key:
        if char.isdigit():
            now = now * 10 + int(char)
        else:
            tmp += char

    key = tmp  # Update the key to exclude the numeric part
    if now != 0:
        next_number = now
    
    if next_number == 0:
        tmp_ab_buffer = ""
        return False
    if key in ab_dict:
        if next_number in ab_dict[key]:
            # return ab_dict[key][next_number]
            print(f"ab_dict {key} {next_number} {ab_dict[key][next_number]}")
            tmp_ab_buffer = ab_dict[key][next_number]
            # return True
            return tmp_ab_buffer
        else:
            # return f"Next number {next_number} not found for key {key}"
            return False
    else:
        # return f"Key {key} not found in ab_dict"
        return False

def read_key():
    key = None
    oldt = termios.tcgetattr(sys.stdin)
    newt = termios.tcgetattr(sys.stdin)
    newt[3] = newt[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(sys.stdin, termios.TCSANOW, newt)

    rlist, _, _ = select.select([sys.stdin], [], [], 10)

    if rlist:
        # key2 = ord(key)
        # print(f"Key {key2}")
        key = sys.stdin.read(1)
        print(f"Input Key: {key}")  # Prompt for the key you input

    termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, oldt)

    return key


# Define the positions where the default green color should be applied
green_positions = [3, 6, 13, 16, 23, 26]  # Updated to start from 1

# Function to apply colors to the word table
def apply_colors(word_table, color_table, green_positions):
    result = []
    for i in range(0, len(word_table), 10):
        word_line = word_table[i:i+10]
        color_line = color_table[i:i+10]
        colored_line = ""
        for j, char in enumerate(word_line):
            color_code = int(color_line[j])
            if (j+i) in green_positions and color_code == 0:
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
    # return result

    # Display the colored word table
    # colored_lines = apply_colors(word_table, color_table, green_positions)
    # for line in colored_lines[:3]:  # Print the first 3 lines
    #    print(line)
    for line in result[:3]:  # Print the first 3 lines
       print(line)

def show_dict(keys, table):
    keys = keys.upper()
    if keys in table:
        output_prompt = table[keys]
        now_keys = keys
        while len(now_keys) < 3:
            now_keys += "_"
        if now_keys in table1_dict:
            now_char = table1_dict[now_keys]
        else:
            now_char = ""
        print(f"六一 半 {now_char}")
        if keys in table:
            word_table = table[keys]
        else:
            word_table = ""
        if keys in color_dict:
            color_table = color_dict[keys]
        else:
            color_table = ""
        print("１２３４５６７８９０")
        if len(word_table) >= 30 and len(color_table) >= 30:
            apply_colors(word_table, color_table, green_positions)
        else:
            for i in range(0, len(output_prompt), 10):
                print(output_prompt[i:i+10])


def prompt_keys(input_buffer):
    # Display all keys in the input buffer, with spaces shown as "_"
    prompt_buffer = input_buffer.replace(' ', '_')
    print(f"Prompt Keys: {prompt_buffer}")

import re

def extract_ab_and_number(input_buffer):
    # Define regular expression patterns for the non-number and number parts
    non_number_pattern = r'^\D+'
    number_pattern = r'\d+'
    
    # Use re.search to find the first match in the input_buffer for each pattern
    non_number_match = re.search(non_number_pattern, input_buffer)
    number_match = re.search(number_pattern, input_buffer)
    
    # Extract ab_buffer and number, or set number to 0 if no match is found
    ab_buffer = non_number_match.group(0) if non_number_match else ''
    number = int(number_match.group(0)) if number_match else 0
    
    return ab_buffer, number

def process_input_buffer(input_buffer, output_buffer):
    # Split input_buffer into 3-key pairs and perform the TABLE search
    output_table_keys = ""

    # ab_buffer = input_buffer.replace('_', '').upper()
    # if ab_buffer in ab_dict:
    #     output_table_keys += ab_dict[ab_buffer]
    # else:    
    offset = 0
    for i in range(0, len(input_buffer), 3):
        ab_buffer, number = extract_ab_and_number(input_buffer[i + offset:].replace('_', '').upper())
        # ab_buffer = input_buffer.replace('_', '').upper()
        # if ab_buffer in ab_dict:
        tmp = lookup_ab_dict(ab_buffer, number)
        if tmp:
            # output_table_keys += tmp_ab_buffer # Not ab_dict[ab_buffer]
            output_table_keys += tmp
            print(f"Output String: {output_table_keys}")
            # input_buffer = ""
            if number:
               offset += len(ab_buffer) + len(str(number))
            else:
               offset += len(ab_buffer)

        # if number:
        #    tmp_key = input_buffer[i:].replace(ab_buffer + str(number), "");
        # else:
        #    tmp_key = input_buffer[i:].replace(ab_buffer, "");
        
        current_key = input_buffer[i + offset:i+offset+3]
        # tmp_key = xxx
        while len(current_key) < 3:
            current_key += "_"
        current_key = current_key.upper()
        if current_key in table1_dict:
            output_table_keys += table1_dict[current_key]
            # output_table_keys += so61utf8_dict[current_key]

    output_buffer += output_table_keys

    print(f"Input Buffer: {input_buffer.replace(' ', '_')}")
    print(f"Output Buffer: {output_buffer.replace(' ', '_')}")
    print(f"Current Input Key: {input_buffer}")
    print(f"Output String: {output_table_keys}")
    return output_table_keys
    
def clear_outstr():
    # Define your clear_outstr function if needed
    pass

def is_utf8_character(char):
    try:
        char.encode('utf-8')
        return True
    except UnicodeEncodeError:
        return False


def do_work():
    input_buffer = ""
    output_buffer = ""
    prompt_buffer = ""  # Added prompt_buffer
    oldt = termios.tcgetattr(sys.stdin)  # Capture the terminal settings

    # show_dict('', ab_dict)
    show_dict('', prompt_dict)    
    while True:
        key = read_key()

        if key is None:
            # break
            continue

        if ord(key) == 10:  # Enter key (newline)
            process_input_buffer(input_buffer, output_buffer)
            clear_outstr()
            input_buffer = ""
            output_buffer = ""
            prompt_buffer = ""
            # show_dict('', ab_dict)
            show_dict('', prompt_dict)
        elif key == ' ':
            # ab_buffer = input_buffer.replace('_', '').upper()
            # if ab_buffer in ab_dict:
            # if lookup_ab_dict(ab_buffer, 0):
            #    output_table_keys = tmp_ab_buffer # Not ab_dict[ab_buffer]
            #    print(f"Output String: {output_table_keys}")
            #    # input_buffer = ""
            # else:    
            if True:
                input_buffer += '_'
                for i in range(0, len(input_buffer), 3):
                    current_key = input_buffer[i:i+3]
                    while len(current_key) < 3:
                        current_key += "_"
                        input_buffer += '_'
                output_buffer += process_input_buffer(input_buffer, output_buffer)
                print(f"Current Input Key: {input_buffer}")
                print(f"Output Buffer: {output_buffer}")
            prompt_buffer = ""
            input_buffer = ""
            # show_dict('', ab_dict)
            show_dict('', prompt_dict)
        elif ord(key) == 127:  # Handle backspace
            if input_buffer:
                input_buffer = input_buffer[:-1]
                # output_buffer = output_buffer[:-1]
                prompt_buffer = prompt_buffer[:-1]
        elif key == '=':
            show_roots()
        elif key == '-':
            if output_buffer:
                last_character = output_buffer[-1]
                show_code(last_character)
            else:
                print(f"The input buffer is empty. {input_buffer} ")
        elif key == '`':
            debug_ab(ab_dict)
        # elif key == 0x4:
        #    break
        else:
            if ord(key) > 127 and is_utf8_character(key):
                show_code(key)
            else:
                input_buffer += key
                # output_buffer += key
                prompt_buffer += key
                # show_dict(prompt_buffer, ab_dict)
                show_dict(prompt_buffer, prompt_dict)

        prompt_keys(input_buffer)  # Call the prompt_keys function for each input key

    termios.tcsetattr(sys.stdin, termios.TCSANOW, oldt)  # Restore the terminal settings

# def show_table_dict():
#    for key, values in table_dict.items():
#        print(f"{key}: {values}")

def show_table_dict():
    for word, keys in table_dict.items():
        if word != "﹏":  # Skip the word "﹏"
            for key in keys:
                # color_code = color_dict.get(key, "0")  # Get the color code from color_dict, default to "0"
                color_code = "0"
                # key2 = key.replace('_', '')  
                key2 = key[0:2]
                if key2 in color_dict:
                    color_char = key[2:3]
                    color_index = TABLE.find(color_char)
                    color_table = color_dict[key2]
                    color_code = color_table[color_index:color_index+1]
                else:
                    color_table = ""
                    color_code =  "0"
                # print(f"{color_table} ")
                # color_code = "0"
                # Check if color_code is not a digit, set it to "0"
                if not color_code.isdigit():
                    color_code = "0"
                key = key.lower()
                print(f"{word} {color_code} {key}")

# Call the function to display the contents of table_dict
show_table_dict()

# Call the do_work function to start reading and processing input keys
# do_work()
