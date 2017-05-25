#pragma once

#include <iostream>

#include "Graph.h"
#include "util.h"

using namespace std;

namespace TPII
{
    class InputReader
    {
    public:
        vector<Graph> ReadFromInput(istream& inputStream);
    };
}
