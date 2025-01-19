# # a)
# l=[1,2,3,4,5,6,7,8,9]
# r=list(map(str,l))
# print(r)

# # b)
# l=[1,2,3,4,5,6,7,8,9]
# r=list(filter(lambda x:x>5, l))
# print(r)

# c)
l=[1,2,3,4,5,6,7,8,9]
r=list(map(lambda x:x-1-len(l),l))
print(r)