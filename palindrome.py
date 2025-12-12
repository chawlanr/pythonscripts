string=input("Enter any string: ")
# if(string not in " \n\t"):
    # string=(string.replace(" ","")).upper()
    # if(string == string[::-1]):
        # print("Entered string is Palindrome")
    # else:
        # print("Entered string is not Palindrome")
# else:
    # print("Entered is either empty string or not a string")
count=0
if(string not in " \n\t"):
    half=len(string)//2
    for x in range(half):
        if(string[x]==string[-(x+1)]):
            count+=1
            continue
    if(count==half):
        print("Entered string is Palindrome!!")
        print("New LINE")
    else:
        print("Entered string is not Palindrome!!")
else:
    print("Entered is either empty string or not a string")
