# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count("а"))

# Вывести количество гласных букв в слове


word = "Архангельск"
count = 0
for letter in word:
  if letter.lower() in "ауеёоэяиыю":
    count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(*(word[0] for word in sentence.split()), sep = "\n")


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(sum([len(word) for word in sentence])/len(sentence.split()))