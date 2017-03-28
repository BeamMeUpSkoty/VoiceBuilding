import os, re

us_path = "../resources/MAUS_TextGrids"
gb_path = "../resources/MAUS_TextGrids_GB"


us_names = []
gb_names = []

for root, dirs, files in os.walk(us_path, topdown=False):
    for name in files:
        if name[-9:] == ".TextGrid":
            us_names.append(name)


#for root, dirs, files in os.walk(gb_path, topdown=False):
#    for name in files:
#        if name[-9:] == ".TextGrid":
#            gb_names.append(name)
for i in us_names:
    print(i)
    m = i
    comb = open(i, 'w', encoding = 'utf-8')
    us = open(us_path+"/"+i, encoding = 'utf-8')
    gb = open(gb_path+"/"+i, encoding = 'utf-8')
    count = 0
    us_intervals = []
    gb_intervals = []
    arr = []
    arr2 = []
    for i in us:
        if re.search('intervals \[.', i) != None:
            count = 1
        if count == 1:
            if re.search('intervals \[.', i) != None:
                us_intervals.append(arr)
                arr = []
                arr.append(re.sub('\s','',i))
            else:
                i = re.sub('\s','',i)
                i = re.sub('(xmin=|xmax=|text=|\")', '', i)
                arr.append(i)
    us_intervals.append(arr)

    for i in gb:
        if re.search('intervals \[.', i) != None:
            count = 1
        if count == 1:
            if re.search('intervals \[.', i) != None:
                gb_intervals.append(arr2)
                arr2 = []
                arr2.append(re.sub('\s','',i))
            else:
                i = re.sub('\s','',i)
                i = re.sub('(xmin=|xmax=|text=|\")', '', i)
                arr2.append(i)
    gb_intervals.append(arr2)
    us_intervals = us_intervals[1:]
    gb_intervals = gb_intervals[1:]
    for i in us_intervals:
        i[1] = float(i[1])
        i[2] = float(i[2])
    for i in gb_intervals:
        i[1] = float(i[1])
        i[2] = float(i[2])
    times = []
    for u in us_intervals:
        for g in gb_intervals:
            if u[1] >= g[1] and u[1] <= g[2]:
                if u[3] == 'V' and g[3] == '@':
                    if u[1] not in times:
                        times.append(u[1])
            elif u[2] >= g[1] and u[2] <= g[2]:
                if u[3] == 'V' and g[3] == '@':
                    if u[1] not in times:
                        times.append(u[1])
    counter = 0
    us = open(us_path+"/"+m, encoding = 'utf-8')
    gb = open(gb_path+"/"+m, encoding = 'utf-8')
    for j in us:
        xmin = re.search('xmin = (.*)$', j)
        if xmin != None:
            counter = 1
        text = re.search('text = ', j)
        if text != None and counter == 1:
            j = re.sub('V','@',j)
            counter = 0
            comb.write(j)
        else:
            comb.write(j)
    comb.close()
        
        
        
            
