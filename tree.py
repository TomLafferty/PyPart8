import os

def print_file_paths(file_path):
    '''Given a file path, write to a file all of the contents of the directory and child directories below it'''

    # new_file = open(file_path, 'w')
    # for line in new_file:
    #     new_file.write(line)
    contents = os.listdir(file_path)
    for item in contents:
        print(os.path.relpath(item))


example = ('/Users/laffertythomas/dev/PyParts/PyPart8')
print_file_paths(example)



# ./file1.py
# ./file2.py
# ./dir1/file1_in_dir1.txt
# ./dir1/file2_in_dir1.txt
# ./dir3/file1_in_dir3.txt

