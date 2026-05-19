adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
replaced_adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(replaced_adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
replace_dots = replaced_adwentures_of_tom_sawer.replace('....', ' ')
print(replace_dots)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
replace_space = ' '.join(replace_dots.split())
print(replace_space)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = 0

for i in range(len(replace_space)):
    if replace_space[i] == 'h':
        count_h += 1
print(count_h)
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_isupper = 0

for i in range(len(replace_space)):
    if replace_space[i].isupper():
        count_isupper += 1
print(count_isupper)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
lst_adwentures_of_tom_sawer = replace_space.split()
count_tom = 0

for i in range(len(lst_adwentures_of_tom_sawer)):
    if lst_adwentures_of_tom_sawer[i] == 'Tom':
        count_tom += 1
        if count_tom == 2:
            print(i)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#replace_space = ' '.join(replace_dots.split())

lst_replace_space = replace_space.split('.')
adwentures_of_tom_sawer_sentences =  '.'.join(lst_replace_space)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
lst_adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_sentences.rstrip('.').split('.')
print((lst_adwentures_of_tom_sawer_sentences[3].strip()).lower())
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for i in range(len(lst_adwentures_of_tom_sawer_sentences)):
    if lst_adwentures_of_tom_sawer_sentences[i].find("By the time") >= 0:
        print(f'З "By the time" починається {i + 1} речення')


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = lst_adwentures_of_tom_sawer_sentences[-1].strip()
print(len(last_sentence.split()))