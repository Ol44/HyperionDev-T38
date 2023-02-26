#
# # libraries
#


import spacy # imports spacy module to be used in program



#
# # functions
#


# generates list of movie titles and descriptions
def import_file():
    with open('movies.txt', 'r') as file: # closes file once code block ends
        for x in file:
            temp_list = x.split(' :') # creates new temp list by splitting x / line at ' :'
            movie_title.append(temp_list[0]) # adds first value to title list, this will always be the title
            movie_description.append(temp_list[1][ : -1]) # adds second value to descriptions list, this will always be the description, removes special char '\n' from the end of the descriptions


# converts descriptions list into tokens to be used in comparison, user will only input a description
def convert_description_to_tokens(movie_description):
    for x in movie_description:
        movie_description_md.append(nlp(x))    
        

# takes user input and returns the index value of the movie with the highest comparison value, 0 being unrelated and 1 being the same / very similar 
def watch_next(description_input):

    description = nlp(description_input) # converts users input into a token to be compared


    for x in movie_description_md: # generates a list of tokens compared to users input, the highest value of the list will be the most similar movie by description
        description = nlp(description_input)
        movie_description_md_results_list.append(description.similarity(x))


    for index, value in enumerate(movie_description_md_results_list): # enumerates list into dict, allows for get() method to be used to get original indexing
        movie_description_md_results_dict.update({value : index})
    

    movie_description_md_results_list_max = max(movie_description_md_results_list) # sets highest token value to variable

    movie_title_indexing = movie_description_md_results_dict.get(movie_description_md_results_list_max) # gets the original indexing of the highest value once the input has been compared to the descriptions

    return movie_title_indexing # returns original indexing value



#
# # global variable
#

nlp = spacy.load('en_core_web_md') # loads md model into a variable


# blank variables to be used through the program
movie_title = []
movie_title_indexing = 0
movie_description = []
movie_description_md = []
movie_description_md_results_list = []
movie_description_md_results_dict = {}
description_input = ''



#
# # main
#


# asks user to input description, checks if input is blank, loops until correct
while True:
    description_input = input('Enter the description of the movie you watched last:  ')
    if len(description_input) < 1:
        print('\nThe description cannot be blank, try again')
    else:
        break


import_file() # calls function to generates list of movie titles and descriptions
convert_description_to_tokens(movie_description) # passes descriptions list to generate tokens
movie_title_indexing = watch_next(description_input) # passes user input to return indexing


# outputs to user which movie they should watch next based on the description they provided, outputs title and description
print(f'\nYou should watch {movie_title[movie_title_indexing]}\n\nTitle: {movie_title[movie_title_indexing]}\nDescription: {movie_description[movie_title_indexing]}')