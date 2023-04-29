# 리스트(lists) - 여러 개의 데이터를 하나의 변수에 담을 수 있음

mbti = ['INFP', 'ENFP', 'ISTJ', 'ESTP']

print(mbti)
print(mbti[0])

mbti[0] = 'INFJ' # 0번째 데이터 변경

print(mbti)
print(mbti[0])

my_list = [123, 'apple'] # 다양한 데이터 타입 가능
print(mbti)

colors = ['red', 'blue', 'green']

# 수정
colors[2] = 'black'
print(colors)

# 추가 1
colors.append('purple') # append 함수는 맨 마지막에 데이터 추가
print(colors)

# 추가 2
colors.insert(1, 'yellow') # insert 함수는 원하는 인덱스에 데이터 추가
print(colors)

# 제거 1
del(colors[0]) # del 함수는 원하는 인덱스의 데이터 삭제
print(colors)

# 제거 2
color = colors.pop(0) # pop 함수는 데이터 삭제와 동시에 반환
print(colors)
print(color)

# 제거 3
colors.remove('blue') # remove 함수는 지정한 데이터 삭제
print(colors)

# 리스트 정렬

colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# 정렬 1
colors.sort() # 알파벳 순으로 정렬하여 원래 리스트에 저장
print(colors)

'''
colors.sort(reverse=True) # 정렬한 데이터 역순으로 저장
print(colors)
'''

# 정렬 2
print(sorted(colors)) # 정렬하지만 원래 리스트는 변하지 않음

# 길이 - 요소의 개수
print(len(colors))

# print(colors[7]) 존재하지 않는 인덱스의 값을 읽으려고 하면 에러남
print(colors[-1]) # 역순으로 인덱스를 읽을 것

# 리스트 슬라이싱

colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

colors_2 = colors[:] # colors_2 = colors 의 경우 데이터의 왜곡 발생할 수 있음(한 리스트 수정 시 같이 수정됨)

print(colors_2)
print(colors[1:5]) # [시작값:끝값+1]
print(colors[:4]) # 맨 처음부터
print(colors[2:]) # 맨 끝까지

print(colors[-5:]) # -5부터 마지막까지

# 리스트 흐름 제어

scores = [88, 100, 96, 43, 65, 78]
scores.sort()
scores.sort(reverse=True) # 내림차순 정렬
print(scores)

for score in scores: # 스코어스 리스트의 값 순서대로 입력
    if score >= 80 :
        print(score)
    else :
        print('Fail')

# 리스트의 최댓값, 최솟값, 총합

scores = [88, 100, 96, 43, 65, 78]

max_val = max(scores) # 최댓값
min_val = min(scores) # 최솟값
sum_val = sum(scores) # 총합
print(sum_val)
'''
sum_value = 0
for score in scores :
    sum_value = sum_value + score
print(sum_value)
'''
avg_val = sum(scores) / len(scores) # 평균
















