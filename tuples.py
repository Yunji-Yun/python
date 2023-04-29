# 튜플(tuples)

tup = (1, 20, 40)
print(tup[0])

# 각각의 요소 값 변경 불가능 = 읽기 전용
# tup[0] = 100 안됨

# 아예 재할당하는 것은 가능
tup = (100, 30, 4)
print(tup)

for x in tup :
    print(x)

# 튜플 리스트 변환 1
tup = (1, 20, 40)

list_1 = list(tup)
print(list_1)

# 튜플 리스트 변환 2
list_2 = [x for x in tup] # 튜플 요소 하나하나 리스트에 담음
print(list_2)

# 튜플 리스트 변환 3

list_3 = []

for x in tup :
    list_3.append(x)

print(list_3)