two = input()
if '0' in two:
    two = two.replace('0','1',1)
else:
    two = two[:len(two)-1] + '0'
ans = 0

for i in range(len(two)):
    ans += int(two[i])*(2**(len(two)-i-1))
print(ans)
