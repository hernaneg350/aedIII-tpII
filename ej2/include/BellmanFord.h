#pragma once

#include <limits>
#include <tuple>

#include "Graph.h"

const int INFINITY = std::numeric_limits<int>::max();

namespace TPII
{
    class BellmanFord {
    private:
        const Graph& _graph;
        const int _weightModifier;
        bool Run(vector<int>& distance, const int source) const;
    public:
        BellmanFord(const Graph& graph, int weightModifier);
        bool HasNegativeCycles(const int source) const;
    };
}
