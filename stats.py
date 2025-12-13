def get_num_words(text):
    words = text.split()
    return len(words)

def get_ch_num(text):
    ch_count = {}
    for ch in text:
        ch = ch.lower()
        ch_count[ch] = ch_count.get(ch, 0) + 1
    return ch_count

def sort_on(d):
    return d["num"]

def chars_dictsorted(num_char_dict):
    sorted_list = []
    for ch in num_char_dict:
        sorted_list.append({"char": ch, "num": num_char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
