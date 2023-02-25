#
# # libraries
#

import spacy # imports spacy module to be used in program


#
# # global variable
#

nlp_sm = spacy.load('en_core_web_sm') # loads sm model into a variable
nlp_md = spacy.load('en_core_web_md') # loads md model into a variable

words = ['cat', 'monkey', 'banana'] # list of words to be compared
words_sm = []
words_md = []


#
# # main
#

# generates a list of tokens using web_sm
for x in words:
    words_sm.append(nlp_sm(x))


# generates a list of tokens using web_md
for x in words:
    words_md.append(nlp_md(x))


# compares each word / token using the sm model, outputs to user which words have been compared and what their values are
print('Comparison using sm or Small Model - en_core_web_sm')
for x in words_sm:
    for y in words_sm:
        similarity = x.similarity(y)
        print(f'{x} compared to {y} = {similarity}')
print(f'\n\n')


# attempting to use the web_sm model to compare words gives the below error / output, sm doesn't contain vectors
# confirmed the difference between the models on spacy's documentation, sm/md is advised for development and lg for production, main differences are statistical with larger models being more accurate
# https://spacy.io/models/en
# https://stackoverflow.com/questions/50487495/what-is-difference-between-en-core-web-sm-en-core-web-mdand-en-core-web-lg-mod
# # error / output
# The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be 
# based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if 
# you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only 
# use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.


# compares each word / token using the sm model, outputs to user which words have been compared and what their values are
print('Comparison using md or Medium Model - en_core_web_md')
for x in words_md:
    for y in words_md:
        similarity = x.similarity(y)
        print(f'{x} compared to {y} = {similarity}')
print(f'\n\n')


# attempted to run below loops to see if models could be compared at any point, both errored
# I expected the sm comparison to md to fail as it doesn't ship with vectors
# wasn't sure about md compared to sm but this also errored

# for x in words_sm:
#     for y in words_md:
#         similarity = x.similarity(y)
#         print(similarity)

# for x in words_md:
#     for y in words_sm:
#         similarity = x.similarity(y)
#         print(similarity)



# # comments on word similarity, new word comparison
# it looks like the model will give a higher similarity between monkeys and fruit as they can be associated with eating them, where as cats don't typically eat fruit

words = ['adult', 'child', 'father', 'mother', 'son', 'daughter', 'driving', 'school', 'university', 'nursery'] # new list of words to compair
words_md = [] # clears the list as append() is used


# generates a list of tokens using web_md, since vectors aren't packaged with web_sm I won't be using it
for x in words:
    words_md.append(nlp_md(x))


# compares each word / token using the sm model, outputs to user which words have been compared and what their values are
print('Comparison using md or Medium Model - en_core_web_md')
for x in words_md:
    for y in words_md:
        similarity = x.similarity(y)
        print(f'{x} compared to {y} = {similarity}')

# choose to compare peoples traits in relation to their age and activities they may or may not be able to do
# typically I would expect things like driving and university to give a lower result to to child than adult
# and for father, mother, son and daughter to have a higher value when comparing a more generic term like adult and child
# some results were lower than expected university compared to son seems very low at 0.06
# I would expect the web_lm to give a better comparison for more nuanced terms like these