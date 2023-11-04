# Define the TABLE
TABLE = "qwertyuiopasdfghjkl;zxcvbnm,./"
# Create second_keys by converting TABLE to uppercase and prepending '_'
second_keys = '_' + TABLE.upper()
TABLE = TABLE.upper()

# Initialize variables to store data
data_lines = []
extract_data = False
start_flag = False
start_line = "川先質忠螺靠制書看告生鬥反由鬧片牡製史牌物盡毛劃數雖段失特牛"

# Read the data from the file line by line and process it
with open('/dev/shm/raw.txt', 'r', encoding='utf8') as file:
    Lines = file.readlines()
    count = 0
    for line in Lines:
        count += 1
        # print("Line {}: {}".format(count, line.strip()))

        if extract_data:
            if line.strip() == start_line:
                start_flag = True
            if start_flag:
                data_lines.append(line.strip())
            extract_data = False
            continue

        if line.find('BIG5') != -1:
            # Set extract_data to True when 'BIG5' keyword is found
            extract_data = True

    for main_key in TABLE:
        for second_key in second_keys:
            if data_lines:
                data_line = data_lines.pop(0)
                if data_line:
                    print(f"{main_key}{second_key}_ {data_line}")
        print()  # Print an empty line to separate different data entries
