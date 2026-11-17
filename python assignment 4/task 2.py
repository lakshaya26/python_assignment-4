attendance = {}

records = [
    "101,2026-10-01,P",
    "102,2026-10-01,A",
    "101,2026-10-02,P",
    "102,2026-10-02,P",
    "103,2026-10-02,X"
]

errors = []

for line in records:
    try:
        parts = line.split(",")

        if len(parts) != 3:
            raise ValueError

        reg, date, status = parts

        if status not in ["P", "A"]:
            raise ValueError

        if reg not in attendance:
            attendance[reg] = [0, 0]

        attendance[reg][0] += 1

        if status == "P":
            attendance[reg][1] += 1

    except ValueError:
        errors.append(line)

for reg, values in attendance.items():
    percentage = values[1] / values[0] * 100
    print(reg, "Attendance:", percentage, "%")

    if percentage < 75:
        print("Below 75%")

print("Damaged Records:", errors)