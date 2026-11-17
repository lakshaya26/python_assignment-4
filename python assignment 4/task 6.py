students = [
    "101,Arun,CSE,arun@gmail.com,Music;Dance",
    "102,Ravi,ECE,ravi@gmail.com,Singing;Dance",
    "103,Kumar,CSE,kumargmail.com,Music",
    "101,Arun,CSE,arun@gmail.com,Music",
    "104,John,ECE,john@gmail.com"
]

registered = set()
events = {}
errors = []

for line in students:
    try:
        parts = line.split(",")

        if len(parts) != 5:
            raise ValueError("Damaged record")

        reg, name, dept, email, choices = parts

        if reg in registered:
            raise ValueError("Duplicate registration")

        if "@" not in email or "." not in email:
            raise ValueError("Invalid email")

        registered.add(reg)

        for event in choices.split(";"):
            events.setdefault(event, []).append(name)

        print("Registered:", name)

    except ValueError as error:
        errors.append(line + " - " + str(error))

print("\nEvent Participants")

for event, names in events.items():
    print(event, ":", names)

print("\nError Records:", errors)
print("\nTotal Registrations:", len(registered))