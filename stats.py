def get_num_words(text_to_count_words_in:str):
    total_words_list = text_to_count_words_in.split() # returns a list of the words in the string
    number_of_words = len(total_words_list) #each step in separate line for educational purposes
    return number_of_words

def summary_of_chars_dict(text_to_count_in:str):
    char_summary= {} #dictionary declaration
    for char in text_to_count_in:
        char = char.lower()
        if char in char_summary:
            char_summary[char] += 1
        else:
            char_summary[char] = 1
    return char_summary #returns a dictionary

def sort_on(item):
        return item[1] # sort on second element

def sorting_dictionary(dict_to_sort):
    
    my_dict = dict_to_sort

    #print("------------First method of sorting with lambda--------------")
    #sorted1list = (sorted(my_dict.items(), key=lambda item: item[1]))
    #print(sorted1list)
    #print("-------------Should be the same with recall function and no lambda---------------")
    #sorted2list = (sorted(my_dict.items(), key=sort_on))
    #print(sorted2list)

    sorted_list = sorted(my_dict.items(), key=sort_on, reverse = True)
    dict_list = [{"char": ch, "num": num} for ch, num in sorted_list]

    #sorted list is a list of tuples sorted by number
    #dict_list is a list of dictionaries

       
          
    return dict_list
