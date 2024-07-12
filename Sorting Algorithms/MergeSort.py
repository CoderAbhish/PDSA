class MergeSort:
   def mergeTwoLists(self, A, B):
       (m, n) = (len(A), len(B))
       (resultLst, i, j) = ([], 0, 0)
       
       #case 1: When A and B both are non-empty
       while i<m and j<n:
           if A[i]<B[j]:
               resultLst.append(A[i])
               i += 1
           else:
               resultLst.append(B[j])
               j += 1

       #case 2: When A is non-empty but B is empty
       while i<m:
           resultLst.append(A[i])
           i += 1

       #case 2: When A is non-empty but B is empty
       while j<n:
           resultLst.append(B[j])
           j += 1
        
       return resultLst

   #region Recursive Method
   def recursiveMthd(self, unorderedLst):
       n = len(unorderedLst)
       if n<=1:
           return unorderedLst

       A = self.recursiveMthd(unorderedLst[:n//2])
       B = self.recursiveMthd(unorderedLst[n//2:])

       return self.mergeTwoLists(A, B)
   #endregion

unorderedLst1 = [3, 2, -1, 2, 4, 8]
unorderedLst2 = [10, 2, -7, 9, 3, 21]
sort = MergeSort()
print(sort.recursiveMthd(unorderedLst1))