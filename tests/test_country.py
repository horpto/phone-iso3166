from phone_iso3166.country import (
    phone_country, InvalidPhone, network_country, InvalidNetwork
)
import pytest


def test_phone_country_dk():
    assert phone_country(45) == 'DK'
    assert phone_country(4566118311) == 'DK'
    assert phone_country('+4566118311') == 'DK'


def test_invalid():
    with pytest.raises(InvalidPhone):
        phone_country(0)


def test_missing():
    with pytest.raises(InvalidPhone):
        phone_country(999)
    with pytest.raises(InvalidPhone):
        phone_country('999')


def test_whitehouse():
    # White house comment line
    assert phone_country('+1 202-456-1111') == 'US'


def test_bermuda():
    # Bermuda city hall
    assert phone_country(14412921234) == 'BM'


def test_network_dk():
    assert network_country(238, 1) == 'DK'


def test_network_multi():
    assert network_country(340, 1) == 'GP'   # Guadeloupe
    assert network_country(340, 12) == 'MQ'  # Martinique


def test_network_invalid():
    with pytest.raises(InvalidNetwork):
        network_country(0, 0)