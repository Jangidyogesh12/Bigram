import sqlite3
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt') # Download the necessary data for tokenization

con = sqlite3.connect("index_based_encoding.db")
cur = con.cursor()

path = "D:\Encoder\english.txt"

'''The index function return;s a dictionary with string as key
   and there (index + 1) as a value in a sorted way'''
def index(path):
    # Open the file in read mode ('r')
    with open(path,'+r', encoding = 'utf-8') as file:
        # Read the entire content of the file
        data = file.read()
        data = data.lower()
        new_data = data.replace('old_text', 'new_text')
        file.seek(0)
        file.write(new_data)
        file.truncate()
    # Now, 'data' contains the entire content of the file

    #Now spliting the data in to the tokens
    split_data = word_tokenize(data)
    s = set()
    for i in split_data:
        s.add(i)

    # sorting the data
    sorted_list = sorted(s)

    #Creating a dictionary
    dict = {}
    for i, d in enumerate(sorted_list):
        dict[d] = i+1;

    return dict


dict = index(path)
'''the text_split function split the text into the diffetent and group
   them into different chucks according to the cunk size'''

def text_split(text, chunk_size):
    tokens = word_tokenize(text)
    l = []
    sub_l = []
    for i in tokens:
        if((chunk_size - len(sub_l))>0):
            sub_l.append(i)
        else:
            l.append(sub_l)
            sub_l = [i]
    if(sub_l):
        if(len(sub_l)<chunk_size):
            for i in range(chunk_size-len(sub_l)):
                sub_l.append(0)
            l.append(sub_l)
    return l


text = "a lovely river called nallar flows through the chambal forest. there was a fox named kullan. the"
tokens = text_split(text, 10)
vector_embeding = [] 

for token in tokens:
    sub_vectors = []
    for word in token:
        if(word != 0 ):
            sub_vectors.append(dict[word])
        else:
            sub_vectors.append(0)
    vector_embeding.append(sub_vectors)

print(vector_embeding)