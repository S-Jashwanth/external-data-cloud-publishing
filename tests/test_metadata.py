import pandas as pd
import pytest
from src.metadata_extractor import extract_metadata_local

# Fixture to create a temporary CSV file
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

# Test using the temporary CSV
def test_metadata_customers(temp_customers_csv):
    # Call your metadata extractor
    metadata = extract_metadata_local(temp_customers_csv)
    
    # Basic assertions
    assert "id" in metadata
    assert "name" in metadata
    assert "email" in metadata
    assert metadata["id"]["count"] == 3  # Example check
