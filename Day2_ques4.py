""" Question-4:
Recursively go below a dir and based on filter, dump those files in to  single file 
(work with only text file)"""


import os

def files(directory):
    txt_files = []
    for root, dir, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root,file)
                txt_files.append(path)
    return txt_files
        
def merge_files(file_list, output_path):
    with open(output_path,'w') as output:
        for file in file_list:
            with open(file, 'r') as f:
                output.write(f.read())
                output.write('\n')
 
directory = r"C:\Users\Bhavya\handson" 
file_list = files(directory)
output_file = os.path.join(directory , "merged.txt" )
print(merge_files(file_list, output_file))
    
