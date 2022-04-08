#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
	print('Invalid usage')
	sys.exit()
file_name = sys.argv[1]
try:
	least_cnt = int(sys.argv[2])
except ValueError:
	print('second parameter is not a number')
	sys.exit()

try:
	file = open(file_name, 'r')
except FileNotFoundError:
	print('File not found')
	sys.exit()
lines = file.readlines()
file.close()

word_cnt = {}
for line in lines:
	for word in line.replace('.', '').replace(',', '').split():
		if not word in word_cnt:
			word_cnt[word] = 0
		word_cnt[word] += 1
		word_cnt = dict(sorted(word_cnt.items(), key=lambda x : x[1], reverse=True))

for key, value in word_cnt.items():
	if value >= least_cnt:
		print(('%-15s %3d') % (key, value))
