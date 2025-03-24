from unittest.mock import MagicMock, patch
from bin.gainers import yahoo

def test_gainer_download_yahoo():
    downloader = yahoo.GainerDownloadYahoo()
    assert downloader.url == "https://finance.yahoo.com/gainers"
    assert downloader.output_file == "sample_data/ygainers.html"

    with patch("subprocess.run") as mock_subprocess:
        downloader.download()
        mock_subprocess.assert_called_once()

def test_gainer_process_yahoo():
    processor = yahoo.GainerProcessYahoo()
    assert processor.input_file == "sample_data/ygainers.html"
    assert processor.output_file == "sample_data/ygainers.csv"

    with patch("pandas.read_html", return_value=[MagicMock()]) as mock_read_html:
        with patch("pandas.DataFrame.to_csv") as mock_to_csv:
            processor.normalize()
            mock_read_html.assert_called_once()
            mock_to_csv.assert_called_once()
            
