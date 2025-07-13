# BOJ1660 
# 캡틴 이다솜

N = int(input())

# 주어진 포탄 내에서 가능한 모든 사면체 구하기 
bomb_stacks = []

cur_sum = 1
cur_add = 1
next_level = 2

while cur_sum <= N:
    bomb_stacks.append(cur_sum)
    cur_add += next_level
    next_level += 1
    cur_sum += cur_add

# dp[i] : i개의 대포알 다 써서 만들수있는 사면체들의 최소 개수
dp = [float('inf')] * (N + 1)
dp[0] = 0

for stack in bomb_stacks:
    for total in range(stack, N + 1):
        dp[total] = min(dp[total], dp[total - stack] + 1)

print(dp[-1])
