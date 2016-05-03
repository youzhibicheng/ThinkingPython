def shorten(string_list):
    length = len(string_list[0])
    for s in string_list:
        length = yield s[:length]

mystringlist = ['loremipsum', 'dolorsit', 'ametfoobor']
shortstringlist = shorten(mystringlist)

result = []
try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        filter_result = filter(lambda letter: letter in 'aeiou', s)
        number_of_vowels = len(filter(lambda letter: letter in 'aeiou', s))
        s = shortstringlist.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass