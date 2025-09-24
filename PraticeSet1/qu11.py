# count each vowel

def count(str):
    result = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    for i in ["a", "e", "i", "o", "u"]:
        count = 0
        for j in str:
            if j.lower() == i:
                count += 1
        result[i] = count

    print(result)

str = input("Enter String : ")
count(str)