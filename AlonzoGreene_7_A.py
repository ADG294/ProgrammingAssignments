import re

# The purpose of this program is to create a regular expression pattern that will
# allow a user to input multiple sentences starting with words or numbers then count
# them after printing those sentences out.

# Create a sentence matching and counting function.
def sentence_count(s):

    # Create a re pattern for a sentence.
    pat = r'[A-Z\d].*?[.!?](?= [A-Z]|$)'

    # Create a re pattern that helps identify a sentence.
    sen_pat = r'[^.!?]+[.!?](?= [A-Z]|$)'

    # Create a match variable that has DOITALL or MULTILINE flags set to look ahead
    # for the end of the current sentence after a space and beginning of a new sentence
    # or the end of the line.
    m = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)

    # Create a sentence variable using the findall method that validates whether it's a
    # sentence or not.
    sen = re.findall(sen_pat, s)

    # Create a for loop that prints every sentence line by line.
    for i in m:

        print('->', i)

    # Use the len function to count the length of the sentence variable.
    # This will be stored in the sentence count variable.
    sen_count = len(sen)

    # Use an f string to print out the sen_count variable. This will display the
    # total number of sentences.
    print(f'Sentence Count: {sen_count}')

# Create a main function
def main():

    # Create an input variable
    s = input('''Enter your sentences: \n''')

    # Call the sentence_count function
    sentence_count(s)

# Call the main function
main()
