from unittest.mock import patch, Mock
import get_gainer

def test_get_gainer_main():
    with patch("sys.argv", ["get_gainer.py", "yahoo"]), \
         patch("get_gainer.GainerFactory") as mock_factory, \
         patch("get_gainer.ProcessGainer") as mock_process_gainer:

        mock_downloader = Mock()
        mock_processor = Mock()
        mock_factory_instance = Mock()
        mock_factory_instance.get_downloader.return_value = mock_downloader
        mock_factory_instance.get_processor.return_value = mock_processor
        mock_factory.return_value = mock_factory_instance

        mock_process_gainer_instance = Mock()
        mock_process_gainer.return_value = mock_process_gainer_instance

        get_gainer.main()

        mock_factory.assert_called_once_with("yahoo")
        mock_process_gainer.assert_called_once_with(mock_downloader, mock_processor)
        mock_process_gainer_instance.process.assert_called_once()

def test_get_gainer_main_no_args():
    with patch("sys.argv", ["get_gainer.py"]), \
         patch("sys.exit") as mock_exit, \
         patch("builtins.print") as mock_print:
        get_gainer.main()
        mock_print.assert_called_once_with("Usage: python get_gainer.py [yahoo|wsj]")
        mock_exit.assert_called_once_with(1)
             
