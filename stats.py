def word_count(text_str):
     wordcount = 0
     for word in text_str.split():
        wordcount += 1
     return wordcount
def char_count(text_str):
    lower_case = text_str.lower()
    count_dict = {}
    for entry in lower_case:
        if entry in count_dict:
            count_dict[entry] += 1
        else:
            count_dict[entry] = 1
    return count_dict
def sort_on(dict):
    return dict["num"]
def dict_sort_list(unsorted_dict):
    unsorted_list = []
    for entry in unsorted_dict:
        new_dict = {}
        new_dict["char"] = entry
        new_dict["num"] = unsorted_dict[entry]
        unsorted_list.append(new_dict)
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list
def char_num(text_str):
    lower_case = text_str.lower()
    charnum = len(lower_case)
    return charnum