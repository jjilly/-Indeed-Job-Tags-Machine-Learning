import csv

def combineArrayAndWriteToFile(licAr,supAr,eduAr,expAr,timeAr,payAr):
    wholesomeArr=stringArrayConcatinate(licAr,supAr)
    wholesomeArr=stringArrayConcatinate(wholesomeArr,eduAr)
    wholesomeArr=stringArrayConcatinate(wholesomeArr,expAr)
    wholesomeArr = stringArrayConcatinate(wholesomeArr, timeAr)
    wholesomeArr = stringArrayConcatinate(wholesomeArr, payAr)
    wholesomeArr=nullStringToBullet(wholesomeArr)
    with open('tags.tsv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['tags'])
        for val in wholesomeArr:
            writer.writerow([val])


def stringArrayConcatinate(originalArr,extArr):
    wholesomeArr = []
    for i in range(0,len(originalArr)):
        if not extArr[i] == "":
            wholesomeArr.append(extArr[i]+" "+originalArr[i])
        elif not originalArr[i] == "":
            wholesomeArr.append(originalArr[i])
        else:
            wholesomeArr.append('')
    return wholesomeArr

def nullStringToBullet(arr):
    wholesomeArr=[]
    for i in range(0,len(arr)):
        if arr[i] == '':
            wholesomeArr.append(' ')
        else:
            wholesomeArr.append(arr[i])
    return wholesomeArr