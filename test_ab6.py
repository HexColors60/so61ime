# Initialize the dictionary
ab_dict = {}

# Read data from the file 'testab.txt'
with open('testab.txt', 'r') as file:
    lines = file.readlines()

# Process each line in the file
for line in lines:
    key, value = line.strip().split()  # Split the line into key and value
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
    if key in ab_dict:
        next_number = ab_dict[key][0]  # Get the next_number for the key
    else:
        # Key doesn't exist, start with next_number = 1
        next_number = 1
        ab_dict[key] = {}  # Initialize an empty dictionary for the key

    if now == 0:
        now = next_number
        
    # Swap values between ab_dict[key][now] and ab_dict[key][next_number] if now exists
    if now in ab_dict[key]:
        temp = ab_dict[key][now]
        ab_dict[key][now] = value
        print(f"Debug: {key} {now} => {value} {temp}")
        ab_dict[key][next_number] = temp
    else:
        ab_dict[key][now] = value

    # Increment next_number if it already exists
    while next_number in ab_dict[key]:
        next_number += 1

    # Update the next_number for the key
    ab_dict[key][0] = next_number

# Print the updated ab_dict
for key, values in ab_dict.items():
    # items = sorted(values.items())
    items = values.items()
    for next_number, value in items:
        # if next_number != 0:
        print(f"{key} {next_number} => {value}")

def do_output_file():
    # Optionally, you can save the updated ab_dict to a file for future reference
    with open('updated_ab_dict.txt', 'w') as outfile:
        for key, values in ab_dict.items():
            # items = sorted(values.items())
            items = values.items()
            for next_number, value in items:
            #    if next_number != 0:
                outfile.write(f"{key} {next_number} => {value}\n")


