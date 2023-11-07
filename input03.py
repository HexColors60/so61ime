
# Test script for phrase.
import sys
import termios
import select
import time
import glob
import os

prompt_dict = {}  # Added prompt_dict
table1_dict = {}
tmp_ab_dict = {}

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
        print(f"Debug: {key} {now} => {value} {temp}")
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
    for ab_file in glob.glob(os.path.join(ab_folder, '*.ab')):
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
    
    return ab_dict

def debug_ab(ab_dict):
    for key, value in ab_dict.items():
        print(f'{key} => {value}')
        # time.sleep(1)

# Global variables
ab_folder = "ab"
so61utf8_dict = parse_so61utf8("so61utf8.txt")
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
        key = sys.stdin.read(1)
        print(f"Input Key: {key}")  # Prompt for the key you input

    termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, oldt)

    return key

def show_dict(keys, table):
    keys = keys.upper()
    if keys in table:
        output_prompt = table[keys]
        print("１２３４５６７８９０")
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

def clear_outstr():
    # Define your clear_outstr function if needed
    pass

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
            break

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
                process_input_buffer(input_buffer, output_buffer)
                print(f"Current Input Key: {input_buffer}")
                print(f"Output Buffer: {output_buffer}")
            prompt_buffer = ""
            input_buffer = ""
            # show_dict('', ab_dict)
            show_dict('', prompt_dict)
        elif ord(key) == 127:  # Handle backspace
            if input_buffer:
                input_buffer = input_buffer[:-1]
                output_buffer = output_buffer[:-1]
                prompt_buffer = prompt_buffer[:-1]
        elif key == '`':
            debug_ab(ab_dict)
        else:
            input_buffer += key
            output_buffer += key
            prompt_buffer += key
            # show_dict(prompt_buffer, ab_dict)
            show_dict(prompt_buffer, prompt_dict)

        prompt_keys(input_buffer)  # Call the prompt_keys function for each input key

    termios.tcsetattr(sys.stdin, termios.TCSANOW, oldt)  # Restore the terminal settings

# Call the do_work function to start reading and processing input keys
do_work()
