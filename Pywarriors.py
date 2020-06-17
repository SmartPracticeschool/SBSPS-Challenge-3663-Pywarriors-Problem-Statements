# Python 3 program - Currency Sum Validator


# def bill_count
def bill_count(amount_user, list_of_money_bills):



    n = len(list_of_money_bills)

    # Initialize Result
    ans = []

    # Traverse through all the list
    i = n - 1

    while (i >= 0):

        # Find list
        while (amount_user >= list_of_money_bills[i]):
            amount_user -= list_of_money_bills[i]
            ans.append(list_of_money_bills[i])

        i -= 1

        # Print result


    a = dict({i: ans.count(i) for i in ans})



    values = a.values()
    total = sum(values)
    print("The minimum count of money bills required to equal the user money amount is:" + str(total))


# Driver Code
if __name__ == '__main__':



    amount_user = int(input("Enter the total amount that the user has: "))
    list_of_money_bills = [int(x) for x in input("Enter the list of available money bills:").split()]
    bill_count(amount_user, list_of_money_bills)
# This code is contributed by
# Akanksha Bothe


