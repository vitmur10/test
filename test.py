import pytest
from parsing_bytes import get_data_from_payload, device_settings, field8, test_data


def test_type():
    assert get_data_from_payload(device_settings) == type(dict)


@pytest.mark.parametrize('a, expencted_result', [(get_data_from_payload(device_settings), get_data_from_payload(device_settings)),
                                                 (get_data_from_payload(device_settings), field8),
                                                 (get_data_from_payload(device_settings), test_data)])
def test_result(a, expencted_result):
    with pytest.raises(AttributeError):
        assert get_data_from_payload(a) == expencted_result
