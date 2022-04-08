#!/usr/bin/python3

import sys #명령행 인자와 프로그램 중단을 위한 모듈

if len(sys.argv) != 3: #명령행 인자 개수 검사
	print('Invalid usage')
	sys.exit()
file_name = sys.argv[1] #파일 이름 가져오기
try:
	n = int(sys.argv[2]) #표시할 단어 개수 가져오기
except ValueError: #두 번째 인자가 숫자가 아닐 경우 예외 처리
	print('second parameter is not a number')
	sys.exit()

try:
	file = open(file_name, 'r') #파일 열기
except FileNotFoundError: #파일이 없을 경우 예외 처리
	print('File not found')
	sys.exit()
lines = file.readlines() #파일의 모든 줄 읽기
file.close() #파일 닫기

word_cnt = {} #단어와 개수를 저장할 dictionary
for line in lines: #각 줄마다 반복
	for word in line.replace('.', '').replace(',', '').split(): #해당 줄에서 '.', ',' 토큰 제거 후 단어로 나눠서 반복
		if not word in word_cnt: #해당 단어가 아직 dictionary에 없으면 추가
			word_cnt[word] = 0
		word_cnt[word] += 1 #단어 개수 추가
		word_sorted = sorted(word_cnt.items(), key=lambda x : x[1], reverse=True) #dictionary를 value의 역순으로 정렬

for i in range(0, n):
	print('%-12s %2d' % word_sorted[i]) #개수가 많은 순서대로 n개 출력
