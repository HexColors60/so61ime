import sys
import termios
import select

# Initialize the TABLE
TABLE = "qwertyuiopasdfghjkl;zxcvbnm,./"
TABLE = TABLE.upper()

# Read the data from the file and create two dictionaries to map TABLE keys to characters
with open("so61utf8.txt", "r", encoding="utf-8") as file:
    data = file.read()

lines = data.split("\n")
table_dict_1 = {}
table_dict_2 = {}

for line in lines:
    if line:
        key, value = line[:3], line[3:]
        key = key.strip()
        value = value.strip()
        for i, char in enumerate(value):
            replaced_key = key.replace('_', TABLE[i % len(TABLE)], 1)
            table_dict_1[replaced_key] = char

        replaced_key = key.replace('_', '')
        table_dict_2[replaced_key] = value

prompt_dict = {}  # Added prompt_dict

for line in lines:
    if line:
        key, value = line[:3], line[3:]
        key = key.strip()
        value = value.strip()
        replaced_key = key.replace('_', '')
        prompt_dict[replaced_key] = value  # Populate prompt_dict as well

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

def old_show_dict(keys, table):
    keys = keys.upper()
    if keys in table:
        output_prompt = table[keys]
        print(f"Output Prompt: {output_prompt}")

def show_dict(keys, table):
    keys = keys.upper()
    if keys in table:
        output_prompt = table[keys]
        print("１２３４５６７８９０")
#        words = output_prompt.split()
#        for i in range(0, len(words), 10):
#            line = "".join(words[i:i+10])
#            print(line + "\n")
        for i in range(0, len(output_prompt), 10):
            print(output_prompt[i:i+10])


def prompt_keys(input_buffer):
    # Display all keys in the input buffer, with spaces shown as "_"
    prompt_buffer = input_buffer.replace(' ', '_')
    print(f"Prompt Keys: {prompt_buffer}")

def process_input_buffer(input_buffer, output_buffer, table):
    # Split input_buffer into 3-key pairs and perform the TABLE search
    output_table_keys = ""

    for i in range(0, len(input_buffer), 3):
        current_key = input_buffer[i:i+3]
        while len(current_key) < 3:
            current_key += "_"
        current_key = current_key.upper()
        if current_key in table:
            output_table_keys += table[current_key]
    output_buffer = output_table_keys

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

    show_dict('', prompt_dict)
    while True:
        key = read_key()

        if key is None:
            break

        if ord(key) == 10:  # Enter key (newline)
            process_input_buffer(input_buffer, output_buffer, table_dict_1)
            clear_outstr()
            input_buffer = ""
            output_buffer = ""
            prompt_buffer = ""
        elif key == ' ':
            input_buffer += '_'
            for i in range(0, len(input_buffer), 3):
                current_key = input_buffer[i:i+3]
                while len(current_key) < 3:
                    current_key += "_"
                    input_buffer += '_'
            process_input_buffer(input_buffer, output_buffer, table_dict_1)
            print(f"Current Input Key: {input_buffer}")
            print(f"Output Buffer: {output_buffer}")
            prompt_buffer = ""
        elif ord(key) == 127:  # Handle backspace
            if input_buffer:
                input_buffer = input_buffer[:-1]
                output_buffer = output_buffer[:-1]
                prompt_buffer = prompt_buffer[:-1]
        else:
            input_buffer += key
            output_buffer += key
            prompt_buffer += key
            show_dict(prompt_buffer, prompt_dict)

        prompt_keys(input_buffer)  # Call the prompt_keys function for each input key

    termios.tcsetattr(sys.stdin, termios.TCSANOW, oldt)  # Restore the terminal settings

# Call the do_work function to start reading and processing input keys
do_work()

