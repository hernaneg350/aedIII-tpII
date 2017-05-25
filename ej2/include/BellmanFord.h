#pragma once

#include <limits>

#include "Graph.h"

const int INFINITY = std::numeric_limits<int>::max();

namespace TPII
{
    class BellmanFord {
    private:
        const Graph& _graph;
        const int _weightModifier;
    public:
        BellmanFord(const Graph& graph, int weightModifier);
        bool HasNegativeCycles() const;
    };
}
