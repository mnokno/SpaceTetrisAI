//
// Created by kubaa on 06/04/2023.
//

#ifndef ENVIRONMENT_PIECE_H
#define ENVIRONMENT_PIECE_H

#include <vector>
#include "types.h"

using namespace std;
using namespace environment;

namespace enviroment {

    class piece {
    public:
        static ulong getPiece(int pieceId, int rotation);
        static void init();
    private:
        inline static ulong pieces[16][4];
        static vector<bool> getPieceVector(int i);
        static vector<bool> rotatePieceVector(const vector<bool>& piece);
    };

} // enviroment

#endif //ENVIRONMENT_PIECE_H
