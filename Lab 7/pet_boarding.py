import math


def parse_booking(text):
    if not isinstance(text, str):
        return None

    parts = text.split(":")
    if len(parts) != 2:
        return None

    pet, days = parts
    pet = pet.strip()

    if not pet:
        return None

    try:
        day_value = float(days.strip())
    except (ValueError, OverflowError):
        return None

    if not math.isfinite(day_value) or day_value < 0:
        return None

    return pet.title(), day_value


def stay_average(days_csv):
    if not isinstance(days_csv, str) or not days_csv.strip():
        return None

    parts = [part.strip() for part in days_csv.split(",")]

    if not all(parts):
        return None

    try:
        values = [int(part) for part in parts]
    except (ValueError, OverflowError):
        return None

    if any(value < 0 for value in values):
        return None

    return sum(values) // len(values)


def payable_fee(text):
    if not isinstance(text, str):
        return None

    parts = text.split("|")
    if len(parts) != 2:
        return None

    try:
        fee = float(parts[0].strip())
        discount = float(parts[1].strip())
    except (ValueError, OverflowError):
        return None

    if not math.isfinite(fee) or not math.isfinite(discount):
        return None

    if fee < 0 or discount < 0:
        return None

    total = fee * 1.18 - discount
    return max(total, 0)


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter pet:days (e.g. dog:5): ")
    result = parse_booking(user_input)
    print("Pet and Days:", result)

    print("\n==== Running stay_average ====")
    user_input = input(
        "Enter stay lengths in days as CSV (e.g. 2,5,7): "
    )
    result = stay_average(user_input)
    print("Average Stay:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 1500|100): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()