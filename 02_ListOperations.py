orglist = [1, 2, 3 , 4, 5, 6,7 ,8, 9, 10]

print(orglist)
orglist.append(11)
print("After appending:",orglist)

orglist.insert(2, "new element")
print("After inserting 'new element' at position 2: ", orglist)

val = "new element"
orglist.remove(val)
print("After removing 'new element':", orglist)

print("Largest element: ", max(orglist))
print("smallest element: ", min(orglist))

orglist.sort()
print("Second largest element:", orglist[-2])

newlist = [90,80,70]
print(newlist)
print(orglist)
concatlist = orglist + newlist
print("After concatenation:", concatlist)

revlist = orglist[::-1]
print("reversed list:", revlist)

copylist = orglist.copy()
print("Copied list:", copylist)

orglist.append(11)

print("original list:",orglist)
print("Removing duplicate elemensts from list:",set(orglist))

matri1 = [[1, 2], [3,4]]
matri2 = [[5,6], [7,8]]
result = [[0,0], [0,0]]

for i in range(2):
    for j in range (2):
        result[i][j] = matri1[i][j] +  matri2[i][j]
print("Matrix Addition: " ,result)

