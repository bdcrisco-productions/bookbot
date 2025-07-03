def get_word_count(file_to_parse):
    word_count = len(file_to_parse.split())
    return word_count

def get_character_appearance_count(text):
    character_count = {}
    for word in text.split():
        for character in word:
            if character.lower() not in character_count.keys():
                character_count[character.lower()] = 0
            character_count[character.lower()] += 1

    return character_count

def sort_character_count(count_dict):
    sorted_dict = {}
    for key in sorted(count_dict, key=count_dict.get, reverse=True):
        sorted_dict[key] = count_dict[key]

    return sorted_dict