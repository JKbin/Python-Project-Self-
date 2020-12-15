kor = ["사과","바나나","오렌지"]
eng = ["apple","banana","orange"]

a = (list(zip(kor,eng)))

print(a)

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

a = (list(zip(*mixed)))

print(a)


