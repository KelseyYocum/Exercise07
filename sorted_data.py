from sys import argv
script, filename = argv

# opening and reading the file. Splitting on the line breaks
lines = open(filename).read().split('\n')

# creating a list of lists, splitting on the colon.
scores_list = []
for i in lines:
    scores_list.append(i.split(":"))

# creating a dictionary out of the list of lists
scores_dictionary = dict(scores_list)

# alphabetizing dictionary keys
sorted_keys = sorted(scores_dictionary.keys())

# printing alphabetized keys and values
for key in sorted_keys:
    print "%s is rated at %s." % (key, scores_dictionary[key])


