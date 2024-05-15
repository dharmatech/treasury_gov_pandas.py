import treasury_gov_pandas

def load():
    url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_4'

    return treasury_gov_pandas.load_records(url, lookback=10)