# FinTrackPy

FinTrackPy is a lightweight Python package for processing personal bank statements and generating simple financial summaries.

The package allows users to import bank statements (Excel or CSV), automatically categorize transactions using rule-based matching, and compute financial metrics such as total income, expenses, and category-level spending.

---

# Features

FinTrackPy provides tools to:

• Load bank statements from Excel or CSV files  
• Parse and normalize transaction data  
• Automatically categorize transactions using regex-based rules  
• Store transactions in a ledger object  
• Compute financial summaries such as income, expenses, and net totals  
• Generate category-level spending summaries  

The package is designed to be simple, extensible, and easy to integrate into other applications.

---

# Modules

*transactions.py*
Defines the Transaction class representing individual financial records

*ledger.py*
Stores and manages collections of transactions and provides summary methods

*rules.py*
Defines category matching rules using regular expressions

*default_rules.py*
Contains predefined categorization rules

*io.py*
Handles loading and parsing of bank statements

*pipeline.py*
Orchestrates the full processing workflow from raw file to processed ledger

---

# Installation

Install the package from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ finance-tracker-g1