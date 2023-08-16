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

[3. Spell checker using transformers for multiple incorrect words](https://github.com/arunima2407/Auto-correct/blob/main/multi_spell_check_transformers.ipynb) 
This is a continuation of the previous spell checker using transformers notebook, where I'm first searching for all occurances of misspelt words and converting them to the [MASK] token for the model to predict. I truncate the text to the first occurance of the masked token and use the substring to predict the sentence and recursively pass this new predicted sentence appending the words till the next masked token as the input till all the masked tokens are predicted.
While this solves problems better than the first 2 approach,

Cons:
 - It is unable to understand the grammar and allows any semantically correct word even though the word has no contribution to the meaning of the sentence.  

 
[4. Autopredict + Autocorrect](https://github.com/arunima2407/Auto-correct/blob/main/text-generation-autocorrect.ipynb)
I've built this notebook modifying on a text generation task using a Transformer decoder model. It works almost similar to the previous notebook, except the part where I mask tokens. Instead, I pass this truncated text to the model and predict the next word in sequence. I try to match the predicted word with the input sentence's misspelt word and corrects the sentence. This process continues till no misspelt words are there.
