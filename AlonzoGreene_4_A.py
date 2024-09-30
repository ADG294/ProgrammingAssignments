import time
# Program will create a list of 30 words

# and phrases that will be used to identify

# if the user input is a spam message or not.


# Define message function so it takes input from user

# and compares to the list of spam words.

# A timer function will be made using the time package

# to calculate the execution time of the program.

def spam_message():

    # Create list that holds all spam words.

    spam_words = ['gift', 'free', 'extra', 'cash', 'fast', 'earn money',
                  'giveaway', 'get paid', 'million dollars', 'prize', 'opportunity', 'risk-free',
                  'lowest', 'price', 'rate', "don't", 'miss', 'out', 'guaranteed',
                  'billion', '100%', 'winner', 'urgent', 'act now', 'You have been selected',
                  'congratulations', 'no cost', 'passwords', 'social security',
                  'credit', 'debit', 'claims', 'deal', 'investment']

    # Create a str input variable for users to input emails.

    e_mail = str(input('Enter your message:'))

    # Create count variable to help iterate through the email.

    count = 0

    # Create empty word list to hold spam words found.

    word_list = []

    # Create spam score variable.

    spam_score = 0

    # Create a variable to show tell whether the email is spam or not.

    is_spam = ''

    # Use a for loop to iterate through an email.

    for word in e_mail.split(' '):

        # Add a condition that finds matching words

        # from the spam list to the email then append

        # to the new word list then increment and update

        # spam score by count.

        if word.lower() in spam_words:

            word_list.append(word)

            count += 1

            spam_score = count

            # Add a conditional that tells whether the email

            # is spam or not based on the spam score.

            if spam_score >= 3:
                is_spam = 'Spam'

            else:
                is_spam = 'Not Spam'


    # Print spam score, whether the email is spam or not, and the new word list

    # with the spam words found in the email.

    print(f'Spam Score: {spam_score}, Spam: {is_spam} , Words: {word_list}')

# Create a make_timer function

def make_timer(func):

    # Wrap original function

    def wrapper(*args, **kwargs):

        # Assign start time

        t1 = time.time()

        # Assign an all args and keywords function to a variable

        ret_val = func(*args, **kwargs)

        #Assign end time

        t2 = time.time()

        # Display elapsed time

        print('Time elapsed was', t2 - t1)

        # Returns ret_val if it has a value

        return ret_val

    return wrapper

# Create a decorator for the make_timer function.

@make_timer

# Create main function

def main():

    # Call spam_message function.


    spam_message()





# Run main function.
main()
