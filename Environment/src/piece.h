//
// Created by kubaa on 06/04/2023.
//

#ifndef ENVIRONMENT_PIECE_H
#define ENVIRONMENT_PIECE_H

#include <vector>
#include "types.h"

using namespace std;
using namespace environment;

namespace environment {

    class piece {
    public:
        /**
         * Returns bit mask for a given piece located at the very bottom of the bitboard
         *
         * @param pieceId Piece id
         * @param rotation Rotation of the piece
         * @return Bit mask for the requested piece
         */
        static ulong getPiece(int pieceId, int rotation);

        /**
         * Generates piece data
         */
        static void init();

        /**
         * Converts given piece to a flat vector
         *
         * @param pieceId Piece id
         * @param rotation Rotation of the piece
         * @return Piece as a flat vector
         */
        static vector<int> pieceToFlatVector(int pieceId, int rotation);
    private:
        /**
         * Stores generated piece masks
         */
        inline static ulong pieces[15][4];

        /**
         * Returns piece i, 0 <= i <= 14
         *
         * @param i Piece number
         * @return Piece
         */
        static vector<vector<int>> getPieceVector(int i);

        /**
         * Creates a new copy of the rotated piece
         *
         * @param piece Piece to rotated
         * @return New rotated piece
         */
        static vector<vector<int>> rotatePieceVector(const vector<vector<int>>& piece);

        /**
         * Converts the given piece to a bit mask
         *
         * @param piece Piece to convert
         * @return Bitmask
         */
        static ulong pieceVectorToUlong(const vector<vector<int>>& piece);
    };

} // enviroment

#endif //ENVIRONMENT_PIECE_H
