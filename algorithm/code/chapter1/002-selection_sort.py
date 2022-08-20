'''
SELECTION-SORT(A,n)
for i=0 to n-2
  index=i
  for j=i+1 to n-1
    if A[index]>A[j]
      index=j
  temp=A[index]
  A[index]=A[i]
  A[i]=temp
'''

def selection_sort_function(array):
  for i in range(0, len(array)-1):
    index = i
    for j in range(i+1, len(array)):
      if(array[index]>array[j]):
        index=j
    temp=array[index]
    array[index]=array[i]
    array[i]=temp
    


if __name__ == "__main__":
  array = [8,6,5,4,3,2,1]
  selection_sort_function(array)
  for item in array:
    print(item)