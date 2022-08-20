'''
INSERTION-SORT(A,n)
for i=2 to n
  key=A[i]
  //Insert A[i] into the sorted subarray A[1,i-1]
  j=i-1
  while j>=0 and A[j]>key
    A[j+1]=A[j]
    j=j-1
  A[j+1]=key
'''

def insertion_sort_function(array):
  for i in range(1, len(array)):
    key = array[i]
    j=i-1
    while j>=0 and array[j]>key:
      array[j+1] = array[j]
      j=j-1
    array[j+1]=key
    


if __name__ == "__main__":
  array = [8,6,5,4,3,2,1]
  insertion_sort_function(array)
  for item in array:
    print(item)
