from random import randint
from time import time

# Part 1
# A) Define a function retrieve_words
def retrieve_words(text_file):
    with open(text_file, 'r') as f:
        ordered_words = []
        for line in f:
            line = line.strip()
            ordered_words.append(line)

        return ordered_words

# B) Define a function determine_top_prefixes
def sort_prefix_by(one_prefix):
    if len(one_prefix.keys()) != 1:
        print "input argument does not have exactly 1 key!"
        return

    one_key = one_prefix.keys()[0]              # from list of dictionary keys, set 1st element equal to one_key
    one_value = one_prefix[one_key]             # get the value of the one_key

    return one_value                            # sort by value of the dictionary

def determine_top_prefixes(ordered_words, prefix_length, num_prefixes):
    total_prefixes_list = [word[:prefix_length] for word in ordered_words if len(word) >= prefix_length]
    unique_prefixes = []
    for prefix in total_prefixes_list:
        if prefix in unique_prefixes:
            continue
        unique_prefixes.append(prefix)


    # prefix_to_count = [prefix: prefixes_list.count(prefix)for prefix in unique_prefixes]
    prefix_to_count = []
    for prefix in unique_prefixes:
        dictionary = {}
        dictionary[prefix] = total_prefixes_list.count(prefix)
        prefix_to_count.append(dictionary)
    # sorted[iterable_list, key= to sort by, reverse= FALSE for ascending sort)
    sorted_prefixes_count = sorted(prefix_to_count, key=sort_prefix_by, reverse = True)
    # for the prefixes in positions 0 to 9 in sorted_prefixes_count
    top_X_prefixes = [prefix_to_count.keys()[0] for prefix_to_count in sorted_prefixes_count[:num_prefixes]]
    return top_X_prefixes


    # 10% extra credit: count_to_prefixes
    count_to_prefixes = {}
    for prefix in unique_prefixes:
        counter = total_prefixes_list.count(prefix)
        dict_keys = count_to_prefixes.keys()
        if counter in dict_keys:
            count_to_prefixes[counter].extend([prefix])
        else:
            count_to_prefixes[counter] = [prefix]
    sorted_count = sorted(count_to_prefixes.keys())
    reversed_count = list(reversed(sorted_count))
    # return 10 ten most common prefixes:
    position = -1
    top_X_count = []
    while len(top_X_count) < num_prefixes:
        for key in count_to_prefixes:
            top_X_count.extend(count_to_prefixes.values()[position])
            position -= 1
    # return top_10_count[:num_prefixes]

# C) define a function retrieve_words_with_prefix:
def retrieve_words_with_prefix(ordered_words, chosen_prefix):
    chosen_pre_length = len(chosen_prefix)
    list_of_words_with_prefix = [word for word in ordered_words if (word[: chosen_pre_length] == chosen_prefix)]
    return list_of_words_with_prefix


# Project Part 2:
def calculate_points(user_input, list_of_words_with_prefix, user_words):
    if user_input in list_of_words_with_prefix:
        if user_input not in user_words:
            points_earned = len(user_input)
            user_words.add(user_input)
            return points_earned, user_words
        else:
            print "You've already input this word. You can only input a word once."
            points_earned = 0
            return points_earned, user_words
    else:
        print "{0} is not in my dictionary. Sorry!" .format(user_input)
        points_earned = 0
        return points_earned, user_words


def retrieve_prefix(top_X_prefixes):
    max_num = len(top_X_prefixes) - 1
    min_num = 0
    random_index = randint(min_num,max_num)
    return top_X_prefixes[random_index]

def game_round(chosen_prefix, possible_words, user_words, round_time):
    start_time = time()
    round_points = 0
    while True:
        user_input = raw_input('What word with the prefix   < {0} >   would you like to enter: '.format(chosen_prefix))
        now_time = time()
        if (now_time - start_time) > round_time:
            break
        points_earned, user_input = calculate_points(user_input, possible_words, user_words)
        round_points += points_earned
        remaining_time = round_time - (now_time - start_time)
        print points_earned, "points earned.   You have {0} seconds left.".format(remaining_time)

        print ""
    print 'TIME HAS RUN OUT!'
    return round_points, user_words

def game_implementation(ordered_words,prefix_length, num_prefixes):
    round_time = 15
    user_words = set()
    prefix_letters = prefix_length
    total_points = 0
    top_X_prefixes = determine_top_prefixes(ordered_words, prefix_length, num_prefixes)
    chosen_prefix = retrieve_prefix(top_X_prefixes)
    while len(chosen_prefix) > 0:
        list_of_words_with_prefix = retrieve_words_with_prefix(ordered_words, chosen_prefix)
        print ""
        print ""
        print "You have {0} seconds to complete this round".format(round_time)
        round_points, user_words = game_round(chosen_prefix, list_of_words_with_prefix,user_words,round_time)
        print "Points earned this round: ", round_points
        total_points += round_points
        prefix_letters -= 1
        chosen_prefix = chosen_prefix[:prefix_letters]
    return total_points, user_words


def main():
    text_file ='wordlist10000mit.txt'
    ordered_words = retrieve_words(text_file)

    prefix_length = 3
    num_prefixes = 10
    total_points, user_words = game_implementation(ordered_words, prefix_length, num_prefixes)
    print ""
    print "Your game total is: ", total_points
    print "You entered the following words: ", user_words


main()