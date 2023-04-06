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
        static ulong getPiece(int pieceId, int rotation);

        /**
         * Generates piece data
         */
        static void init();
    private:
        /**
         * Stores generated piece masks
         */
        inline static ulong pieces[16][4];

        /**
         * Returns piece i, 0 <= i <= 15
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
