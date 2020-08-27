import random
import sys
import time

import pandas as pd


def clean_data():
	filepath = input('请输入数据文件地址: ')
	df = pd.read_excel(filepath)

	# drop duplicate 
	df = df.drop_duplicates(subset=['mid'])

	# select result before 2020-08-18 18:00:00
	df['time'] = pd.to_datetime(df['time'])
	cond = df['time'] < '2020-08-18 18:00:00'
	dfs = df[cond]
	return dfs

def lottery(df):
	# get name list
	names = df['name'].to_list()

	try:
		while True:
			i = random.randint(0, len(names)-1)
			time.sleep(0.05)
			print(names[i])
	except KeyboardInterrupt:
		print(f'\r来让我们公司这个B\n..................站用户: \n >>>>>>>>>>>>>>>>{names[random.randint(0, len(names)-1)]}<<<<<<<<<<<<<<<<<<')

def main():
	df = clean_data()
	lottery(df)