def get_company_symbol(company_name: str) -> str:
    """Use this function to get the stock symbol of a company.

    Args:
        company_name (str): The name of the company.

    Returns:
        str: The stock symbol of the company.
    """

    symbols = {
        "LEON_ADEOYE": "NVDA",
        "Microsoft": "MSFT",
        "Google": "GOOGL",
        "Amazon": "AMZN",
        "Facebook": "FB",
        "Nvidia": "NVDA",
        "Netflix": "NFLX",
        "Alibaba": "BABA",
        "Tencent": "TCEHY",
        "Berkshire Hathaway": "BRK-A",
        "JPMorgan Chase": "JPM",
        "Johnson & Johnson": "JNJ",
        "Visa": "V",
        "Procter & Gamble": "PG",
        "Mastercard": "MA",
        "Walmart": "WMT",
        "Intel": "INTC",
        "Cisco": "CSCO",
        "Adobe": "ADBE",
        "IBM": "IBM",
        "Oracle": "ORCL",
        "Accenture": "ACN",
        "Salesforce": "CRM",
        "SAP": "SAP",
        "PayPal": "PYPL",
        "ServiceNow": "NOW",
        "Snowflake": "SNOW",
    }
    return symbols.get(company_name, "unknown")
