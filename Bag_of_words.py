data =  ["this is a good phone" , "this is a bad mobile" , "she is a good cat" , "he has a bad temper" , "this mobile phone is not good"]

'''Function to create the data corpus'''
def create_corpus(data):
    data_corpus = []
    for i in data:
        for j in i.split():
            if(j not in data_corpus):
                data_corpus.append(j)     
    data_corpus.sort()
    return data_corpus
   
data_corpus = create_corpus(data)

data1 = "this is a good phone"
def tokenise(data):
    data = data.split()
    return data

# Binary Bag of Words
tokenise_data1 = tokenise(data1)
def binary_embeding(tokenise_data , data_corpus = data_corpus):
    vector = [0]*len(data_corpus)
    for i  in range(len(data_corpus)):
        if(data_corpus[i] in tokenise_data):
            vector[i] = 1

    return vector

'''Traditional Bag of words in this the frequenct of 
   the word is taken in to account to create the vector'''

data2 = "this is a good mobile this is a good phone"
tokenise_data2 = tokenise(data2)
def embeding(tokenise_data , data_corpus = data_corpus):
    frequency_dict = {}
    for i in tokenise_data:
        if(i in frequency_dict.keys()):
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1

    vector = [0]*len(data_corpus)
    for i in range(len(data_corpus)):
        if(data_corpus[i] in data2):
            vector[i] = frequency_dict[data_corpus[i]]
    return vector


print(embeding(tokenise_data2))