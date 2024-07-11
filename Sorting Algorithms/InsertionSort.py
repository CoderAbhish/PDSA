class InsertionSort:
    #Iterative Method
    #region
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


unorderedLst1 = [3, 2, -1, 2, 4, 8]
unorderedLst2 = [10, 2, -7, 9, 3, 21]
sort = InsertionSort()
print(sort.iterativeMthd([]))