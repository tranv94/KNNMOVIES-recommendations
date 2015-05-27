from collections import defaultdict


# parses each line in data.txt and ignoring white space
def movieData():
    return [line.strip().split(' ') for line in open('data.txt', 'rU') if not line.isspace()]


def manhattanDistance(user1, user2):
    distance = -1
    for movie in user1:
        if movie in user2:
            distance = distance + 1
            distance = abs(int(user1[movie]) - int(user2[movie]))
    return distance


def nearest(userX):
    distances = []
    global userList
    for user in userList:
        if user is not userX:
            distance = manhattanDistance(userList[user], userX)
            if distance > 1:
                distances.append((distance, user))
    distances.sort()
    return distances


def recommender(userX):
    global userList
    limit = 5
    closest = nearest(userX)
    recommendations = []
    for movie in closest:
        if movie not in userX and limit != 1:
            recommendations.append(userList[movie[1]])
            limit = limit - 1
    return recommendations


def Deviations(userList):
    global frequencies, deviations
    for movies in userList.values():
        for movieTitle, movieRating in movies.iteritems():
            frequencies.update({movieTitle: movieRating})
            deviations.update({movieTitle: movieRating})
            for movieTitle2, movieRating2 in movies.iteritems():
                if movieTitle is not movieTitle2:
                    frequencies[movieTitle].setdefault(movieTitle2, 0)
                    deviations[movieTitle].setdefault(movieTitle2, 0.0)
                    frequencies[movieTitle][movieTitle2] += 1
                    deviations[movieTitle][movieTitle2] += movieRating - movieTitle2
    for (movie, rating) in deviations.iteritems():
        frequencies[movie] = int(frequencies[movie])/int(deviations[movie])

userList = defaultdict(list)
movieAndRating = {}
frequencies = {}
deviations = {}

# creates user object that stores a dictionary for each movie they rate
# and what they rate as {userID: {movie : rating}}
for k in movieData():
    userList.update({k[0]: {k[2]: k[3]}})

# print recommendation for user in userList
# print recommender(userList['1056'])
print Deviations(userList)
