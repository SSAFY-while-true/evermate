# BOJ1174
# 줄어드는 수

from itertools import combinations

def create_desc_nums(num_length):
    """
    주어진 길이(num_length)의 감소하는 수들을 생성해 리스트로 반환하는 함수
    """
    desc_nums = []

    # 0~9 중 주어진 길이만큼 숫자 조합 (오름차순)
    for comb_tuple in combinations(range(10), num_length):
        num = 0

        # 오름차순 정렬된 튜플을 숫자로 변환
        # 예: (1, 4, 7) → 1x1 + 4×10 + 7×100 = 741
        for idx, digit in enumerate(comb_tuple):
            num += digit * (10 ** idx)
        
        desc_nums.append(num)
    
    return desc_nums

N = int(input())

all_desc_nums = []

for i in range(1, 11):
    all_desc_nums.extend(create_desc_nums(i))

all_desc_nums.sort()

if N - 1 >= len(all_desc_nums):
    print(-1)
else:
    print(all_desc_nums[N - 1])
