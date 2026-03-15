from fintrackpy.io import load_santander_statement
from fintrackpy.default_rules import get_default_rules
from fintrackpy.rules import Categorizer
from fintrackpy.ledger import Ledger


def process_statement(path: str) -> Ledger:
    '''
    Load transactions from a statement, categorize them using default rules, and return a Ledger object.
    '''

    transactions = load_santander_statement(path)

    rules = get_default_rules()
    categorizer = Categorizer(rules)

    ledger = Ledger()

    for tx in transactions:
        categorizer.categorize(tx)
        ledger.add(tx)

    return ledger
