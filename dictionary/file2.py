'''
Finds the average rating for each movie, and
Returns the movie with the highest average rating.
'''

movies = [
    {
        "title": "Inception",
        "reviews": [
            {"reviewer": "Alice", "rating": 9},
            {"reviewer": "Bob", "rating": 8},
            {"reviewer": "Charlie", "rating": 10}
        ]
    },
    {
        "title": "Interstellar",
        "reviews": [
            {"reviewer": "Alice", "rating": 10},
            {"reviewer": "Bob", "rating": 9}
        ]
    },
    {
        "title": "Tenet",
        "reviews": [
            {"reviewer": "Charlie", "rating": 7}
        ]
    }
]

avarage_rating = {}
highest_movie = movies[0]["title"]

for i in movies:
    ava = 0
    sum = 0
    for j in i["reviews"]:
        sum += j["rating"]
    ava = sum / len(i["reviews"])
    avarage_rating.update({ i["title"]: round(ava)})

high = 0
for i in avarage_rating:
    if (high < avarage_rating[i]):
        high = avarage_rating[i]
        highest_movie = i


print("Avarage Rating of each movie")
print(avarage_rating, "\n")
print("Highest Movie Rating Name : ", highest_movie)