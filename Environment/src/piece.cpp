//
// Created by kubaa on 06/04/2023.
//

#include "piece.h"

namespace enviroment {


    ulong piece::getPiece(int pieceId, int rotation) {
        return 0;
    }

    void piece::init() {

    }

    /**
     * Returns piece i, 0 <= i <= 15
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

    vector<vector<int>> piece::rotatePieceVector(const vector<vector<int>>& piece) {
        return {};
    }

} // enviroment