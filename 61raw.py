import time

# Function to find the start and end positions of the target data in a binary buffer
def find_start_end(buffer, start_hex, end_hex):
    start_pos = buffer.find(bytes.fromhex(start_hex))
    if start_pos == -1:
        return None, None
    end_pos = buffer.find(bytes.fromhex(end_hex), start_pos)
    if end_pos == -1:
        return None, None
    return start_pos, end_pos + len(bytes.fromhex(end_hex))

# Function to split the work buffer into 60-character binary chunks
def split_work_buffer(buffer):
    return [buffer[i:i + 60] for i in range(0, len(buffer), 60)]

# Function to print 30 words per line
# def print_words_per_line(words):
#    for i in range(0, len(words), 30):
#        print(" ".join(words[i:i+30].replace(' ','﹏')))

# def print_words_per_line(text):
#    words = text.split()
#    special_char = '﹏'
#    result = []

#    for word in words:
#        word_with_special_char = word.replace(' ', special_char)
#        result.append(word_with_special_char)

#    lines = [" ".join(result[i:i+30]) for i in range(0, len(result), 30)]
#
#    for line in lines:
#        print(line)
def print_words_per_line(words):
    special_char = '﹏'
    result = []

    for word in words:
        word_with_special_char = word.replace('　', special_char)
        result.append(word_with_special_char)

    lines = ["".join(result[i:i+30]) for i in range(0, len(result), 30)]

    for line in lines:
        print(line)

#  
# Example usage:
# words = ["This", "is", "a", "sample", "list", "of", "words", "that", "you", "want", "to", "split", "into", "lines", "with", "a", "special", "character", "replacing", "spaces", "in", "each", "word."]
# print_words_per_line(words)

# Example usage:
# text = "This is a sample text that you want to split into lines with a special character replacing spaces in each word."
# print_words_per_line(text)

# Read the binary file
with open("_61_0809.ime", "rb") as file:
    binary_data = file.read()

# Define the start and end hex values
start_hex = 'a4a4b77ca6b3aabab9efa457a446ac4fb44ea7daa440acb0a662b0eaa54cad6ea661a548a46aadd3a94da8eca558a4a3b36fa5cea8d3a448aec9'
end_hex = '3030303030303030303030'

# Find start and end positions
start_pos, end_pos = find_start_end(binary_data, start_hex, end_hex)

# Check if the data was found
if start_pos is not None and end_pos is not None:
    # Extract the data between start and end positions
    extracted_data = binary_data[start_pos:end_pos]

    # Remove null characters from the extracted data
    extracted_data = extracted_data.replace(b'\x00', b'')

    # Split the extracted data into 60-character chunks
    work_buffer = split_work_buffer(extracted_data)

    # Display the size of the work buffer
    print(f"Size of work buffer: {len(work_buffer)}")

    # Convert each chunk from Big5 or ASCII to UTF-8 and display 30 words per line
    for chunk in work_buffer:
        hex_chunk = chunk.hex()
        utf8_text = chunk.decode('big5', errors='ignore')
        
        if all(c.isascii() or c.isspace() for c in utf8_text):
            print("ascii")
        else:
            print("BIG5")
        
        # Split the text into words
        # words = utf8_text.split()
        words = utf8_text
        
        print_words_per_line(words)

        print(f"Hex: {hex_chunk}")
        print(f"Start Pos: {start_pos}, End Pos: {end_pos}")
        # time.sleep(1)
else:
    print("Start and end hex values not found in the binary data.")
