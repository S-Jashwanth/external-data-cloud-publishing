import pandas as pd
import pytest
from src.metadata_extractor import extract_metadata_local

# -----------------------------
# Fixture to create a temporary CSV file
# -----------------------------
@pytest.fixture
def temp_customers_csv(tmp_path):
    # Define CSV content
    csv_content = """id,name,email
1,John,john@example.com
2,Jane,jane@example.com
3,Bob,bob@example.com
"""
    # Create temporary CSV file
    csv_file = tmp_path / "customers.csv"
    csv_file.write_text(csv_content)
    return str(csv_file)

# -----------------------------
# Test metadata extraction
# -----------------------------
def test_metadata_customers(temp_customers_csv):
    # Call your metadata extractor
    metadata = extract_metadata_local(temp_customers_csv)
    
    # Check top-level keys
    expected_keys = ["columns", "dtypes", "file_name", "missing_values"]
    for key in expected_keys:
        assert key in metadata, f"Missing key: {key}"
    
    # Check column names
    for col in ["id", "name", "email"]:
        assert col in metadata["columns"], f"Column {col} missing"
    
    # Check data types
    expected_dtypes = {"id": "int64", "name": "object", "email": "object"}
    assert metadata["dtypes"] == expected_dtypes, f"Unexpected dtypes: {metadata['dtypes']}"
    
    # Check missing values
    for col in ["id", "name", "email"]:
        assert metadata["missing_values"][col] == 0, f"Missing values in column {col}"
    
    # Check file name
    assert metadata["file_name"] == "customers.csv"
