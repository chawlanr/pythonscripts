# Program to print fibonacci series
def fibonacci(number):
  a,b=0,1
  if(number<=0):
    print("Entered number is too small")
  elif(number==1):
    print(a)
  elif(number==2):
    print(a,b)
  elif(number>2):
    print(a,b,end=" ")
    for i in range(number-2):
      c=a+b
      a,b=b,c
      print(c,end=" ")
  
number=int(input("Enter Integer number to print fibonacci series: "))
fibonacci(number)