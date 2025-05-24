def print_table(table_data):
    """Prints a list of lists in a well-aligned table format."""
    # Find the maximum width of each column
    col_widths = [max(len(item) for item in column) for column in table_data]

    # Get number of rows from the length of the first column
    num_rows = len(table_data[0])

    print("\nFormatted Table:\n")
    for row_index in range(num_rows):
        for col_index in range(len(table_data)):
            item = table_data[col_index][row_index]
            print(item.rjust(col_widths[col_index] + 2), end=' ')
        print()  # Newline after each row

def main():
    # Example table data (columns)
    table_data = [
        ['Name',   'Alice', 'Bob', 'Carol'],
        ['Age',    '24',    '19',  '32'],
        ['City',   'NY',    'LA',  'Chicago']
    ]

    print_table(table_data)

if _name_ == "_main_":
    main()