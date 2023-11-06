import re
import sys
import os

# Check if the command line argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py input_file.html")
    sys.exit(1)

input_file_name = sys.argv[1]
output_file_name = input_file_name + ".new.htm"

# Define a regular expression pattern to match the URLs
url_pattern = r'<a href="/web/\d+/(http://[^"]+)">([^<]+)</a>'

# Function to extract the desired information from the URL
def extract_filename(match):
    url = match.group(1)
    return re.sub(r'/', '-', url.split('/')[-1]) + ".htm"

# Read the input file and create the output file
with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
    for line in input_file:
        matches = re.finditer(url_pattern, line)
        for match in matches:
            new_link = extract_filename(match)
            line = line.replace(match.group(0), f'<a href="{new_link}">{match.group(2)}</a>')
        output_file.write(line)

print(f"File '{output_file_name}' created with updated links.")

# Rename the old file to xx.old.htm
if os.path.exists(input_file_name):
    old_file_name = input_file_name + ".old.htm"
    os.rename(input_file_name, old_file_name)
    print(f"Old file '{input_file_name}' renamed to '{old_file_name}'.")

    # Rename the new file to xx.htm
    os.rename(output_file_name, input_file_name)
    print(f"New file '{output_file_name}' renamed to '{input_file_name}'.")
else:
    print(f"Error: Input file '{input_file_name}' not found.")
