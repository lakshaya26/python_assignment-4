class InvalidRecord(Exception):
    pass


def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord("Wrong number of fields")

    if parts[2] not in ["P", "A"]:
        raise InvalidRecord("Invalid status")

    return parts


def summarise(records):
    present = 0
    absent = 0
    errors = []

    for number, line in enumerate(records, start=1):
        try:
            data = parse_line(line)

            if data[2] == "P":
                present += 1
            else:
                absent += 1

        except InvalidRecord as error:
            errors.append((number, str(error)))

    return present, absent, errors


records = [
    "101,2026-10-08,P",
    "102,2026-10-08,A",
    "103,2026-10-08",
    "104,2026-10-08,L"
]

print(summarise(records))