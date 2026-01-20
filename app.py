import streamlit as st

st.title('English To Foreign Language Dictionary')
st.write('Choose a Language and enter an English word to get a translation in Bura or Nupe')
#Lanaguage Selection
language = st.selectbox(
    'Choose a Language',
#the languages are stored in a tuple below because it is a fixed list of options
    ('Bura', 'Nupe')
)
#SIMNOM HAI
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
#MIRIAM KWAJAFFA
bura_dictionary = {
    'husband': 'biyi',
    'basket': 'makha',
    'know': 'gi',
    'yam': 'hir',
    'red': 'nuyi',
    'blue': 'dere',
    'wife': 'ritki',
    'thanks': 'godo',
    'good': 'kici',
    'father': 'lau',
    'house': 'wura',
    'green': 'sarata',
    'tired': 'ibe',
    'hungry': 'kirba',
    'female': 'dawa',
    'relative': 'gimi',
    'hello': 'bado',
    'cough': 'rimda',
    'blind': 'baha',
    'yellow': 'palam',

}
#Input box, whatever the user types is stored in 'word'
word = st.text_input('Enter an English word').lower()
#the first if statement, means the code will only run if the 'translate' button is clicked
if st.button('Translate'):
    if language == 'Nupe':
        dictionary = nupe_dictionary
    else:
        dictionary = bura_dictionary

    if word in dictionary:
#f-string, it allows you insert variables into text
        st.success(f'Translation ({language}): {dictionary[word]}')
    else:
        st.error('Sorry, the word is not in the dictionary')