X = int(input())
cnt = 0

for i in bin(X):
    if i == '1':
        cnt += 1

print(cnt)
