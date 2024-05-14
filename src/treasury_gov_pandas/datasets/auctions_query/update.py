import treasury_gov_pandas

# https://fiscaldata.treasury.gov/datasets/treasury-securities-auctions-data/treasury-securities-auctions-data

def update():
    url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query'

    treasury_gov_pandas.load_records(url, lookback=10, update=True)

if __name__ == '__main__':
    update()
