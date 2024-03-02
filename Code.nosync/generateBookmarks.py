#!/usr/bin/python3

import os
import plistlib
import html

# Define the directory where the .webloc files are located
webloc_directory = '..'

# Define the output file
output_file = '../ Resources - Bookmarks.2.html'

# Start the bookmarks HTML content
bookmarks_html = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
'''

# Function to parse .webloc files and extract URLs
def parse_webloc(file_path):  
    try:
        with open(file_path, 'rb') as fp:  
            plist = plistlib.load(fp)  
        return plist.get('URL')
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

# Function to convert folder path to title
def path_to_title(path):
    return path.split('/')[-1].replace('.webloc', '').replace(' - ', ' ').replace('_', ' ')

# Recursive function to process folders and .webloc files
def process_directory(path, depth=1):
    content = ''
    indent = '    ' * depth
    for item in sorted(os.listdir(path)):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            title = path_to_title(item)
            content += f'{indent}<DT><H3>{html.escape(title)}</H3>\n{indent}<DL><p>\n'
            content += process_directory(full_path, depth + 1)
            content += f'{indent}</DL><p>\n'
        elif item.endswith('.webloc'):
            url = parse_webloc(full_path)
            title = path_to_title(item)
            content += f'{indent}<DT><A HREF="{url}">{html.escape(title)}</A>\n'
    return content

# Process the webloc_directory and append to bookmarks_html
bookmarks_html += process_directory(webloc_directory)

# Close the bookmarks HTML content
bookmarks_html += '</DL><p>\n'

# Write the bookmarks HTML content to the output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(bookmarks_html)

print(f'Bookmarks have been exported to {output_file}')
