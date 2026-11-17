def calculate_bill(filename):
    total = 0
    rejected = []

    with open(filename, "r") as file:
        for line in file:
            try:
                parts = line.strip().split(",")

                if len(parts) != 3:
                    raise ValueError

                name = parts[1]
                amount = float(parts[2])

                total += amount
                print(name, amount)

            except ValueError:
                rejected.append(line.strip())

    print("Total Bill:", total)
    print("Rejected Lines:", rejected)


with open("mess.txt", "w") as file:
    file.write("101,Arun,1200\n")
    file.write("102,Ravi,1500.50\n")
    file.write("103,Kumar\n")

calculate_bill("mess.txt")