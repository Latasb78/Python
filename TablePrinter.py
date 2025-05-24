# TablePrinter.py
print("Name:Lata.S.B",
       "USN:1AY24AI060",
       "Section:'O'")
def print_table(table_data, headers=None):
    # Transpose the table to work column-wise
    columns = list(zip(*table_data))

    # Determine max width for each column
    col_widths = [max(len(str(item)) for item in col) for col in columns]

    # Print headers if provided
    if headers:
        header_line = " | ".join(str(header).ljust(col_widths[i]) for i, header in enumerate(headers))
        print(header_line)
        print("-" * len(header_line))

    # Print each row
    for row in table_data:
        row_line = " | ".join(str(item).ljust(col_widths[i]) for i, item in enumerate(row))
        print(row_line)

# Example usage
if _name_ == "_main_":
    headers = ["Item", "Count"]
    inventory = {
        "gold coin": 45,
        "rope": 1,
        "dagger": 2,
        "ruby": 1,
        "torch": 6
    }

    # Convert dict to list of lists
    table = [[item, count] for item, count in inventory.items()]

    print_table(table, headers)