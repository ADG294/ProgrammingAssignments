import random

# Program will create a text file that will provide answers

# to random yes or no questions.

# Then program will read answers from text file into a list.

# Then the program will ask a yes or no question then prompt the user to quit when they're ready

# then display the response.


def write_responses():

    eight_ball_file = open('8ball_responses.txt', 'w')

    r1 = 'Yes, of course!'

    r2 = 'Without a doubt, yes.'

    r3 = 'You can count on it.'

    r4 = 'For sure!'

    r5 = 'Ask me later!'

    r6 = "I'm not sure."

    r7 = "I can't tell you right now."

    r8 = "I'll tell you after my nap."

    r9 = "No way!"

    r10 = "I don't think so."

    r11 = "Without a doubt, no."

    r12 = "The answer is clearly NO!"

    eight_ball_file.write(r1 + '\n')

    eight_ball_file.write(r2 + '\n')

    eight_ball_file.write(r3 + '\n')

    eight_ball_file.write(r4 + '\n')

    eight_ball_file.write(r5 + '\n')

    eight_ball_file.write(r6 + '\n')

    eight_ball_file.write(r7 + '\n')

    eight_ball_file.write(r8 + '\n')

    eight_ball_file.write(r9 + '\n')

    eight_ball_file.write(r10 + '\n')

    eight_ball_file.write(r11 + '\n')

    eight_ball_file.write(r12 + '\n')

    eight_ball_file = open('8ball_responses.txt', 'r')

    line = eight_ball_file.read()

    line_list = line.split('\n')

    eight_ball_file.close()


    while True:
        questions = str(input('Ask a a question! [press enter to quit]\n'))

        r_index = random.randint(0, len(line_list) - 1)

        r_answer = line_list[r_index]

        if questions == "":

            print("Goodbye")

            break

        else:

         print(r_answer)

write_responses()