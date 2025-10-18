amount = int(input("enter amount"))

notes500 = amount // 500
amount %= 500
notes200 = amount//200
amount %= 200
notes100 = amount//100
amount %=100
notes50 = amount//50
amount %=50
notes20 = amount//20
amount %=20
notes10 = amount//10
amount %=10


print("notes of 500",notes500)
print("notes of 200",notes200)
print("notes of 100",notes100)
print("notes of 50",notes50)
print("notes of 20",notes20)
print("notes of 10",notes10)