'''
я еще думал обрабатывать строку, через экранирование в список, но решил,
что это будет больше нагружать комп в случае обьемной программы
'''
def correct_sentence(text: str):
    result = ''
    if text[0].islower():
        result += text[0].capitalize() + text[1:]
    else:
        result = text

    if text[-1] != '.':
        result += '.'
    return result


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

# print(correct_sentence("Greetings. Friends"))
