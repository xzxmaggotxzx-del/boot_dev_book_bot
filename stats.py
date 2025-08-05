def count_words(text):
    text_list = text.split()
    return len(text_list)

def count_symbols(text):
    symbols_dict = {}
    text_lower = text.lower()

    for symbol in text_lower:
        if symbol not in symbols_dict:
            symbols_dict[symbol] = 1
        else:
            symbols_dict[symbol] += 1
    
    return symbols_dict

def sort_on(items):
    return items["num"]

def sort_symbols(symbols_dict):
    symbols_kvp = []

    for key in symbols_dict:
        kvp = {}
        kvp["char"] = key
        kvp["num"] = symbols_dict[key]
        symbols_kvp.append(kvp)
    
    symbols_kvp.sort(reverse=True, key=sort_on)
    return symbols_kvp
    