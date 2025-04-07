import os
def large_file(directory):
        max_size = 0
        max_file_name = " "
        for root, dir, files in os.walk(directory):
            for file in files:
                path = os.path.join(root,file)
                size = os.path.getsize(path)
                if size > max_size:
                    max_size = size
                    max_file_size = file
        return max_file_size
print(large_file(r"C:\Users\Bhavya\handson")) 
