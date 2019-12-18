array=[1,4,6,3,2,7,9,12,3,4,2,6,7]
unique_elements=[]
duplicate_elements=[]
for i in array:
    if i not in unique_elements:
        unique_elements.append(i)
    else:
        duplicate_elements.append(i)

print(unique_elements)
print(duplicate_elements)
