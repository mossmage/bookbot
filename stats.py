def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        char_dict[lower_char] = char_dict.get(lower_char, 0) + 1
    return char_dict

def sort_on(item):
    return item["num"]

def sort_char(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({
            "char": char,
            "num": count,
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
