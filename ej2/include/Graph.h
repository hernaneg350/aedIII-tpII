#pragma once

#include <vector>
#include <tuple>

using namespace std;

namespace TPII
{
    struct Edge
    {
        int v1;
        int v2;
        int weight;
    };

    typedef vector<Edge>::const_iterator EdgeIterator;

    class Graph {
    private:
        const int _n;
        const vector<Edge> _edgeList;
    public:
        Graph(const int n, const vector<Edge>& edges);
        int GetN() const;
        EdgeIterator Edges() const;
        bool IsLast(EdgeIterator edgeIterator) const;
    };
}
