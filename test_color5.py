
# The sixone root characters with color
# Define the word table
# word_table = "川先質忠螺靠制書看告生鬥反由鬧片牡製史牌物盡毛劃數雖段失特牛"

TABLE2 = "ＱＷＥＲＴＹＵＩＯＰＡＳＤＦＧＨＪＫＬ；ＺＸＣＶＢＮＭ，．／"
TABLE3 = "１２３４５６７８９０一二三四五六七八九十竹廾廿火乂手木人尸／"
TABLE4 = "中乙貝心彎女刀日月口一二三四五六土八九十竹草散火插手木人耳空"

# Define the color table
# color_table = "030000003003000000300003003000"
color_table = "000000000000000000000000000000"

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

# Display the colored word table
def work(word_table):
    colored_lines = apply_colors(word_table, color_table, green_positions)
    for line in colored_lines[:3]:  # Print the first 3 lines
        print(line)
    print(f"")        
print(f"https://hexcolors60.github.io/so61ime/ch0202.php.htm")
work(TABLE2)
work(TABLE3)
work(TABLE4)

