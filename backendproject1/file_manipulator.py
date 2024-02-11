import sys
import os

file = open('./test2.txt', mode='w')
file.write('hello')
file.close()

class Command:
    def __init__(self):
        self.c_name = ""
        self.inputpath = ""

    def set(self, c_name, inputpath):
        self.c_name = c_name
        self.inputpath = inputpath


    def reverse(self, outputpath):
        with open(self.inputpath, mode="r") as f:
            content = f.read()

        content_no_newlines = content.replace('\n', '').replace('\r', '')

        reversed_content = content_no_newlines[::-1]

        output_filename = os.path.basename(reversed_content)
        if not output_filename.lower().endswith('.txt'):
            output_filename += ".txt"

        output_file_path = os.path.join(outputpath, output_filename)
        with open(output_file_path, mode="x") as f:
            f.write('')

    def copy(self, outputpath):
        with open(self.inputpath, "r") as input_file:
            content = input_file.read()

        output_filename = os.path.basename(self.inputpath)
        if not output_filename.lower().endswith('.txt'):
            output_filename += ".txt"
        output_file_path = os.path.join(outputpath, output_filename)
        with open(output_file_path, "x") as output_file:
            output_file.write(content)
    
    def duplicate_contents(self, n):
        with open(self.inputpath, mode='r') as f:
            content = f.read()
        with open(self.inputpath, mode="a") as f:
            for i in range(int(n)):
                f.write(content)
    
    def replace_string(self, r_string, newstring):
        with open(self.inputpath, mode='r') as f:
            content = f.read()
            content = content.replace(r_string, newstring)
        with open(self.inputpath, mode="w") as f:
            f.write(content)

command = Command()
command.set(sys.argv[1], sys.argv[2])

if command.c_name == "reverse":
    command.reverse(sys.argv[3])
elif command.c_name == "copy":
    command.copy(sys.argv[3])
elif command.c_name == "duplicate-contents":
    command.duplicate_contents(sys.argv[3])
elif command.c_name == "replace-string":
    command.replace_string(sys.argv[3], sys.argv[4])
else :
    print(sys.argv[1] + ': command not found')