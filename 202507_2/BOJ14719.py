# BOJ 14719
# 빗물

H, W = map(int, input().split())
arr = list(map(int, input().split()))

total_water = 0
stack = []

for i in range(W):
    # 현재 높이가 이전보다 높다면, 물 고일 수 있는 조건을 체크
    while stack and arr[i] > arr[stack[-1]]:
        bottom = stack.pop()  # 물이 고일 바닥 높이의 인덱스 
        
        if not stack:
            break  # 왼쪽 벽이 없음

        distance = i - stack[-1] - 1  # 양쪽 벽 사이 거리
        depth = min(arr[i], arr[stack[-1]]) - arr[bottom]
        total_water += distance * depth

    stack.append(i)

print(total_water)
