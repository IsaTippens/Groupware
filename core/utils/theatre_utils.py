class TheatreUtils():
    @staticmethod
    def valid_seat(seat: str):
        """
            Checks if the seat is valid.

            E.g A1 is the first seat in the row A.

            A1 is valid, A0 is not valid.

            A11 is valid, AA1 is not valid.
        """
        if len(seat) < 2:
            return False
        row = seat[0]
        col = seat[1:]
        if not row.isalpha():
            return False
        if not col.isdigit():
            return False
        if int(col) < 1:
            return False
        return True
    
    @staticmethod
    def split_seat(seat: str):
        """
            Splits the seat into a row and column.

            E.g A1 is the first seat in the row A.
        """
        row = seat[0]
        col = seat[1:]
        return row, int(col)

    @staticmethod
    def letter_to_index(row_letter: str):
        """
            Converts a row letter to a row index.
            A => 0
            B => 1
            AA => 26
            AB => 27
            AAA => 702
        """
        row_index = 0
        for i in range(len(row_letter)):
            row_index += (ord(row_letter[i]) - 64) * 26 ** (len(row_letter) - i - 1)
        return row_index - 1
    
    @staticmethod
    def index_to_letter(row_index: int):
        """
            Converts a row index to a row letter.
            0 => A
            1 => B
            26 => AA
            27 => AB
            702 => AAA
        """
        row_letter = ""
        while row_index >= 0:
            row_letter = chr(row_index % 26 + 65) + row_letter
            row_index = int(row_index / 26) - 1
        return row_letter