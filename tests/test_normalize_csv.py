import os
import sys
sys.path.append('.')
import pytest
current_dir = os.path.dirname(os.path.abspath(__file__))
bin_dir = os.path.abspath(os.path.join(current_dir, '..', 'bin'))
sys.path.insert(0, bin_dir) # is this to avoid the linter hickuping on `bin`?  I believe that rule can be turned off
from normalize_csv import normalize_csv, write_normalized_csv, main

def test_normalize_csv_valid(tmp_path):
    """
    Test that a valid CSV file with a header and two data rows
    is parsed correctly.
    """
    csv_content = (
        "symbol,price,price_change,price_percent_change\n"
        "AAPL,150,1,0.67%\n"
        "GOOG,2800,10,0.36%\n"
    )
    csv_file = tmp_path / "valid.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    result = normalize_csv(str(csv_file))
    expected = [
        {
            "symbol": "AAPL",
            "price": "150",
            "price_change": "1",
            "price_percent_change": "0.67%",
        },
        {
            "symbol": "GOOG",
            "price": "2800",
            "price_change": "10",
            "price_percent_change": "0.36%",
        },
    ]
    assert result == expected

def test_normalize_csv_insufficient_columns(tmp_path):
    """
    Test that a row with fewer than 4 columns raises an AssertionError.
    """
    csv_content = (
        "symbol,price,price_change,price_percent_change\n"
        "AAPL,150,1\n"  # Missing the fourth column
    )
    csv_file = tmp_path / "insufficient.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    with pytest.raises(AssertionError, match="Row has fewer than 4 columns"):
        normalize_csv(str(csv_file))

def test_normalize_csv_no_data(tmp_path):
    """
    Test that a CSV with only a header row raises an AssertionError.
    """
    csv_content = "symbol,price,price_change,price_percent_change\n"
    csv_file = tmp_path / "no_data.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    with pytest.raises(AssertionError, match="No data found after skipping header"):
        normalize_csv(str(csv_file))

def test_normalize_csv_nonexistent_file(tmp_path):
    """
    Test that providing a path to a non-existent file raises an AssertionError.
    """
    fake_file = tmp_path / "nonexistent.csv"
    with pytest.raises(AssertionError, match="File not found"):
        normalize_csv(str(fake_file))

def test_write_normalized_csv(tmp_path):
    """
    Test that write_normalized_csv correctly writes the normalized data.
    """
    normalized_rows = [
        {
            "symbol": "AAPL",
            "price": "150",
            "price_change": "1",
            "price_percent_change": "0.67%",
        },
        {
            "symbol": "GOOG",
            "price": "2800",
            "price_change": "10",
            "price_percent_change": "0.36%",
        },
    ]
    output_file = tmp_path / "output.csv"
    write_normalized_csv(normalized_rows, str(output_file))

    # Read the file manually and compare its contents.
    with open(output_file, 'r', encoding="utf-8") as f:
        content = f.read()
    # Expected CSV content (header plus two rows).
    expected_content = (
        "symbol,price,price_change,price_percent_change\n"
        "AAPL,150,1,0.67%\n"
        "GOOG,2800,10,0.36%\n"
    )
    # Compare lines ignoring potential differences in trailing newlines.
    content_lines = content.strip().splitlines()
    expected_lines = expected_content.strip().splitlines()
    assert content_lines == expected_lines

def test_write_normalized_csv_empty(tmp_path):
    """
    Test that attempting to write an empty list of normalized rows raises an AssertionError.
    """
    normalized_rows = []
    output_file = tmp_path / "empty.csv"
    with pytest.raises(AssertionError, match="Nothing to write"):
        write_normalized_csv(normalized_rows, str(output_file))

def test_write_normalized_csv_invalid_path():
    """
    Test that providing a non-string output_path raises an AssertionError.
    """
    normalized_rows = [
        {
            "symbol": "AAPL",
            "price": "150",
            "price_change": "1",
            "price_percent_change": "0.67%",
        }
    ]
    with pytest.raises(AssertionError, match="Expected string path"):
        write_normalized_csv(normalized_rows, 123)  # Non-string output path

def test_normalize_csv_invalid_path_type():
    """
    Test that providing a non-string input_path to normalize_csv raises an AssertionError.
    """
    with pytest.raises(AssertionError, match="Expected string path"):
        normalize_csv(123)  # Non-string input path

def test_main(monkeypatch, tmp_path, capsys):
    """
    Test the main() function by simulating command-line arguments.
    """
    # Create a temporary CSV file with valid content.
    csv_content = (
        "symbol,price,price_change,price_percent_change\n"
        "MSFT,300,2,0.67%\n"
    )
    csv_file = tmp_path / "test_main.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    # Simulate command-line arguments: the first element is the script name.
    monkeypatch.setattr(sys, "argv", ["normalize_csv.py", str(csv_file)])

    # Call main(). It should create an output file and print a message.
    main()

    # Capture stdout.
    captured = capsys.readouterr().out.strip()
    expected_message = "Normalized CSV created: "
    assert captured.startswith(expected_message)

    # Check that the output file exists.
    # The output filename is the input filename (without extension) + "_norm.csv"
    output_file = csv_file.with_name(csv_file.stem + "_norm.csv")
    assert os.path.exists(str(output_file))
