def read_attendance():
    return {
        "101": [20, 18],
        "102": [20, 14],
        "103": [20, 19]
    }


def calculate_percentage(data):
    result = {}

    for reg, values in data.items():
        percentage = values[1] / values[0] * 100
        result[reg] = percentage

    return result


def display_report(result):
    for reg, percentage in result.items():
        print(reg, ":", percentage, "%")

        if percentage < 75:
            print("Attendance shortage")


def main():
    data = read_attendance()
    result = calculate_percentage(data)
    display_report(result)


if __name__ == "__main__":
    main()