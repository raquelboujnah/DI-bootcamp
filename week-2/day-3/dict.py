#print the price of the fruit the user choose
prices = {
    "appla" : 2,
    "banana" : 5,
    "orange" : 1
}

#user_fruit = input("choose a fruit")
#print(prices[user_fruit])

#create a new list that only contains the uppercased words
words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
new_list = [ x for x in words if x.isupper()]
# print(new_list)



#Print the total duration of the playlist

playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}
total = 0
for music in playlist['songs']:
    total += music["duration"]
print(total)

