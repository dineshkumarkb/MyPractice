l = [['user1', 40.0],
['user2', 50.0],
['user3', 40.0]]
# for _ in range(int(raw_input())):
#     l.append([raw_input(),float(input())])

for i in range(len(l)):
    print sorted(l[i][1])


