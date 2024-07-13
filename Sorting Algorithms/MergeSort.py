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
   #region Iterative Method
   def iterativeMthd(self, unorderedLst):
       n = len(unorderedLst)
       if n<=1:
           return unorderedLst

       #Setting the width(size) of List for each pass
       width = 1
       #A list cannot be broken down into size grater than it's own
       while width<n:
           #leftmost index of first list for each pass
           firstIdx_LeftLst= 0

           #till all the indices have been visited
           while firstIdx_LeftLst < n:
               firstIdx_RightLst= firstIdx_LeftLst + width

               #Updating the Lists to be merged
               lstA = unorderedLst[firstIdx_LeftLst:(firstIdx_LeftLst + width)]
               if firstIdx_RightLst < n:
                   lstB = unorderedLst[firstIdx_RightLst:min((firstIdx_RightLst + width),n)]
               else:
                   lstB = []

               tempLst = self.mergeTwoLists(lstA, lstB)

               #replace the value of sorted elements
               i=firstIdx_LeftLst
               for j in range(len(tempLst)):
                   unorderedLst[i] = tempLst[j]
                   i += 1
               firstIdx_LeftLst += width*2
           width = width*2
       return unorderedLst
   #endregion

unorderedLst1 = [3, 2, -1, 2, 4, 8]
unorderedLst2 = [10, 2, -7, 9, 3, 21, 0]
sort = MergeSort()
print(sort.recursiveMthd(unorderedLst1))
print(sort.iterativeMthd(unorderedLst2))