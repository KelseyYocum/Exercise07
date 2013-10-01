from sys import argv
script, filename = argv

def main():
    # opening and reading the file. Splitting on the line breaks
    lines = open(filename).readlines()

    # creating a list of lists, splitting on the colon.
    scores_list = []
    for line in lines:
        line = line.strip()
        scores_list.append(line.split(":"))

    # creating a dictionary out of the list of lists
    scores_dictionary = dict(scores_list)

    # alphabetizing dictionary keys
    sorted_restaurants = sorted(scores_dictionary.keys())
    for key in sorted_restaurants:
        print "%s is rated at %s." % (key, scores_dictionary[key])

    # creating a dictionary organized by rating
    ratings_dictionary = {}
    for restaurant, rating in scores_dictionary.iteritems():
        if ratings_dictionary.has_key(rating):
            ratings_dictionary[rating].append(restaurant)
        else:
            ratings_dictionary.setdefault(rating, [restaurant])

    # printing 
    sorted_ratings = sorted(ratings_dictionary.keys())
    sorted_ratings.reverse()

    for rating in sorted_ratings:
        print "Restaurants that got a score of %s:" % (rating)
        for restaurant_name in ratings_dictionary[rating]:
            print restaurant_name
       


main()