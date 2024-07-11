class InsertionSort:
    #region Iterative Method
    def iterativeMthd(self, lst):
        n = len(lst)
        if n < 1:
            return lst

        for i in range(1, n):
            j = i
            while j > 0 and lst[j]<lst[j-1]:
                (lst[j], lst[j-1]) = (lst[j-1], lst[j])
                j -= 1
        return lst
    #endregion
    
    #region Iterative Method
    def recursiveMthd(self, lst, currentPos=1):
        n = len(lst)
        #Base consdition
        if n<1 or currentPos>=n:
            return lst
        #logic
        j = currentPos
        while j>0 and lst[j]<lst[j-1]:
            (lst[j], lst[j-1]) = (lst[j-1], lst[j])
            j -= 1
        #recursive call
        return self.recursiveMthd(lst, currentPos +1)
    #endregion

unorderedLst1 = [3, 2, -1, 2, 4, 8]
unorderedLst2 = [10, 2, -7, 9, 3, 21]
sort = InsertionSort()
print(sort.iterativeMthd(unorderedLst1))
print(sort.recursiveMthd(unorderedLst2))