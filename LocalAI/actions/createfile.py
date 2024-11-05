import datetime

def create_file(prompt):
    # Get the timestamp and convert it to a consistent format
    current_date = datetime.date.today()

    # Create a new file with a unique name based on the formatted timestamp
    filename = f"{prompt}_{current_date}.txt"

    # Create a new text document and save it to the current working directory
    with open(filename, "w") as file:
        pass

    print(f"A new text document has been created: {filename}")