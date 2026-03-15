from fintrackpy.rules import CategoryRule


def get_default_rules() -> list[CategoryRule]:
    '''
    Return a list of default CategoryRule objects for common transaction categories.
    '''

    # Store rules from most specific to least specific

    return [
        CategoryRule("mercadona|aldi|carrefour", "groceries"),
        CategoryRule("uber|bolt|taxi", "transport"),
        CategoryRule("netflix|spotify|amazon prime", "subscriptions"),
        CategoryRule("nomina|salary|payroll", "income"),
        CategoryRule("restaurante|bar|cafe", "food"),
        CategoryRule("transferencia|bizum", "transfer")
    ]
