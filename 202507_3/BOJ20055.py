# BOJ20055
# 컨베이어 벨트 위의 로봇

from collections import deque
N, K = map(int, input().split())
# [내구도, 화물 유무]
belt = deque([hp, 0] for hp in map(int, input().split()))

UP = 0
DOWN = N - 1

zero_count = 0
step = 0

while True:
    step += 1


    # 1
    belt.rotate(1)
    belt[DOWN][1] = 0

    # 2
    for i in range(N-2, -1, -1):
        if belt[i][1] == 1 and belt[i+1][1] == 0 and belt[i+1][0] > 0:
            belt[i][1], belt[i+1][1] = 0, 1
            belt[i+1][0] -= 1
            if belt[i+1][0] == 0:
                zero_count += 1

    belt[DOWN][1] = 0

    # 3
    if belt[UP][0] > 0 and belt[UP][1] == 0:
        belt[UP][1] = 1
        belt[UP][0] -= 1
        if belt[UP][0] == 0:
            zero_count += 1

    # 4
    if zero_count >= K:
        break

print(step)



from collections import deque

N, K = map(int, input().split())

# 인덱스 의미 부여
HP = 0
IS_LOADED = 1

# [내구도, 화물 유무]
belt = deque([[hp, False] for hp in map(int, input().split())])

UP = 0
DOWN = N - 1

zero_count = 0
step = 0

while True:
    step += 1

    # 1
    belt.rotate(1)
    belt[DOWN][IS_LOADED] = False

    # 2
    for i in range(N - 2, -1, -1):
        if belt[i][IS_LOADED] and not belt[i + 1][IS_LOADED] and belt[i + 1][HP] > 0:
            belt[i][IS_LOADED] = False
            belt[i + 1][IS_LOADED] = True
            belt[i + 1][HP] -= 1
            if belt[i + 1][HP] == 0:
                zero_count += 1

    belt[DOWN][IS_LOADED] = False

    # 3
    if belt[UP][HP] > 0 and not belt[UP][IS_LOADED]:
        belt[UP][IS_LOADED] = True
        belt[UP][HP] -= 1
        if belt[UP][HP] == 0:
            zero_count += 1

    # 4
    if zero_count >= K:
        break

print(step)
