from unittest.mock import MagicMock, patch
from bin.gainers import wsj

def test_gainer_download_wsj():
    downloader = wsj.GainerDownloadWSJ()
    assert downloader.url == "https://www.wsj.com/market-data/stocks/biggest-gainers"
    assert downloader.output_file == "sample_data/wjsgainers.html"

    with patch("subprocess.run") as mock_subprocess:
        downloader.download()
        mock_subprocess.assert_called_once()
        
def test_gainer_process_wsj():
    processor = wsj.GainerProcessWSJ()
    assert processor.input_file == "sample_data/wjsgainers.html"
    assert processor.output_file == "sample_data/wjsgainers.csv"

    mock_df = MagicMock(spec=pd.DataFrame) #Creates a magic mock that behaves like a dataframe.
    with patch("pandas.read_html", return_value=[mock_df]) as mock_read_html:
        with patch("pandas.DataFrame.to_csv") as mock_to_csv:
            processor.normalize()
            mock_read_html.assert_called_once()
            mock_df.to_csv.assert_called_once() #calls the to_csv function from the mocked dataframe.
