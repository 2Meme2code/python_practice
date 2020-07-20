def is_in(list1, list2, list3):
  for i in list1:
     if i in list2 and i in list3:
         print(i)
         return True
  return False

def switch(num1, num2):
  num3=num1
  num1=num2
  num2=num3
  return[num1, num3]



def swap_array0(a):
  n=len(a)
  l=0
  r=n-1
  while l < r:
    t = a[l]
    a[l]=a[r]
    a[r]=t
    l=l+1
    r=r-1

def swap_array1(a):
  n=len(a)
  for i in range(n/2):
    t = a[i]
    a[i]=a[n-(i+1)]
    a[n-(i+1)] = t

  
