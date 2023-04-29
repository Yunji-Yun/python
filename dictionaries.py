# 딕셔너리(Dictionaries)

student = {
    "student_no": "20220823",
    "major": "computer engineering",
    "grade": 2
}
'''
print(student["student_no"])

student["student_no"] = "20231234" # 데이터 변경
print(student)
print(student["student_no"])
'''

# 추가
student["age"] = 20
print(student)

# 수정
student["age"] = 21
print(student)

# 삭제
del student["grade"]
print(student)

# 데이터 접근
print(student.get("major"))

# 존재하지 않는 데이터에 접근할 때(None 출력 대체)
print(student.get("grade", "해당 키-값 쌍이 없습니다."))

# 딕셔너리의 키를 반환
print(student.keys()) # dict_keys([~~~])
print(list(student.keys())) # [~~~]

# 딕셔너리의 값을 반환
print(student.values()) # dict_values([~~~])
print(list(student.values())) # [~~~]

#딕셔너리와 반복문

tech = {
    "HTML": "Advanced",
    "JavaScript": "Intermediate",
    "Python": "Expert",
    "Go": "Novice"
}

for key, value in tech.items():
    print(f'{key} - {value}')

'''
for i in tech:
    print(i)
키 값만 출력
'''
for key in tech.keys():
    print(key)

for value in tech.values():
    print(value)

# 중첩(Nesting)

# 리스트 안에 딕셔너리
student_1 ={
    "student_no": 1,
    "gpa": "4.3"
}
student_2 ={
    "student_no": 2,
    "gpa": "3.8"
}

students = [student_1, student_2]

for student in students:
    print(student['student_no'])

for student in students:
    student['grauated'] = False
    print(student)

# 딕셔너리 안에 리스트
student = {
    "subject": ["파이썬", "인터넷기초"]
}

print(student["subject"])

subjects_list = student["subjects"]

for subject in subjects_list :
    print(subject)

# 딕셔너리 안에 딕셔너리

student = {
    "scholarship": {
        "name": "국가장학금",
        "acount": "1000000"
    }
}

print(student)

for key in student.keys():
    print(key)

for value in student.values():
    for value_2  in value.values:
        print(value_2)