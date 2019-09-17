#coding:utf-8
import csv

datalist = [ ]
filename = 'sar14'
destfile = 'sar14.csv'

linenum_begin = 0
linenum_end = 0
linenum = 0

# --------------- 得到内存文本块的统计信息
with open(filename) as fd:
    for line in fd.readlines():
        linenum += 1
        # print(line)

        if line.find('%memused') != -1 :
            # 得到开始
            linenum_begin = linenum
            continue
        if linenum_begin != 0:
                # print(linenum , "|" + line)
            if line.find('Average') != -1:
                linenum_end = linenum
                break
print('行号: ',linenum_begin, '-', linenum_end)

# ------------------ 内存使用情况
linenum = 0
bStart = False
datalist = [ ]
with open(filename) as fd:
    for line in fd.readlines():
        linenum += 1
        if linenum_begin ==  linenum :
            bStart = True
            continue
        if linenum_end == linenum:
            break

        if bStart :
            sline = line.replace('  ',' ')
            sline = sline.replace('  ',' ')
            sline = sline.replace('  ',' ')

            clist = line.split(' ')
            newlist = [ ]
            for c in clist:
                if c != '':
                    newlist.append(c)
            dtuple = (newlist[0], newlist[4])
            print(dtuple)
            datalist.append(dtuple)
# print(datalist)
# ------------ 输出csv
headers = ['time','mem%']
with open(destfile,'w') as fcsv:
    writer = csv.writer(fcsv)
    writer.writerow(headers)
    writer.writerows(datalist)

