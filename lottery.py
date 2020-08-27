import random
import time

import pandas as pd


def clean_data(filepath: str, deadline: str):
	df = pd.read_csv(filepath)

	# drop duplicate 
	df = df.drop_duplicates(subset=['mid'])

	# select result before 2020-08-18 18:00:00
	df['time'] = pd.to_datetime(df['time'])
	cond = df['time'] < deadline
	dfs = df[cond]
	return dfs


def main():
	# get name list
	filepath = input('请输入数据文件地址(默认为result.csv): ')
	if not filepath:
		filepath = 'result.csv'
	deadline = input('请输入截止时间(例如2020-08-18 18:00:00): ')
	df = clean_data(filepath, deadline)
	names = df['name'].to_list()

	try:
		while True:
			i = random.randint(0, len(names)-1)
			time.sleep(0.05)
			print(names[i])
	except KeyboardInterrupt:
		print(f'\r************************我擦！幸运儿在此*********************\n'
					f'让我们恭喜这个B\n..................站用户: \n'
					f'>>>>>>>>>>>>>>>>{names[random.randint(0, len(names)-1)]}'
					f'<<<<<<<<<<<<<<<<<<')


if __name__ == '__main__':
	main()
