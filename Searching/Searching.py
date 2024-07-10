
class BinarySearch:
    orderedLst = []
    targetVal = 0
    def __init__(object, orderedList, targetVal):
        object.orderedLst = orderedList
        object.targetVal = targetVal
        
    def iterativeMthd(object):
        n = len(object.orderedLst)
        if n < 1:
            return object.orderedLst
        
        (firstIndex, mid, lastIndex) = (0, n//2, n-1)
        while lastIndex >= firstIndex:
            if object.orderedLst[mid] == object.targetVal:
                return mid  
            elif object.orderedLst[mid] < object.targetVal:
                firstIndex = mid+1
            else:
                lastIndex = mid-1
                
            mid = firstIndex + (lastIndex - firstIndex)//2
        return -1
    
search = BinarySearch([2, 4, 6, 7, 12, 15, 17], 4)
print(search.iterativeMthd())