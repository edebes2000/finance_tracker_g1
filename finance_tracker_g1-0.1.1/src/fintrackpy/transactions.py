from datetime import date


class Transaction:
    '''
    Represents a single financial transaction

    Attributes
    ----------
    date : datetime.date
        Date of the transaction
    description : str
        Description of the transaction
    amount : float
        Amount of the transaction
        Positive = income / Negative = expense
    category : str | None
        Category of the transaction (optional)
    '''

    # -------------------------------
    # Constuctor
    # -------------------------------

    def __init__(self, date_: date, description: str, amount: int | float, category: str | None = None):

        # -------------------------------
        # Validate input types and values
        # -------------------------------

        # Date type validation
        if not isinstance(date_, date):
            raise TypeError(
                f"Date must be a datetime.date object, got {type(date_)}"
            )

        # Description type and value validation
        if not isinstance(description, str):
            raise TypeError(
                f"Description must be a string, got {type(description)}"
            )
        if description == "":
            raise ValueError(
                "Description cannot be an empty string"
            )

        # Amount type validation
        if not isinstance(amount, (int, float)):
            raise TypeError(
                f"Amount must be an int or float, got {type(amount)}"
            )

        # Category type validation (if provided)
        if category is not None and not isinstance(category, str):
            raise TypeError(
                f"Category must be a string or None, got {type(category)}"
            )

        # -------------------------------
        # Assign attributes for instances
        # -------------------------------

        self.date = date_
        self.description = description
        self.amount = amount
        self.category = category

    # -------------------------------
    # Magic methods
    # -------------------------------

    def __repr__(self) -> str:
        '''Defines how transaction is displayed for developers'''

        return (
            f"Transaction(date={self.date}, "
            f"description='{self.description}', "
            f"amount={self.amount}, "
            f"category={self.category})"
        )

    def __str__(self) -> str:
        '''Defines how transaction is displayed for users'''

        if self.category is not None:
            return f"{self.date.strftime('%Y-%m-%d')} | {self.description} | {self.amount} | {self.category}"
        else:
            return f"{self.date.strftime('%Y-%m-%d')} | {self.description} | {self.amount} | Uncategorized"

    def __lt__(self, other) -> bool:
        '''Defines the less than operator for sorting transactions by amount'''

        # Check if the other object is a Transactions instance
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.amount < other.amount

    # -------------------------------
    # Properties
    # -------------------------------

    @property
    def is_income(self) -> bool:
        '''Returns True if the transaction is an income (amount > 0)'''

        return self.amount > 0

    @property
    def is_expense(self) -> bool:
        '''Returns True if the transaction is an expense (amount < 0)'''

        return self.amount < 0
