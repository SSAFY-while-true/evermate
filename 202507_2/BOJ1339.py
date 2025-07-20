# BOJ1339
# 단어 수학

from collections import defaultdict

N = int(input())

data = defaultdict(int)

for _ in range(N):
    word = input()
    len_word = len(word) 
    for idx in range(len_word):
        data[word[idx]] += 10 ** (len_word - idx - 1)

data = list(data.items())
data.sort(key=lambda x:x[1])

answer = 0

for idx in range(len(data)):
    answer += (10 - len(data) + idx) * data[idx][1]

print(answer)
