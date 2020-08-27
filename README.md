# Bilibili Python抽奖脚本
这是一个基于Python3.8的B站评论抽奖的脚本
* 确保`Python`为3.0以上
* 安装依赖
```bash
pip install -r requirements.txt -i http://pypi.douban.com/simple/
``` 
* 运行`get_comments.py`并输入对应信息获取评论文件。
```bash
python get_comments.py
请输入你的B站id: 711846602
请输入评论页数: 18
输出csv文件路径(默认为result.csv): result.csv
已获取第1页评论
已获取第2页评论
已获取第3页评论
...
已获取第18页评论
数据文件已导出到: result.csv
```
* 运行抽奖程序`get_results.py`并输入提示信息将会持续打印用户名, 按`ctrl+c`终止得到幸运用户。
```bash
python get_results.py
请输入数据文件地址(默认为result.csv):
请输入截止时间(例如2020-08-18 18:00:00): 2020-08-18 18:00:00
猫王胖虎
...
亏斯莫斯
蓝大仙2333
言覃月半子
************************我擦！幸运儿在此*********************
让我们恭喜这个B
..................站用户:
>>>>>>>>>>>>>>>>>>>>>>>>RCR_HJ<<<<<<<<<<<<<<<<<<<<<<<
```