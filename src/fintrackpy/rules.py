import re
from fintrackpy.transactions import Transaction


class CategoryRule:
    '''Match transaction descriptions to categories using regex patterns.'''

    # -------------------------------
    # Constructor
    # -------------------------------

    def __init__(self, pattern: str, category: str):
        self.pattern = re.compile(pattern, re.IGNORECASE)
        self.category = category

    # -------------------------------
    # Public methods
    # -------------------------------

    def matches(self, description: str) -> bool:
        '''Checks if the pattern matches the description'''

        return self.pattern.search(description) is not None


class Categorizer:
    '''A class to categorize transactions based on their descriptions.'''

    # -------------------------------
    # Constructor
    # -------------------------------

    def __init__(self, rules: list[CategoryRule]):
        self.rules = rules

    # -------------------------------
    # Public methods
    # -------------------------------

    def categorize(self, transaction: Transaction) -> None:
        '''Categorizes a transaction based on its description and the defined rules'''

        for rule in self.rules:
            if rule.matches(transaction.description):
                transaction.category = rule.category
                return None  # Stop after the first match

        # Set to None if no rules match
        transaction.category = None
