import pytest
from hypothesis import given, strategies as st

from pet_boarding import parse_booking, stay_average, payable_fee


@given(st.text() | st.none())
def test_parse_booking_no_crash(value):
    try:
        result = parse_booking(value)
        assert result is None or (
            isinstance(result, tuple) and len(result) == 2
        )
    except Exception as exc:
        pytest.fail(f"parse_booking crashed for {value!r}: {exc}")


@given(st.text() | st.none())
def test_stay_average_no_crash(value):
    try:
        result = stay_average(value)
        assert result is None or isinstance(result, int)
    except Exception as exc:
        pytest.fail(f"stay_average crashed for {value!r}: {exc}")


@given(st.text() | st.none())
def test_payable_fee_no_crash(value):
    try:
        result = payable_fee(value)
        assert result is None or result >= 0
    except Exception as exc:
        pytest.fail(f"payable_fee crashed for {value!r}: {exc}")