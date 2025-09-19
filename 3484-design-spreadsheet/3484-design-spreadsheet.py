class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        # Store cell values in a dictionary: keys are cell refs like 'A1', values are integers
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        # Reset the cell value to 0 (removing from dictionary to save space)
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        # formula is always in the format "=X+Y"
        # Remove the '=' at start
        expr = formula[1:]
        left, right = expr.split('+')

        def get_val(token: str) -> int:
            # Return the integer value if token is a digit, else get the cell value (default 0)
            if token.isdigit():
                return int(token)
            else:
                return self.cells.get(token, 0)

        return get_val(left) + get_val(right)
