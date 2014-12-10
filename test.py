#!/usr/bin/python
import re


file = open('sample.log','r')
FILE = file.readlines()
file.close()

countnum, getmesnum, friendspronum, friendscornum, postidnum, getidnum = (0,)*6


counttimevalues = []
getmessagevalues = []
friendsprogvalues = []
friendscrovalues = []
postidvalues = []
getidvalues = []
dynos = []
dynos1 = []
dynos2 = []
dynos3 = []
dynos4 = []
dynos5 = []

value = 0


def bubbleSort(sortvalues):
    for passnum in range(len(sortvalues)-1,0,-1):
        for i in range(passnum):
            if sortvalues[i]>sortvalues[i+1]:
                temp = sortvalues[i]
                sortvalues[i] = sortvalues[i+1]
                sortvalues[i+1] = temp
                return sortvalues
def mode(arr):
    m = max([arr.count(a) for a in arr])
    return [x for x in arr if arr.count(x) == m][0] if m>1 else None

def median(x):
    if len(x)%2 != 0:
        return x[len(x)/2]
    else:
        midavg = (x[len(x)/2] + x[len(x)/2-1])/2.0
        return midavg

def aver(array, total):
		return float(sum(array))/float(total)


for line in FILE:
	countpending = re.search('count_pending_messages', line)
	getmessages = re.search('get_messages', line)
	friendsprogress = re.search('get_friends_progress', line)
	friendsscore = re.search('get_friends_score', line)
	postid = re.search('POST', line)
	getid = re.search('count_pending_messages', line)
	getdyno = re.search("web.11", line)

	if countpending:
		countnum = countnum +1
		value = int(line.partition("connect=")[2].partition("ms")[0]) + int(line.partition("service=")[2].partition("ms")[0])
		counttimevalues.append(value)
		dynos.append(line.partition("dyno=web.")[2].partition(" ")[0])		

	elif getmessages:
		getmesnum = getmesnum+1
		value = int(line.partition("connect=")[2].partition("ms")[0]) + int(line.partition("service=")[2].partition("ms")[0])
		getmessagevalues.append(value)
		dynos1.append(line.partition("dyno=web.")[2].partition(" ")[0])		

	elif friendsprogress:
		friendspronum = friendspronum+1
		value = int(line.partition("connect=")[2].partition("ms")[0]) + int(line.partition("service=")[2].partition("ms")[0])
		friendsprogvalues.append(value)
		dynos2.append(line.partition("dyno=web.")[2].partition(" ")[0])		

	elif friendsscore:
		friendscornum = friendscornum+1
		value = int(line.partition("connect=")[2].partition("ms")[0]) + int(line.partition("service=")[2].partition("ms")[0])
		friendscrovalues.append(value)
		dynos3.append(line.partition("dyno=web.")[2].partition(" ")[0])		

	elif postid:
		postidnum = postidnum+1
		value = int(line.partition("connect=")[2].partition("ms")[0]) + int(line.partition("service=")[2].partition("ms")[0])
		postidvalues.append(value)
 		dynos4.append(line.partition("dyno=web.")[2].partition(" ")[0])		

 	else:
		getidnum = getidnum+1
		value = int(line.partition("connect=")[2].partition("ms")[0]) + int(line.partition("service=")[2].partition("ms")[0])
		getidvalues.append(value)
		dynos5.append(int(line.partition("dyno=web.")[2].partition(" ")[0]))

print "  "
print "STATISTICS FOR ALL"
print "  "

print "count_pending_messages"
print "Total", countnum
print "Average",aver(counttimevalues, countnum)
print "Mode", mode(counttimevalues)
print "Median", median(counttimevalues)
print "Most responded dyno",mode(dynos)
print "  "

print "get_messages"
print "Total", getmesnum
print "Average", aver(getmessagevalues, getmesnum)
print "Mode", mode(getmessagevalues)
print "Median", median(getmessagevalues)
print "Most responded dyno", mode(dynos1)
print "  "

print "get_friends_progress"
print "Total", friendspronum
print "Average", aver(friendsprogvalues, friendspronum)
print "Mode", mode(friendsprogvalues)
print "Median", median(friendsprogvalues)
print "Most responded dyno", mode(dynos2)
print "  "

print "get_friends_score"
print "Total", friendscornum
print "Average", aver(friendscrovalues, friendscornum)
print "Mode", mode(friendscrovalues)
print "Median", median(friendscrovalues)
print "Most responded dyno", mode(dynos3)
print "  "

print "post id values"
print "Total", postidnum
print "Average", aver(postidvalues, postidnum)
print "Mode", mode(postidvalues)
print "Median", median(postidvalues)
print "Most responded dyno", mode(dynos4)
print "  "

print "get id values"
print "Total", getidnum
print "Average", aver(getidvalues, getidnum)
print "Mode", mode(getidvalues)
print "Median", median(getidvalues)
print "Most responded dyno", mode(dynos5)
print "  "



