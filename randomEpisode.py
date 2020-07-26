import os

import random

p = r'D:\Courses\node.js'

os.chdir(p)

# print(os.listdir(p))

folder_name = random.choice(os.listdir(p))

folder_path = str(os.path.realpath(folder_name))

os.chdir(folder_path)

# print(os.listdir(folder_path))

file_name = random.choice(os.listdir(folder_path))


print("Enjoy !!")

os.startfile(file_name)
