class SelectionSort:
    #region Iterative Method
    def iterativeMthd(self, lst):
        n = len(lst)
        if n < 1:
            return lst

        for i in range(n):
            minpos = i
            for j in range(i+1, n):
                if lst[j] < lst[minpos]:
                    minpos = j
            (lst[i], lst[minpos]) = (lst[minpos], lst[i])
        return lst
    #endregion
    #region Recursive Method
    def recursiveMthd(self, lst, start):
        n = len(lst)
        #Base condition
        if n<1 or start >= n:
            return lst
        #logic
        minpos = start
        for i in range(start, n):
            if lst[i] < lst[minpos]:
                minpos = i
        (lst[minpos], lst[start]) = (lst[start], lst[minpos])
        #self call
        return self.recursiveMthd(lst, start+1)
    #endregion
        

unorderedLst1 = [3, 2, -1, 2, 4, 8]
unorderedLst2 = [10, 2, -7, 9, 3, 21]
sort = SelectionSort()
print(sort.iterativeMthd(unorderedLst1))
print(sort.recursiveMthd(unorderedLst2, 0))