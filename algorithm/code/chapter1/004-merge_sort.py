'''
MERGE(A, p, q, r)
nL = q - p + 1 // length of A[p : q]
nR = r - q // length of A[q + 1 : r]
let L[0 : nL - 1] and R[0 : nR - 1] be new arrays
for i = 0 to nL - 1 // copy A[p : q] into L[0 : nL - 1]
  L[i] = A[p + i]
for j = 0 to nR - 1 // copy A[q + 1 : r] into R[0 : nR - 1]
  R[j] = A[q + j + 1]
i = 0 // i indexes the smallest remaining element in L
j = 0 // j indexes the smallest remaining element in R
k = p // k indexes the location in A to fill
// As long as each of the arrays L and R contains an unmerged
element,
// copy the smallest unmerged element back into A[p : r].
while i < nL and j < nR
  if L[i] ≤ R[j]
    A[k] = L[i]
    i = i + 1
  else A[k] = R[j]
    j = j + 1
  k = k + 1
// Having gone through one of L and R entirely, copy the
// remainder of the other to the end of A[p : r].
while i < nL
  A[k] = L[i]
  i = i + 1
  k = k + 1
while j < nR
  A[k] = R[j]
  j = j + 1
  k = k + 1
'''
'''
MERGE-SORT(A, p, r)
if p ≥ r // zero or one element?
  return
q = ⌊(p + r)/2⌋ // midpoint of A[p : r]
MERGE-SORT(A, p, q) // recursively sort A[p : q]
MERGE-SORT(A, q + 1, r) // recursively sort A[q + 1 : r]
// Merge A[p : q] and A[q + 1 : r] into A[p : r].
MERGE(A, p, q, r)
'''

def quick_sort(lists,i,j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists

if __name__=="__main__":
    lists=[30,24,5,58,18,36,12,42,39]
    print("排序前的序列为：")
    for i in lists:
        print(i,end =" ")
    print("\n排序后的序列为：")
    for i in quick_sort(lists,0,len(lists)-1):
        print(i,end=" ")