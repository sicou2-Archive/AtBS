import re

text = [
    '     howdy my name is the navitron    ',
    'howdy my name is the navitron    ',
    '     howdy my name is the navitron',
    '   ojwej   '
    '',
]

# stripped_text = []

# for sentence in text:
#     if not sentence:
#         stripped_text.append(sentence)
#     elif sentence:
#         mo1 = multi_word_strip.search(sentence)
#         if not mo1:
#             mo2 = single_word_strip.search(sentence)
#             stripped_text.append(mo2.group())
#         else:
#             stripped_text.append(mo1.group())

# print(stripped_text)


def stripper(text, chars=''):

    multi_word_strip = re.compile(r'(\w+\s)+(\w+)')
    single_word_strip = re.compile(r'(\w+)')

    stripped_text = []
    if not chars:
        for sentence in text:
            if not sentence:
                stripped_text.append(sentence)
            elif sentence:
                mo1 = multi_word_strip.search(sentence)
                if not mo1:
                    mo2 = single_word_strip.search(sentence)
                    stripped_text.append(mo2.group())
                else:
                    stripped_text.append(mo1.group())
        print(stripped_text)




stripper(text)
