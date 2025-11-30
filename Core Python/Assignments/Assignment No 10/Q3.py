def maxEle(li):
    max = li[0]
    for ind in range(0,len(li)):
        if(max < li[ind]):
            max2 = max
            max = li[ind]
    return max2


li = [ 12,21,23,45,87,67,98,99]
min_ele = maxEle(li)
print("maximum element is :" ,min_ele)
