import pytest
from bin.gainers import factory, yahoo, wsj

def test_factory():
    factory_instance = factory.GainerFactory("yahoo")
    assert factory_instance.choice == "yahoo"

    downloader = factory_instance.get_downloader()
    assert isinstance(downloader, yahoo.GainerDownloadYahoo)

    processor = factory_instance.get_processor()
    assert isinstance(processor, yahoo.GainerProcessYahoo)

    factory_instance_wsj = factory.GainerFactory("wsj")
    downloader_wsj = factory_instance_wsj.get_downloader()
    assert isinstance(downloader_wsj, wsj.GainerDownloadWSJ)

    processor_wsj = factory_instance_wsj.get_processor()
    assert isinstance(processor_wsj, wsj.GainerProcessWSJ)

    with pytest.raises(AssertionError):
        factory.GainerFactory("invalid")
        
