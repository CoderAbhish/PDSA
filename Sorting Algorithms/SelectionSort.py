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

unorderedLst = [3, 2, -1, 2, 4, 8]
sort = SelectionSort()
print(sort.iterativeMthd(unorderedLst))