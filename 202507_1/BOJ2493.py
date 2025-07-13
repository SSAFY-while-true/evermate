# BOJ2493
# 탑

N = int(input())
heights = list(map(int, input().split()))

answer = [0] * N
stack = []  # 수신 대기중인 탑들 

for idx in range(N - 1, -1, -1):
    cur_height = heights[idx]
    
    # 쌓인 신호들 가능하면 수신
    while stack and heights[stack[-1]] < cur_height:
        sender_idx = stack.pop()
        answer[sender_idx] = idx + 1

    # 현재 탑은 수신 대기로 스택에 추가
    stack.append(idx)

print(' '.join(map(str, answer)))
