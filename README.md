# Auto Correct

Hey there!
I'm working on the autocorrect feature and tried a [notebook](https://github.com/arunima2407/Auto-correct/blob/main/spell-checker.ipynb) where I used a [dictionary](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) which contains over 300k english words. I tried using levenshtein and jaccard distance to check if my notebook can give me accurate predictions for misspelt words in my sentences.

While they give me moderately accurate results, I see the major cons:
- Jaccard distance works relatively better than levenshtein as it computes on ngrams for each word.
- Results are not very accurate on the basis of context in both cases. For example, if my correct sentence is "I ate an apple", with a misspelt version of the word 'apple', the predictions by the code is 'ape', 'aple', 'apes' etc. which carry no meaning to the input sentence.
   
 


### Way forward
I'm working on using pretrained embeddings to address this issue.

