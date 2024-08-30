# Program pre-sells tickets up to a certain amount

# then displays number of remaining tickets after prompting

# the user to input how many tickets they want.

# After, app will display total number of buyers.

saleLimit = 4

def buyers():

    preSale = 20

    b = 0

    while preSale > 0:

        numberOfTickets = int(input('Enter number of tickets: '))

        if numberOfTickets > saleLimit:
            print('Cannot exceed 4 tickets!')
            numberOfTickets = int(input('Enter number of tickets: '))

        elif preSale == 0:
            break


        preSale = preSale - numberOfTickets

        b += 1

        print('Remaining Tickets: ', preSale)

    print('Total buyers: ', b)


def main():

    buyers()

main()