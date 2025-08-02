# Imports 
import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary

def get_book_text(path_to_file):
    # Open the file at the specified path in read mode
    with open(path_to_file) as f:
        # Read the entire contents of the file into a string
        file_contents = f.read()
        # Return the file contents as a string
        return file_contents
    

def main():
   
   #Check if user provided file path argument 
   if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   
   # Get file path from command line arg 
   file_path = sys.argv[1]

   # Get the text content from the file path input by user 
   book_text = get_book_text(file_path)

    # get word count 
   word_count_result = get_word_count(book_text) 

    # Get character counts  
   char_counts = get_character_count(book_text)

    # Sort the character counts 
   sorted_chars = sort_dictionary(char_counts)


   # ? ~~ REPORT FORMATTING ~~ 

   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {file_path}...")
   print("----------- Word Count ----------")
   print(f"Found {word_count_result} total words")
   print("--------- Character Count -------")

   for char_dict in sorted_chars:
       if char_dict["char"].isalpha():
           print(f"{char_dict['char']}: {char_dict['num']}")

   print("============= END ===============")

    





    
# Execute the main function to run the program
main()