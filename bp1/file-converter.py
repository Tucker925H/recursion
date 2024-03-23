import sys
import os
import markdown

command = sys.argv[1]
inputFile = sys.argv[2]
outputFile = sys.argv[3]

with open(inputFile, 'r') as file:
    text = file.read()
    if command == 'markdown':
        html = markdown.markdown(text)
        output_filename = os.path.basename(inputFile)
        if output_filename.lower().endswith('.md'):
            output_filename = output_filename[:-3]
        if not output_filename.lower().endswith('.html'):
            output_filename += ".html"
        print(output_filename)
        output_file_path = os.path.join(outputFile, output_filename)
        with open(output_file_path, 'w') as file:
            file.write(html)
    else : print(command + ': command not found')
