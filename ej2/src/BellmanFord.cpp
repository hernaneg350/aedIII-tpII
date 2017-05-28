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
    const int n = this->_graph.GetN();
    vector<int> distance(n, INFINITY);
    vector<bool> processed(n, false);

    bool graphHasNegativeCycles = false;
    bool ranThroughAllGraph = false;
    int nextSource = 0;

    while (!graphHasNegativeCycles && !ranThroughAllGraph)
    {
        graphHasNegativeCycles = this->Run(distance, processed, nextSource);

        ranThroughAllGraph = true;
        for (int vertex = 0; ranThroughAllGraph && vertex < n; vertex++)
        {
            ranThroughAllGraph = processed[vertex];
            nextSource = vertex;
        }
    }

    return graphHasNegativeCycles;
}

bool BellmanFord::Run(vector<int>& distance, vector<bool>& processed, int source) const
{
    const int n = this->_graph.GetN();

    int iVertex = 0;
    distance[source] = 0;
    bool distanceModified = true;
    while (distanceModified && iVertex < n - 1)
    {
        distanceModified = false;
        for (EdgeIterator edgeIt = this->_graph.Edges(); !this->_graph.IsLast(edgeIt); ++edgeIt)
        {
            Edge edge = *edgeIt;
            int edgeWeight = edge.weight + this->_weightModifier;
            int v1 = edge.v1 - 1;
            int v2 = edge.v2 - 1;

            // An end has been previously processed by another run of
            // Bellman-Ford. Don't need to process this edge.
            if (processed[v1] || processed[v2])
            {
                continue;
            }

            if (distance[v1] != INFINITY && distance[v1] + edgeWeight < distance[v2])
            {
                distance[v2] = distance[v1] + edgeWeight;
                processed[v2] = true;
                distanceModified = true;
            }
        }

        iVertex++;
    }

    return iVertex == n;
}
