"""
  test
"""

#引用csv模块。
import csv

#待写入csv文件的内容
data = [['lkj ', '1097830167@qq.com'],['liziyu', '429489623@qq.com'],['xiaoxian','747588327@qq.com']]

with open('python file/to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
