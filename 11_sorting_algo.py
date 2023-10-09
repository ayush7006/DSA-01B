"""
"The quick brown fox jumps over the lazy dog"
"This pangram lists four a's, one b, one c, two d's, twenty-nine e's, eight f's, three g's, five h's, eleven i's, one j,
 one k, three l's, two m's, twenty-two n's, fifteen o's, one p, one q, seven r's, twenty-six s's, nineteen t's, four u's,
   five v's, nine w's, two x's, four y's, and one z."
"""

def BubbleSort(data:list) -> list:
    for j in range(len(data)):
        for i in range(1,len(data)-j):
            if data[i-1] > data[i]:
                data[i],data[i-1] = data[i-1], data[i]
    return data

# l = [11,65,12,7,24,6,24,9]
# obj = BubbleSort(l)
# print(obj)

def SelectionSort(data:list)->list:
    l = len(data)
    for j in range(l):
        p = j
        for i in range(j+1,l):
            if data[i] < data[p]:
                p = i
        data[j],data[p] = data[p], data[j]
    return data

# l = [11,65,12,7,24,6,24,9]
# obj = SelectionSort(l)
# print(obj)

def InsertionSort(data:list)->list:
    l = len(data)
    for j in range(1,l):
        key = data[j]
        i = j-1
        while i >= 0 and data[i] > key :
            data[i+1] = data[i]
            i -= 1
        data[i+1] = key

    return data

# l = [11,65,12,7,24,6,24,9]
# obj = InsertionSort(l)
# print(obj)


def margesort(data:list)->list:
    if len(data)>1:

    #---------split---------------    
        m = len(data)//2
        L = data[:m]
        R = data[m:]

        margesort(L)
        margesort(R)
        
    #----------marge---------------
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i+=1
            else:
                data[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1
    return (data)

# l = [11,65,12,7,24,6,24,9]
# obj = margesort(l)
# print(obj)


def quickshot(data:list,s:int,e:int)->list:
    if e-s+1<=1:
        return
    pivot = data[e]
    left = s
    for i in range(s,e):
        if data[i]<pivot:
            data[left], data[i] = data[i], data[left]
            left+=1
    data[e],data[left] = data[left], pivot
    
    quickshot(data,s,left-1)
    quickshot(data,left+1,e)

    return data

# l = [11,65,12,7,24,6,24,9]
# s,e=0,len(l)-1
# obj = quickshot(l,s,e)
# print(obj)


def bucketshot(data:list)->list:
    l = max(data)+1
    count = [0]*l
    for i in data:
        count[i]+=1

    i=0
    for n in range(len(count)):
        for j in range(count[n]):
    #         print(n)
            data[i] = n
            i += 1
    return data

# l = [11,65,12,7,24,6,24,9]
# obj = bucketshot(l)
# print(obj)


def linearsearch(data:list,itme:int)->bool:
    for i in range(0,len(data)):
        if data[i]==itme:
            return True
        return False
    
# l = [11,65,12,7,24,6,24,9]
# itme = 10
# obj = linearsearch(l,itme)
# print(obj)

def binarySearch1(data:list,itme:int)->bool:
    m = len(data)//2
    if not data:
        return False
    if itme > data[m]:
         return binarySearch1(data[m:],itme)
    elif itme < data[m]:
         return binarySearch1(data[:m],itme)
    else:
        return True
    
# l = [11,65,12,7,24,6,24,9]
# li = margesort(l)
# itme = 7
# obj = binarySearch1(li,itme)
# print(obj)

def binarySearch2(data:list, itme:int)->bool:
    low,high =0, len(data)-1
    while low <= high:
        mid = low + (high - low)//2
        if data[mid] > itme:
            high = mid - 1
        elif data[mid] < itme:
            low = mid + 1
        else:
            return True
    return False

# l = [11,65,12,7,24,6,24,9]
# li = margesort(l)
# itme = 9
# obj = binarySearch2(li,itme)
# print(obj)