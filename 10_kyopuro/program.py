S = [input() for _ in range(12)]

ans = 0
for i in range(12):
  if len(S[i]) == i+1:
    ans += 1

print(ans)