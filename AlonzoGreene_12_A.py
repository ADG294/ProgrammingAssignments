import csv
import numpy as np

# The purpose of this program is to create a csv file (if one isn't already created),
# then store its data to a file that will be sliced into a numpy array.
# after being sliced methods will be used on the data in order to calculate the
# mean, median, standard deviation, min, and max then print how many students
# passed and failed each exam. After it will print the pass percentage from all
# the exams.

# Create a function that creates a csv file if one doesn't exist that takes user input.

def students():

    file_path = 'students.csv'

    # Create a try except block that checks if the created file exists or not.
    try:
        with open('students.csv', 'w', newline="") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

            # Create a loop that takes user input on each iteration.
            for x in range(10):

                first = input('Enter your first name: ')

                last = input('Enter your last name: ')

                exam_1 = input('Enter Exam score: ')

                exam_2 = input('Enter Exam score: ')

                exam_3 = input('Enter Exam score: ')

                writer.writerow([first, last, exam_1, exam_2, exam_3])

                print(f"csv file '{file_path}' was created ")

    except FileExistsError:

        print('File already exists.')

# Create a function that generates data from the file and slices the columns needed
# into arrays that can be used in different methods to be calculated.
def student_scores():

   A = np.genfromtxt('students.csv', delimiter=',')

   # Slice the 3rd column from the file that are the scores from exam 1.
   exam_1 = A[:, 2]

   # Calculate the mean, median, standard deviation, min, and max.
   np.mean(exam_1)

   np.median(exam_1)

   np.std(exam_1)

   np.min(exam_1)

   np.max(exam_1)

   # Slice the 4th column from the file that are the scores from exam 2.
   exam_2 = A[:, 3]

   # Calculate the mean, median, standard deviation, min, and max.
   np.mean(exam_2)

   np.median(exam_2)

   np.std(exam_2)

   np.min(exam_2)

   np.max(exam_2)

   # Slice the 5th column from the file that are the scores from exam 3.
   exam_3 = A[:, 4]

   # Calculate the mean, median, standard deviation, min, and max.
   np.mean(exam_3)

   np.median(exam_3)

   np.std(exam_3)

   np.min(exam_3)

   np.max(exam_3)

   # Slice the 3rd - 5th column from the file that are the scores from all exams.
   all_exams = A[:, 2:5]

   # Calculate the mean, median, standard deviation, min, and max.
   np.mean(all_exams)

   np.median(all_exams)

   np.std(all_exams)

   np.min(all_exams)

   np.max(all_exams)

   # Create pass and fail counters
   countP = 0

   countF = 0

   # Create loops for each exam and print the number of passing and failing students.
   for score in exam_1:
       if score >= 60:

           countP += 1

       else:
           countF += 1

       print(f'Students passing: {countP}')

       print(f'Students failing: {countF}')

   for score in exam_2:
       if score >= 60:

           countP += 1

       else:

           countF += 1

       print(f'Students passing: {countP}')

       print(f'Students failing: {countF}')

   for score in exam_3:

       if score >= 60:

           countP += 1

       else:

           countF += 1

       print(f'Students passing: {countP}')

       print(f'Students failing: {countF}')

   # Create a loop that calculates and prints the pass percentage for all exams.
   for score in all_exams:

       if score >= 60:

           countP += 1

       else:

           countF += 1

       print(f'Pass percentage for all exams: {(countP / 10) * 100 }%')

# Create main function then call both functions
def main():

    students()

    student_scores()

main()