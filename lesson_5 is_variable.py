import string
import keyword


edited_str_punkt = string.punctuation.replace("_", " ")
# я удалил символ "_" из стандартного списка знаков пунктуации

result = True

word = input("type the word: ")

if word.isdigit() or word[0].isdigit():
    #я думаю, что достаточно было просто проверить,что слово начинается с цифры,
    #но, рас сказано проверить на "все цифры", значит проверим)))

    result = False
elif word in keyword.kwlist:

    result = False

for char in word:
    if char in edited_str_punkt or char.isupper():
        result = False
    elif char.isupper():
        result = False

print(result)