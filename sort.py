#!/bin/python3 

import os 
import time

photo_path = "/home/ewaat/Pictures/4K"
contents = os.listdir(photo_path)
no_photos = len(contents)
no_photos = no_photos - 7
count = 0
while count <= no_photos:
	file_path = photo_path + '/' + contents[count]
	exif_file = os.system(f'exiftool {file_path} | grep "File Size" >> file_sizes')
	count = count + 1

with open("file_sizes", 'r') as f:
	file_sizes = f.read()
	file_sizes = file_sizes.split('\n')

file_sizes_len = len(file_sizes)
file_sizes_len = file_sizes_len - 7
i = 0
while i <= file_sizes_len:
	line = file_sizes[i]
	line_split = line.split(":")
	sizes = line_split[1]
	number = sizes.split(" ")
	numbers = number[1]
	if '.' in numbers:
		MiB_to_KiB = float(numbers) * 1000
		new_size = int(MiB_to_KiB)
	else:
		new_size = int(numbers)

	#write to file
	file = open("sizes.txt", 'a')
	file.write(str(new_size))
	file.write(',') 
	i = i + 1

#sort
with open("sizes.txt", 'r') as s:
	sizes = s.read()
	sizes = sizes.split(',')
	rm_last = sizes[:-1]

no_sizes = len(rm_last)
new_list = []
for k in rm_last:
	new_dtype = int(k)
	new_list.append(new_dtype)

sort = sorted(new_list)
print(len(sort))
	
