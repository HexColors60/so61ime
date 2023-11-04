import time
import glob
import os

def parse_so61utf8(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    
    TABLE = "qwertyuiopasdfghjkl;zxcvbnm,./_"
    TABLE = TABLE.upper()
    
    # Create a dictionary to map TABLE keys to characters
    table_dict = {}
    for line in lines:
        if line and not line.startswith("___"):
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
    
    return table_dict

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
                ab_dict[ab_entry] = data
    return ab_dict

def debug_ab(ab_dict):
    for key, value in ab_dict.items():
        print(f'{key} => {value}')
        time.sleep(1)

if __name__ == '__main__':
    ab_folder = "ab"
    so61utf8_dict = parse_so61utf8("so61utf8.txt")
    ab_dict = build_ab_dict(ab_folder, so61utf8_dict)
    debug_ab(ab_dict)
