# build a analize of marks with the dictionary

myObj = {
    "Rohit": [60, 56, 87],
    "Saptorshi": [66, 76, 56],
    "Souvik": [78, 56, 59],
    "Rupom": [45, 99, 87],
    "Saptorshi": [56, 34, 86],
    "Choyan": [86, 64, 43]
}

total_marks = {}
avarage_marks = {}

for i in myObj:
    total = 0
    ava = 0
    for j in myObj[i]:
        total += j
    ava = total // len(myObj[i])
    total_marks.update({ i: total})
    avarage_marks.update({ i: ava})

print("Total Marks of Stidents---")
print(total_marks)
print("Avarage Marks of Students----")
print(avarage_marks)