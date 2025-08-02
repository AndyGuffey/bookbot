# FUNCTION THAT COUNTS WORDS 

# Split words function to get count 
def get_word_count(book_text):
    split_words = book_text.split()
    number_of_words = len(split_words)
    return(number_of_words)

def get_character_count(book_text):
    # Convert to lowercase 
    lower_case_book_text = book_text.lower()

    # Store char counts in below var
    char_counts ={}
    # Loop through each char in the text
    for char in lower_case_book_text:
        if char in char_counts:
            char_counts[char] += 1 # add 1 to existing count 
        else:
            # add char to char counts
            char_counts[char] = 1 # set initial count to 1
    return(char_counts) 

def sort_dictionary(char_counts):
    def sort_on(items):
        return items["num"]
    # Empty list to store the dictionaries 
    char_list=[]

    # Loop through each char and count in the dict 
    for char, count in char_counts.items():
        # create new dict for the char 
        char_dict = {"char":char, "num": count}
        # Add it to the list 
        char_list.append(char_dict)
    
    char_list.sort(reverse=True,key=sort_on)
    return(char_list)
