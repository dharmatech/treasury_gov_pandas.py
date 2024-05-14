import treasury_gov_pandas

# https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/deposits-and-withdrawals-of-operating-cash

def update():
    url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/deposits_withdrawals_operating_cash'

    return treasury_gov_pandas.load_records(url, lookback=10, update=True)

if __name__ == '__main__':
    update()
