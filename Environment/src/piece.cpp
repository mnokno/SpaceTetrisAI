//
// Created by kubaa on 06/04/2023.
//

#include "piece.h"

namespace environment {

    /**
     * Returns bit mask for a given piece located at the very bottom of the bitboard
     *
     * @param pieceId Piece id
     * @param rotation Rotation of the piece
     * @return Bit mask for the requested piece
     */
    ulong piece::getPiece(int pieceId, int rotation) {
        return piece::pieces[pieceId][rotation];
    }

    /**
     * Generates piece data
     */
    void piece::init() {
        for (int i = 0; i < 15; i++){
            vector<vector<int>> p = getPieceVector(i);
            piece::pieces[i][0] = pieceVectorToUlong(p);
            for (int j = 0; j < 3; j++){
                p = rotatePieceVector(p);
                piece::pieces[i][j + 1] = pieceVectorToUlong(p);
            }
        }
    }

    /**
     * Returns piece i, 0 <= i <= 14
     *
     * @param i Piece number
     * @return Piece
     */
    vector<vector<int>> piece::getPieceVector(int i) {
        switch (i) {
            //Line
            case 0 : {
                vector<vector<int>> blocks = {{0, 0, 0}, {1, 1, 1}, {0, 0, 0}};
                return blocks;
            }
            //C
            case 1 : {
                vector<vector<int>> blocks = {{0, 0, 0}, {1, 1, 1}, {1, 0, 1}};
                return blocks;
            }
            //Plus
            case 2 : {
                vector<vector<int>> blocks = {{0, 1, 0}, {1, 1, 1}, {0, 1, 0}};
                return blocks;
            }
            //Dot
            case 3 : {
                vector<vector<int>> blocks = {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}};
                return blocks;
            }
            //Square
            case 4 : {
                vector<vector<int>> blocks = {{1, 1, 0}, {1, 1, 0}, {0, 0, 0}};
                return blocks;
            }
            //L
            case 5 : {
                vector<vector<int>> blocks = {{0, 0, 0}, {1, 1, 1}, {0, 0, 1}};
                return blocks;
            }
            //J
            case 6 : {
                vector<vector<int>> blocks = {{0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
                return blocks;
            }
            //S
            case 7 : {
                vector<vector<int>> blocks = {{0, 0, 0}, {0, 1, 1}, {1, 1, 0}};
                return blocks;
            }
            //Z
            case 8 : {
                vector<vector<int>> blocks = {{1, 1, 0}, {0, 1, 1}, {0, 0, 0}};
                return blocks;
            }
            //T
            case 9 : {
                vector<vector<int>> blocks = {{1, 0, 0}, {1, 1, 0}, {1, 0, 0}};
                return blocks;
            }
            //X
            case 10 : {
                vector<vector<int>> blocks = {{1, 0, 1}, {0, 1, 0}, {1, 0, 1}};
                return blocks;
            }
            //Corner
            case 11 : {
                vector<vector<int>> blocks = {{0, 0, 0}, {1, 1, 0}, {1, 0, 0}};
                return blocks;
            }
            //Inverse Corner
            case 12 : {
                vector<vector<int>> blocks = {{1, 0, 0}, {1, 1, 0}, {0, 0, 0}};
                return blocks;
            }
            //Diagonal
            case 13 : {
                vector<vector<int>> blocks = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
                return blocks;
            }
            //Double
            case 14 : {
                vector<vector<int>> blocks = {{0, 1, 0}, {0, 1, 0}, {0, 0, 0}};
                return blocks;
            }
            default: {
                vector<vector<int>> blocks = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
                return blocks;
            }
        }
    }

    /**
     * Converts given piece to a flat vector
     *
     * @param pieceId Piece id
     * @param rotation Rotation of the piece
     * @return Piece as a flat vector
     */
    vector<int> piece::pieceToFlatVector(int pieceId, int rotation) {
        vector<int> pieceFlatVector = {};

        vector<vector<int>> pieceVector = getPieceVector(pieceId);
        for (int i = 0; i < rotation; i++){
            pieceVector = rotatePieceVector(pieceVector);
        }

        for (ulong x = 0; x < 3; x++){
            for (ulong y = 0; y < 3; y++){
                pieceFlatVector.push_back(pieceVector[x][y]);
            }
        }

        return pieceFlatVector;
    }

    /**
     * Converts the given piece to a bit mask
     *
     * @param piece Piece to convert
     * @return Bitmask
     */
    ulong piece::pieceVectorToUlong(const vector<vector<int>> &piece) {
        ulong mask = 0;
        for (ulong x = 0; x < 3; x++){
            for (ulong y = 0; y < 3; y++){
                if (piece[x][y] == 1){
                    mask |= ((ulong)1) << (x + y * 7);
                }
            }
        }
        return mask;
    }

    /**
     * Creates a new copy of the rotated piece
     *
     * @param piece Piece to rotated
     * @return New rotated piece
     */
    vector<vector<int>> piece::rotatePieceVector(const vector<vector<int>>& piece) {
        vector<vector<int>> blocks = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        blocks[2][0] = piece[0][0];
        blocks[1][0] = piece[0][1];
        blocks[0][0] = piece[0][2];

        blocks[2][1] = piece[1][0];
        blocks[1][1] = piece[1][1];
        blocks[0][1] = piece[1][2];

        blocks[2][2] = piece[2][0];
        blocks[1][2] = piece[2][1];
        blocks[0][2] = piece[2][2];
        return blocks;
    }

} // enviroment