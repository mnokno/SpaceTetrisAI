class PrecalculatedData:
    """
    Stores precalculated data, improves preference by avoiding repeated calculations curing runtime
    """

    columnBitmasks: list[int] = [0] * 5
    """
    Stores bitmasks for columns
    """

    rowBitmasks: list[int] = [0] * 5
    """
    Stores bitmasks for rows
    """

    boardBitmask: int = 0
    """
    Stores a bitmask for the game board
    """

    @staticmethod
    def init() -> None:
        """
        Precalculates all required data
        """
        PrecalculatedData.__precalculate_row_data()
        PrecalculatedData.__precalculate_column_data()
        PrecalculatedData.__precalculate_board_data()

    @staticmethod
    def __precalculate_row_data() -> None:
        """
        Precalculates row data
        """
        row_start = 1
        column_start = 1

        for row in range(5):
            mask = 0
            for column in range(5):
                mask |= (1 << (row_start + row + (column_start + column) * 7))
            PrecalculatedData.rowBitmasks[row] = mask

    @staticmethod
    def __precalculate_column_data() -> None:
        """
        Precalculates column data
        """
        row_start = 1
        column_start = 1

        for column in range(5):
            mask = 0
            for row in range(5):
                mask |= (1 << (row_start + row + (column_start + column) * 7))
            PrecalculatedData.columnBitmasks[column] = mask

    @staticmethod
    def __precalculate_board_data() -> None:
        """
        Precalculates column data
        """
        mask = 0
        for row in PrecalculatedData.rowBitmasks:
            mask |= row
        PrecalculatedData.boardBitmask = mask
        