# "Robo Advisor" Project


# Prerequisites

    + Anacoda 3.7
    + Python 3.7
    + Pip

# Security
Repository should contain a file called ".gitignore" which prevents the ".env" file and its secret credentials from being tracked in version control.

The source code excludes secret API Key value.

# Information Input
The system prompts the user to input **one** stock symbol (e.g. "MSFT", "AAPL", etc.).
Code fails if stock does not match.
"There was an error. Please make sure your ticker symbol is correct."

# Validation Requirements
Prevents an HTTP request if stock symbol not likely to be valid (e.g. symbol of "8888")

Fails gracefully if encountering a response error (e.g. symbol of "OOPS")

# Information Output Requirements
Historical prices are written to a CSV file, file path indicated on output

All prices formatted to USD (doesn't apply to CSV file values)

Displays final recommendation, Yes/No

Justification / context = If the stock's latest closing price is less than 20% above its recent low, "Buy", else "Don't Buy".
