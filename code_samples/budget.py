# The Budget class. You'll need to edit/expand on this.
class Budget:
    '''
    This class is designed to create and store budget information.

    This class will (eventually) have the following attributes:

        income [type: int or float]
            This is the monthly income for the budget.
        expenses [type: int or float]
            This is the total monthly expenses.
        categories [type: dictionary]
            This is a dictionary of expense categories (keys)
            and estimated cost associated with those categories (values).

    This class (currently) has the following methods:

        __init__(income)
            Initialize the budget and set the income based on user input.
            Set the initial expenses to 0 and initialize the dictionary
            of categories to be empty.

        get_income()
            Print the current income associated with this budget.
    '''

    def __init__(self, income):
        '''
        Initializes the budget.
        Default expenses are 0 and no expense categories are defined
        (as indicated by the empty dictionary).

        Argument(s):
            income [type: int or float]
                Specifies the monthly income
        '''
        self.income = income

    def get_income(self):
        '''
        Prints the current income. Requires no arguments.
        '''
        print('Your current income is %i dollars' %self.income)
