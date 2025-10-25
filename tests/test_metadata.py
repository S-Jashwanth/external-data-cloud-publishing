from src.metadata_extractor import extract_metadata_local
def test_metadata_customers():
    meta = extract_metadata_local('data/raw/customers.csv')
    assert meta['num_rows'] == 4
    assert 'customer_id' in meta['columns']
