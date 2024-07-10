#Binary search (both Iterative and Recursive method)

class BinarySearch:
    #region Iterative Method
    def iterativeMthd(object, orderedLst, targetVal):
        n = len(orderedLst)
        if n < 1:
            return orderedLst
        
        (firstIndex, mid, lastIndex) = (0, n//2, n-1)
        while lastIndex >= firstIndex:
            if orderedLst[mid] == targetVal:
                return mid  
            elif orderedLst[mid] < targetVal:
                firstIndex = mid+1
            else:
                lastIndex = mid-1
                
            mid = (lastIndex + firstIndex)//2
        return -1
    #endregion
    #region Recursive Method
    def recursiveMthd(object, orderedLst, targetVal, low, high):
        if high - low < 0:
            return -1
        mid = (high + low)//2
        if orderedLst[mid]== targetVal:
            return mid
        elif targetVal > orderedLst[mid]:
            return(object.recursiveMthd(orderedLst, targetVal, mid+1, high))
        else:
            return(object.recursiveMthd(orderedLst, targetVal, low, mid-1))
    #endregion
    
search = BinarySearch()
lst = [2, 4, 6, 7, 12, 15, 17]
target = 15
print(search.iterativeMthd(lst, target))
print(search.recursiveMthd(lst, target, 0, len(lst)-1))