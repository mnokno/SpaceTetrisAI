#include <iostream>
#include "src/types.h"
#include "src/piece.h"

std::string formatBoard(ulong number);

using namespace environment;

int main() {
    std::cout << "Hello, World!" << std::endl;
    piece::init();
    std::cout << formatBoard(piece::getPiece(14, 3)) << std::endl;
    return 0;
}

std::string formatBoard(ulong number) {
    std::string formatted = "";
    for (ulong i = 0; i < 6; i++){
        std::string line = "";
        for (ulong j = 0; j < 7; j++){
            if ((number & ((ulong)1 << (j + i * 7))) == (ulong)1 << (j + i * 7)){
                line = line + "1";
            }
            else{
                line = line + "0";
            }
        }
        formatted = line + "\n" + formatted;
    }
    return formatted;
}

