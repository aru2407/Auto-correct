# Auto Correct

Hey there!
I'm working on the autocorrect feature and worked with a [dictionary dataset](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) which contains over 300k english words. 

[1. Spell checker using jaccard and levenshtein distance](https://github.com/arunima2407/Auto-correct/blob/main/spell-checker.ipynb)
I tried using both levenshtein and jaccard distance to study the comparison between the two methods for accurate predictions for misspelt words in my sentences.
Cons:
- Jaccard distance works relatively better than levenshtein as it computes on ngrams for each word.
- Results are not very accurate on the basis of context in both cases. For example, if my correct sentence is "I ate an apple", with a misspelt version of the word 'apple', the predictions by the code is 'ape', 'aple', 'apes' etc. which carry no meaning to the input sentence.
   
[2. Spell checker using transformers](https://github.com/arunima2407/Auto-correct/blob/main/spell_check_transformers.ipynb)
So, I tried a different approach using transformers making use of the fill-mask pipeline of the [bert-base-uncased model](https://huggingface.co/bert-base-uncased) to predict the incorrect word in my sentence (which I masked).
Cons:
- The major drawback of this method is that fill-mask works for exactly 1 [MASK] token, so it's absolutely useless if I have multiple misspelt words in my sentence.
- It overlooks the grammar in the sentence and is only bothered about the spelling. For example, if I have a sentence, wot gift did he apple her; the code finds no error in this sentence cause these are all valid words


 


### Way forward
Let me try with training a model with pretrained embeddings. Will be back soon. 😉

