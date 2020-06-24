import re

text = [
    '    howdy my name is the navitron    ',
    'howdy my name is the navitron    ',
    '    howdy my name is the navitron',
    '    howdy',
    'howdy   ',
    '    howdy    ',
    '    ',
    'howdy my name is the navitron howdy',
    'howdymy name is the navitronhowdy',
    'howdy my name is the navitron',
    'my name is the navitron howdy',
    '',
]


def stripper(text, chars=' '):

    f_multi_regex = f''

    stripped_text = []
    multi_word_strip = re.compile(rf'[^{chars}](\w+\s)+(\w+)([^{chars}])')
    single_word_strip = re.compile(rf'[^{chars}](\w+)[^{chars}]')

    for sentence in text:
        if not sentence:
            stripped_text.append(None)
        elif sentence:
            mo1 = multi_word_strip.search(sentence)
            if not mo1:
                mo2 = single_word_strip.search(sentence)
                if not mo2:
                    stripped_text.append(None)
                else:
                    stripped_text.append(mo2.group())
            else:
                stripped_text.append(mo1.group())
    print(stripped_text)


stripper(text)

stripper(text, 'howdy ')

print('   howdy my name is  navitron howdy    '.strip('howdy'))
