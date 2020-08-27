import json
import requests
import time

import pandas as pd


def get_comments(user_id: int, page_num: int):
  dic = {}
  count_page = 1
  for i in range(0, page_num):
    url = f'https://api.bilibili.com/x/v2/reply?pn={i}&type=1&oid={user_id}&sort=2'
    str = requests.get(url=url).text
    dic[i] = json.loads(str)
    print(f'已获取第{count_page}页评论')
    count_page += 1
  return dic


def c_time(timeStamp):
  tupTime = time.localtime(timeStamp)
  stadardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
  return stadardTime


def clean_data(data):
  dic = {
    'name': [],
    'comment': [],
    'time': [],
    'mid': [],
  }
  for each_info in data.values():
    comments_data = each_info["data"]["replies"]
    for info in comments_data:
      dic['name'].append(info["member"]["uname"])
      dic['mid'].append(info["member"]["mid"])
      dic['comment'].append(info["content"]["message"])
      dic['time'].append(c_time(info["ctime"]))
  return dic

def main():
  user_id = input('请输入你的B站id: ')
  page_num = input('请输入评论页数: ')
  output_file = input('输出excel文件路径: ')
  data = clean_data(get_comments(int(user_id), int(page_num)))
  df = pd.DataFrame(data)
  df.to_excel(output_file)
  print(f'数据文件已导出到: {output_file}')
  return

main()
