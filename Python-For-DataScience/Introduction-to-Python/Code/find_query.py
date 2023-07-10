dict = {1:"abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]
for i in range(len(query)):
    print(dict.get(query[i]))
