# 1592809575
# "2020-01-01 00:00:00"
import datetime
print(datetime.datetime.fromtimestamp(1738586798))
tslist=[]
for i in range(2014,2026):
    f=datetime.datetime.timestamp(datetime.datetime(i, 1, 1, 0, 0, 0))
    tslist.append(int(f))

print(tslist)