import pandas as pd
from datetime import datetime
from pathlib import Path
import logging

from fintrackpy.transactions import Transaction

logger = logging.getLogger(__name__)


def load_santander_statement(path: str | Path) -> list[Transaction]:
    '''
    Load transactions from an Excel or CSV file and return a list of Transaction objects.

    Expected columns:
    - date: in YYYY-MM-DD format
    - description: a string describing the transaction
    - amount: a number representing the transaction amount

    Others will be ignored.
    '''

    path = Path(path)

    # Load file depending on extension
    if path.suffix.lower() == ".xlsx":
        df = pd.read_excel(path, skiprows=6)
    elif path.suffix.lower() == '.csv':
        df = pd.read_csv(path, skiprows=6)
    else:
        raise ValueError(f"File must be xlsx or csv, got {path.suffix}")

    transactions = []

    for num, row in df.iterrows():
        try:
            date = datetime.strptime(row["Transaction date"], "%d/%m/%Y").date()

            description = row["Description"]

            # Convert European number format to standard float
            amount_str = str(row["Amount"]).replace(".", "").replace(",", ".").replace("−", "-")
            amount = float(amount_str)

            tx = Transaction(date, description, amount)
            transactions.append(tx)

        except Exception as e:
            print("#")
            logger.warning(f"Error processing row {num}: \n{row}. Error: {e}")
            continue

    return transactions
