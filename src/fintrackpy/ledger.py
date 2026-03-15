from fintrackpy.transactions import Transaction


class Ledger:
    '''A class to represent a financial ledger, which is a collection of transactions.'''

    # -------------------------------
    # Constructor
    # -------------------------------

    def __init__(self):
        self._transactions = []

    # -------------------------------
    # Magic methods
    # -------------------------------

    def __repr__(self) -> str:
        '''Defines how ledger is displayed for developers'''

        return f"Ledger(transactions={len(self._transactions)})"

    def __str__(self) -> str:
        '''Defines how ledger is displayed for users'''

        if not self._transactions:
            return "Ledger is empty."

        header = [
            f"Ledger: {len(self._transactions)} transactions",
            "-" * 20,
            "Date | Description | Amount | Category"
        ]

        rows = [str(t) for t in self._transactions]

        return "\n".join(header + rows)

    def __len__(self) -> int:
        '''Defines the length of the ledger as the number of transactions it contains'''

        return len(self._transactions)

    def __iter__(self):
        '''Defines the ledger as an iterable, allowing iteration over its transactions'''

        return iter(self._transactions)

    # -------------------------------
    # Generators
    # -------------------------------

    def get_expenses(self):
        '''Returns a generator of transactions with negative amounts (expenses)'''

        for tx in self._transactions:
            if tx.is_expense:
                yield tx

    def get_income(self):
        '''Returns a generator of transactions with positive amounts (income)'''

        for tx in self._transactions:
            if tx.is_income:
                yield tx

    def get_by_category(self, category: str):
        '''Returns a generator of transactions that match the specified category'''

        if not isinstance(category, str):
            raise TypeError(
                f"Category must be a string, got {type(category)}"
            )

        for tx in self._transactions:
            if tx.category is not None and tx.category.lower() == category.lower():
                yield tx

    def get_by_date(self, year: int, month: int):
        '''Yields transactions from a specific month and year'''

        for tx in self._transactions:
            if tx.date.year == year and tx.date.month == month:
                yield tx

    # -------------------------------
    # Public Methods
    # -------------------------------

    def add(self, transaction: Transaction) -> None:
        '''Adds a transaction to the ledger after validating its type.'''

        if not isinstance(transaction, Transaction):
            raise TypeError(
                f"Expected a Transaction object, got {type(transaction)}"
            )

        self._transactions.append(transaction)

    def total_income(self):
        '''Returns the total income by summing the amounts of all income transactions'''

        return sum(tx.amount for tx in self.get_income())

    def total_expenses(self):
        '''Returns the total expenses by summing the amounts of all expense transactions'''

        return sum(tx.amount for tx in self.get_expenses())

    def net_total(self):
        '''Returns the total net total by summing the amounts of all income and expense transactions'''

        return sum(tx.amount for tx in self._transactions)

    def category_totals(self, kind: str):
        '''
        Returns a dictionary with categories as keys and total amounts as values

        Attributes
        ----------
        kind : str
            The type of transactions to include in the totals. Must be 'income', 'expense', or 'all'.
        '''

        totals = {}

        if kind not in {"income", "expense", "all"}:
            raise ValueError(f"Invalid kind: {kind}. Must be 'income', 'expense', or 'all'.")
        elif kind == "income":
            transactions = self.get_income()
        elif kind == "expense":
            transactions = self.get_expenses()
        else:
            transactions = self._transactions

        for tx in transactions:
            cat = tx.category or "uncategorized"
            totals[cat] = totals.get(cat, 0) + tx.amount

        return totals
