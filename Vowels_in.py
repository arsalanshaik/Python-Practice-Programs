String1=input("Enter String 1:")
vowels=['a','e','i','o','u']
vowels_in_list=[]
String1.lower()
for i in String1:
    if i in vowels:
        vowels_in_list.append(i)

print(vowels_in_list)