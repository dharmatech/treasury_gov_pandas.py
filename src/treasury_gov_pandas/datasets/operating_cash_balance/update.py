import treasury_gov_pandas

# https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/operating-cash-balance

def update():
    url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance'

    return treasury_gov_pandas.load_records(url, update=True)

if __name__ == '__main__':
    update()
