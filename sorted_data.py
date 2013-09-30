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
    sorted_keys = sorted(scores_dictionary.keys())

    # printing alphabetized keys and values
    for key in sorted_keys:
        print "%s is rated at %s." % (key, scores_dictionary[key])


main()