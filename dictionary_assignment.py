# GROUP DICTIONARY PROJECT
print('Welcome to our dictionary')
# Simnom Hai (NUPE)
nupe_dictionary = {
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
# Miriam Kwajaffa (BURA)
bura_dictionary = {

}
# List of languages
dictionaries = {'nupe': nupe_dictionary,
                'bura': bura_dictionary
                }
while True:
    language = input('Choose language (bura/nupe) or type exit to quit: ').lower()

    if language == 'exit':
        print('Goodbye')
        break

    if language in dictionaries:
        word = input('Enter an English word: ').lower()
        selected_dict = dictionaries[language]

        if word in selected_dict:
            print('The translation is:', selected_dict[word])
        else:
            print('Sorry, word not found in the', language, 'dictionary')
            print('Pls try again')
    else:
        print('Language not available, pls try again')
