import sys

def modify_html_links(input_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            html_content = input_file.read()

        modified_html_content = html_content.replace('?c=', '.c.')

        output_filename = input_filename + '.new.htm'

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_html_content)

        print(f'HTML file modified and saved as {output_filename}')

        try:
            # Rename the old file to filename.old.htm
            import os
            os.rename(input_filename, input_filename + '.old.htm')
            # Rename the new file to the original filename
            os.rename(output_filename, input_filename)
        except Exception as e:
            print(f'Error renaming files: ')

    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python modify_html_links.py input_filename.html')
        sys.exit(1)

    input_filename = sys.argv[1]

    modify_html_links(input_filename)
