import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


def test_unknown_pet_type():
    with pytest.raises(ValueError):
        boarding_fee("bird", 2, False)


def test_negative_days():
    with pytest.raises(ValueError):
        boarding_fee("cat", -1, False)


def test_premium_cat_within_included_days():
    assert boarding_fee("cat", 4, True) == 0


def test_long_dog_stay():
    assert boarding_fee("dog", 15, False) == 585


def test_regular_cat_extra_days():
    assert boarding_fee("cat", 5, False) == 40


def test_senior_admission():
    assert admission_ok(10, 3, True) is True


def test_young_pet_rejected():
    assert admission_ok(0.5, 3, False) is False


def test_adult_pet_admitted():
    assert admission_ok(4, 2, False) is True


def test_checkout_open_long_weekend():
    assert checkout_status(50, True, True) == "open"


def test_checkout_late_short_weekday():
    assert checkout_status(10, False, False) == "late"


def test_checkout_closed_long_weekday():
    assert checkout_status(0, True, False) == "closed"