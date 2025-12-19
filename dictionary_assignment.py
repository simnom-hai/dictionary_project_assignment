# hai_simnom NUPE DICTIONARY
print('Welcome to our dictionary')
dictionary = {
    'husband': 'eba',
    'basket': 'kansa',
    'know': 'kpe',
    'yam': 'eci',
    'red': 'dzuru',
    'blue': 'dofa',
    'wife': 'nyimi',
    'thanks': 'kubetun',
    'good': 'ebi',
    'father': 'dau',
    'house': 'wari',
    'green': 'korina',
    'tired': 'ebo',
    'hungry': 'mada',
    'female': 'iyoro',
    'relative': 'yegi',
    'hello': 'yegi',
    'cough': 'ekpa',
    'blind': 'yebonci',
    'yellow': 'yaran',
}
word = input('Enter an English word: ').lower()
if word in dictionary:
    print('Translation:', dictionary[word])
else:
    print('Sorry, word not found')
