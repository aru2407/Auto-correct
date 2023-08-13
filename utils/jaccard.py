from nltk.util import ngrams
from nltk.metrics.distance import edit_distance, jaccard_distance
import itertools

def jaccard(sentence,dictionary):
    similar_word = {}
    tmp_words = []
    distance = []
    wrong = 0   
    
    print("\n\nInput text: ",sentence)
    print("Predictions:")
    for words in sentence.split():
        words = words.lower()


        for i in dictionary:
            if str(i[0]) == words[0]:
                tmp_words.append(i)
                #print(tmp_words)
        for tmp_word in tmp_words:
            if len(words) < 3:
                ngram_length = len(words)
            else:
                ngram_length = 3
            distance = jaccard_distance(set(ngrams(words,ngram_length)),set(ngrams(tmp_word,ngram_length)))
            
            similar_word[tmp_word] = distance
        similar_word = dict(sorted(similar_word.items(), key=lambda x:x[1]))
        for i in similar_word.values():
            if i == 0.0:
                #new_sentence.append(words)
                wrong = 0
                break
            else:
                wrong = 1
        if wrong == 1:
            print("\nThe word ", words, " is wrong. Did you try to mean: ")
            predictions = dict(itertools.islice(similar_word.items(), 7))
            for i in predictions:
                print(i," : ",predictions[i])