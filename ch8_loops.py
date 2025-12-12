print("While loop - Print number from 1 to 9")
count=0
while(count < 10):
  print(count,end=' ')
  count+=1
print("\nWhile loop - infinite")
count=1
while count:
  print("Current number is = ",count)
  count=int(input("Enter any number other than 50 : "))
  if count==50:
    print("Entered value is 50")
    break

print("\nWhile loop - with else statement")
newnum=1
while newnum != 40:
  print("Current number is = ",newnum)
  newnum=int(input("Enter any number other than 40 : "))
else:
  print("Entered value is 40")

print("\nwhile loop - infinite loop till 0")
checknum=10
while (checknum): 
  print("Current number : ",checknum)
  checknum=int(input("Enter number other than 0 : "))
print("\nBye")

print("For loop - Simple list")
list=[10, 20, 30, 40, 50, 60]
for num in list:
  print(num,end=' ')

strfor=(input("\nEnter any string : "))
print("String = ",end='')
for str in strfor:
  print(str,end=' ')

print("\nRange operator")
print("Numbers are : ",end='')
for var in range(30, 40):
  print(var,end=' ')
print("\nNew Sequence : ",end='')
for var in range(5):
  print(var,end=' ')
tupnum=('Apple','Banana','Mango','Orange')
print("\nTuple elements : ",end='')
for tup in tupnum:
  print(tup,end=' ')
print("\nBye")
numbers=[11,33,55,39,55,75,30,21,29,41,13]
for num in numbers:
  if num%2==0:
    print("the list contains an even number")
    break
else:
  print("the list doesnot contain even number")
  print("\nMultiplication table using nested for loop")
for i in range(1,11):
  for j in range(1,11):
    k=i*j
    print(k,end='\t')
  print()

print("\ncontinue statement using for and while loop")
print ('Current Letter :')
for letter in 'Python': # First Example
  if letter == 'h':
    continue
  print (letter,end=' ')
var = 10 # Second Example
print ('Current variable value :',end='')
while var > 0:
  var = var -1
  if var == 5:
    continue
  print (var,end=' ')
print ("\nGood bye!")

print("\npass statement")
count=10
while count > 0:
  if count == 5:
    count-=1
    pass
  else:
    print(count,end=' ')
    count-=1

print("\nIterator and Generator")
list=[10, 20, 34, 56, 67, 83, 432, 567, 398]
it=iter(list)
for num in it:
  print(num,end=' ')
print("\n")
