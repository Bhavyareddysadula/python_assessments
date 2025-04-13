""" Question-6:
#MaxFile class 
from pkg.file import File 
fs = File(".")
fs.getMaxSizeFile(2) # gives two max file names 
fs.getLatestFiles(datetime.date(2018,2,1))
#Returns list of files after 1st Feb 2018 """

import os
import datetime

class File:
    def __init__(self,Directory):
        self.Directory = Directory
        
    def get_max_size_file(self, n):
        file_sizes = []
        for root, dir, files in os.walk(self.Directory):
            for file in files:
                path = os.path.join(root,file)
                size = os.path.getsize(path)
                file_sizes.append((file,size))
        
        file_sizes.sort(key = lambda x : x[1], reverse = True)
        print("Top", n, "largest files:")
        for i in range(min(n, len(file_sizes))):
            print(file_sizes[i][0])
            
        return ""
        
    def get_large_file(self, input_date):
        print("Files after", input_date, "are:")
        for root, dir, files in os.walk(self.Directory):
            for file in files:
                path = os.path.join(root,file)
                created = datetime.date.fromtimestamp(os.path.getctime(path))
                if created > input_date:
                    print(file)
        return ""
        
        
fs = File(r"C:\Users\Bhavya\handson")
fs.get_max_size_file(2) 
fs.get_large_file(datetime.date(2025,4,8)) 
                
