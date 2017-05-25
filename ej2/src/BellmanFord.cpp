#include <vector>

#include "BellmanFord.h"

using namespace std;
using namespace TPII;

BellmanFord::BellmanFord(const Graph& graph, int weightModifier) :
    _graph(graph),
    _weightModifier(weightModifier)
{ }

bool BellmanFord::HasNegativeCycles() const
{
    int n = this->_graph.GetN();

    vector<int> distance(n, INFINITY);
    distance[0] = 0;

    int iVertex = 0;
    bool distanceModified = true;
    while (distanceModified && iVertex < n)
    {
        distanceModified = false;
        for (EdgeIterator edgeIt = this->_graph.Edges(); !this->_graph.IsLast(edgeIt); ++edgeIt)
        {
            Edge edge = *edgeIt;
            int edgeWeight = edge.weight + this->_weightModifier;
            int v1 = edge.v1 - 1;
            int v2 = edge.v2 - 1;

            if (distance[v1] != INFINITY && distance[v1] + edgeWeight < distance[v2])
            {
                distance[v2] = distance[v1] + edgeWeight;
                distanceModified = true;
            }
        }

        iVertex++;
    }

    return iVertex == n;
}
