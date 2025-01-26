print("5,2,4,6,1,3")
A = [5,2,4,6,1,3]

for j in range(1, (len(A))):
  key = A[j]
  print("j --",key,j)   
  i = j-1
  while i>=0 and A[i]>key:
    print("change ", A[i+1],A[i])
    A[i+1]=A[i]  
    i = i-1
    
  print("i --",key,i)   
  A[i+1]=key

  for x in range(0,len(A)):
    print(A[x])