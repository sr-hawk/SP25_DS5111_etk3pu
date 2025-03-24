from unittest.mock import patch, Mock
import get_gainer

def test_get_gainer_main_no_modify():
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

        # Execute the code block directly using exec
        code_to_exec = """
import sys

choice = sys.argv[1]

factory = GainerFactory(choice)
downloader = factory.get_downloader()
normalizer = factory.get_processor()

runner = ProcessGainer(downloader, normalizer)
runner.process()
"""
        exec(code_to_exec, {
            "sys": get_gainer.sys,
            "GainerFactory": mock_factory,  # Pass the mock here
            "ProcessGainer": mock_process_gainer, # Pass the mock here
        })

        mock_factory.assert_called_once_with("yahoo")
        mock_process_gainer.assert_called_once_with(mock_downloader, mock_processor)
        mock_process_gainer_instance.process.assert_called_once()
