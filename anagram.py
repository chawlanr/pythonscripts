# Write Python function to find given two strings are 'anagram or not'
def ana(str1, str2):
  if(len(str1)==len(str2)):
    for x in list(str1):
      if(x in str2):
        continue
      else:
        print("Contents of string1 all are not in string2")
        break
    print("Both strings are anagram")
  else:
    print("String length are not matched")

s1=input("Enter first string: ")
s2=input("Enter second string: ")
ana(s1,s2)
