import random    

def D(x,n):
  conta = 0 
  i = 1                     
  conta = conta+1   
            
  while i < n:
    x[i] =  x[i] +2 
    i = i + 2
    conta = conta+5
  
  i = 1
  conta = conta+1
  while i <= n/2:
    x[i] = x[i] + x[i+1] 
    i = i+1
    conta = conta+7

  print conta
        

B = random.sample(xrange(100), 10)
C = random.sample(xrange(100), 100)
E = random.sample(xrange(1000), 1000)


D(B,10)
print("-----")
D(C,100)
print("-----")
D(E,1000)

