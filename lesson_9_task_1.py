def popular_words (text: str, words: list[str]):
    split_text = text.casefold().split()
    dict_of_usage = {}

    for item in words:
        count = split_text.count(item)
        dict_of_usage.update({item: count})

    return dict_of_usage


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')