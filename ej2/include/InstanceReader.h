#pragma once

#include <iostream>

#include "Graph.h"

namespace TPII
{
    class InstanceReader
    {
    public:
        Graph ReadFromInput(int n, int m, istream& inputStream);
    };
}
