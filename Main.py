N = int(input())
M = 0
MS = []
for i in range(1, N+1):
    if N % i == 0:
        M += 1
        MS.append(i)
print(MS)
print(M)
