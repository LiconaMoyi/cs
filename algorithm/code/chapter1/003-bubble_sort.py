'''
BUBBLE-SORT(A,n)
for i=0 to n-1
  for j=0 to n-i
    if A[j]>A[j+1]
      swap(A[j],A[j+1])
'''
def bubble_sort_function(array):
  for i in range(0, len(array)-1):
    for j in range(0, len(array) - i - 1):
      if(array[j]>array[j+1]):
        temp=array[j]
        array[j]=array[j+1]
        array[j+1]=temp
    


if __name__ == "__main__":
  array = [8,6,5,4,3,2,1]
  bubble_sort_function(array)
  for item in array:
    print(item)