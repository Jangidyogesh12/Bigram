# Term frequency ans Inverse data frequency
import math

data =  ["this is a good phone" , "this is a bad mobile" , "she is a good cat" , 
         "he has a bad temper" , "this mobile phone is not good"]

def create_corpus(data):
    data_corpus = []
    for i in data:
        for j in i.split():
            if(j not in data_corpus):
                data_corpus.append(j)
    data_corpus.sort()
    return data_corpus

'''  

   The above function will create the list of all the words present in the data list 

   Data Corpus: [“a” , “bad” , “cat” , “good” , “has” , “he” , “is” , “mobile” , “not” , 

                 “phone” , “she” , “temper” , “this”]
                 
'''
data_corpus = create_corpus(data)



# Fuction to find the term frequency
def term_frequency(word, sentence):
    # sentence is the sentence whose embeding is to be done
    len_sentence = len(sentence.split())
    occurence = 0

    for i in sentence.split():
        if(word==i):
            occurence += 1;
    
    tf = occurence/len_sentence

    return tf




'''
   finding the inverse data frequency of the data 
   
   where the data is the data list mentioned above

'''

def inverese_data_frequency(data, word):
    corpus = create_corpus(data)
    N = len(corpus) # Total number of words in the whole data corpus 
    df = 0          # The total number of sentences containing the current word
    for i in data:
        if(word in i.split()):
            df += 1;
    idf = math.log(N/df)
    return idf



a = 'this is a good phone'

def embeding(sentence, data, data_corpus = data_corpus):
    dict = {}
    for i in sentence.split():
        tf_idf = term_frequency(i ,sentence) * inverese_data_frequency(data, i)
        dict[i] = tf_idf
    
    vector = [0]*len(data_corpus)
    for i in range(len(data_corpus)):
        if(data_corpus[i] in sentence):
            vector[i] = dict[data_corpus[i]]
    return vector



a = embeding(a, data) 
print(a)



