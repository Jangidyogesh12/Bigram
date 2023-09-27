#This programs gives you the top n similar items from the words

words = open(r"D:\Encoder\names.txt").read().splitlines()

lst_of_bigram = [] #List of consecutive pair 
dict_word_count = {} #Dictionary to keep record of the Bigram count
unigram = {} 

''' Here <S> stands for the start of the character andf
    <E> stands for the end of the character'''
def create_bigram(words):
    for word in words:
        word = ['<S>'] + list(word) + ['<E>']
        for ch1, ch2 in zip(word,word[1:]): 
            lst_of_bigram.append((ch1,ch2))
            #counting the Bigrams
            if (ch1,ch2) in dict_word_count:
                dict_word_count[(ch1, ch2)] += 1
            else:
                dict_word_count[(ch1,ch2)] = 1

        #counting the Unigrams
        for i in word:
            if(i in unigram):
                unigram[i] += 1
            else:
                unigram[i] = 1
    return lst_of_bigram, dict_word_count, unigram

# Calculating the probabilities
lst_of_bigram, dict_word_count, unigram = create_bigram(words)
def calc_prob(lst_of_bigram):
    dict_prob = {}
    for i in lst_of_bigram:
        word1 = i[0]
        word2 = i[1]
        dict_prob[i] = dict_word_count.get(i)/unigram.get(word1)
    return dict_prob

#Getting the most likely element to come after char
def most_likely(char, prob_dict, n_similar_items):
    similar_dict = {}
    n = 0
    for i in prob_dict.items():
        word1 = i[0][0]
        word2 = i[0][1]
        if (word1 == char and word2!='<E>'):
            similar_dict[(word1, word2)] = i[1]
            n += 1
            if n >= n_similar_items:
                break
    return sorted(similar_dict.items(), key=lambda ks: ks[1], reverse=True)


x = calc_prob(lst_of_bigram)
print(most_likely('e', x, 5))


