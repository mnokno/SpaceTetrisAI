class Piece:
    """
    Collection of utilities regarding game pieces.
    """

    # Stores generated piece data
    pieces: [[int]] = [[0] * 4 for _ in range(15)]

    @staticmethod
    def get_piece(piece_id: int, rotation: int):
        """
        Returns bitmask for a given piece located at the very bottom of the bitboard.

        :param piece_id: ID of the piece
        :param rotation: Rotation of the piece
        :return: Bitmask corresponding to the piece
        """
        return Piece.pieces[piece_id][rotation]

    @staticmethod
    def init() -> None:
        """
        Generates piece data, should be called before any other piece utilitea are used.
        """
        for i in range(15):
            p = Piece.get_piece_vector(i)
            Piece.pieces[i][0] = Piece.piece_vector_to_ulong(p)
            for j in range(3):
                p = Piece.rotate_piece_vector(p)
                Piece.pieces[i][j + 1] = Piece.piece_vector_to_ulong(p)

    @staticmethod
    def piece_vector_to_ulong(piece: [[int]]) -> int:
        """
        Converts the given piece vector to a bitmask.

        :param piece: Piece to convert to a bitmask
        :return: Bitmask of the given piece
        """
        mask = 0
        for x in range(3):
            for y in range(3):
                if piece[x][y] == 1:
                    mask |= (1 << (x + y * 7))
        return mask

    @staticmethod
    def piece_to_flat_vector(piece_id: int, rotation: int):
        """
        Converts given piece to a flat vector/list.

        :param piece_id: Piece id
        :param rotation: Rotation of the piece
        :return: Flat vector for the given piece
        """
        piece_flat = []

        piece_vector = Piece.get_piece_vector(piece_id)
        for i in range(rotation):
            piece_vector = Piece.rotate_piece_vector(piece_vector)

        for x in range(3):
            for y in range(3):
                piece_flat.append(piece_vector[x][y])

        return piece_flat

    @staticmethod
    def get_piece_vector(i: int) -> [[int]]:
        """
        Returns piece with given id i, 0 <= i <= 14.

        :param i: Piece id
        :return: Piece
        """
        # Line
        if i == 0:
            return [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        # C
        elif i == 1:
            return [[0, 0, 0], [1, 1, 1], [1, 0, 1]]
        # Plus
        elif i == 2:
            return [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        # Dot
        elif i == 3:
            return [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        # Square
        elif i == 4:
            return [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        # L
        elif i == 5:
            return [[0, 0, 0], [1, 1, 1], [0, 0, 1]]
        # J
        elif i == 6:
            return [[0, 0, 1], [1, 1, 1], [0, 0, 0]]
        # S
        elif i == 7:
            return [[0, 0, 0], [0, 1, 1], [1, 1, 0]]
        # Z
        elif i == 8:
            return [[1, 1, 0], [0, 1, 1], [0, 0, 0]]
        # T
        elif i == 9:
            return [[1, 0, 0], [1, 1, 0], [1, 0, 0]]
        # X
        elif i == 10:
            return [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        # Corner
        elif i == 11:
            return [[0, 0, 0], [1, 1, 0], [1, 0, 0]]
        # Inverse Corner
        elif i == 12:
            return [[1, 0, 0], [1, 1, 0], [0, 0, 0]]
        # Diagonal
        elif i == 13:
            return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        # Double
        elif i == 14:
            return [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
        else:
            return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    @staticmethod
    def rotate_piece_vector(piece: [[int]]) -> [[int]]:
        """
        Rotates a 3x3 piece vector clockwise.

        :param piece: Piece to rotate
        :return: New rotated piece
        """
        # Transpose the piece vector
        piece_transpose = list(map(list, zip(*piece)))
        # Reverse each row of the transposed piece vector
        rotated_piece = [row[::-1] for row in piece_transpose]
        return rotated_piece
