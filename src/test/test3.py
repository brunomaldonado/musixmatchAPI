name1 = [['a', 'b', 'c', 'd', 'e', 'f', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff'], ['a', 'b', 'c', 'd', 'e', 'f', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff'], ['a', 'b', 'c', 'd', 'e', 'f', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']]
name2 = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']

print(name1[-1])

# name1 = [['a', 'b', 'c', 'd', 'e', 'f'], ['aa', 'bb', 'cc', 'dd', 'ee', 'ff]]

# for i in range(len(name1)):
#   name1[i] = [item for item in name1[i] if item in name2]

# print(name1)

# unique_filtered = []
# indices = []
# seen = set()

# for sublist in name1:
#   filtered = [item for item in sublist if item in name2]

#   item = tuple(filtered)
#   if item not in seen:
#     seen.add(item)
#     unique_filtered.append(filtered)
#     idx = [sublist.index(item) + 1 for item in filtered]
#     indices.append(idx)

#     break

# print(f"uunique_filtered\n{unique_filtered}\nindices {indices}")


# delete duplicate list
unique_name1 = []
seen = set()
for sublist in name1:
  item = tuple(sublist)
  if item not in seen:
    seen.add(item)
    unique_name1.append(sublist)

# print(f"unique_name1 {unique_name1}")

# sepaate elements into two groups (those in name1 and those not in name1)
final_result = []
seen_sublist = set()

for sublist in unique_name1:
  not_in_name2 = [item for item in sublist if item not in name2]
  in_name2 = [item for item in sublist if item in name2]

  # print(f"not_in_name2 {not_in_name2}\nin_name2 {in_name2}")

  # convert to tuples to avoid duplicates
  if tuple(not_in_name2) and tuple(not_in_name2) not in seen_sublist:
    final_result.append(not_in_name2)
    seen_sublist.add(tuple(not_in_name2))

  if tuple(in_name2) and tuple(in_name2) not in seen_sublist:
    final_result.append(in_name2)
    seen_sublist.add(tuple(in_name2))

# update name1
name1 = final_result
print(f"name1 {name1}")

indices = []
for sublist in name1:
  if all(item in sublist for item in name2):
    idx = [sublist.index(item) + 1 for item in name2]
    indices.append(idx)

print(indices)



