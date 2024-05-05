# treasury_gov_pandas.py

Library for downloading treasury.gov datasets.

The first time you request a dataset, the entire dataset is retrieved and saved locally. Subsequent requests for the dataset only download newly available records plus a few others to ensure continuity.
