#include <iostream>
#include <vector>
#include <string>

#include "BellmanFord.h"
#include "InputReader.h"
#include "util.h"

using namespace std;
using namespace TPII;

int searchSolution(Graph& instance)
{
    int maxTollboothCost = std::numeric_limits<int>::min();
    for (EdgeIterator edgeIt = instance.Edges(); !instance.IsLast(edgeIt); ++edgeIt)
    {
        Edge edge = *edgeIt;
        if (edge.weight > maxTollboothCost)
        {
            maxTollboothCost = edge.weight;
        }
    }

    if (maxTollboothCost == 0)
    {
        return 0;
    }

    // Busqueda binaria sobre los posibles costos
    int leftBoundary = -1;
    int rightBoundary = maxTollboothCost + 1;
    while (rightBoundary - leftBoundary > 1)
    {
        int middle = leftBoundary + (rightBoundary - leftBoundary) / 2;

        BellmanFord bellmanFordImpl(instance, -middle);

        if (bellmanFordImpl.HasNegativeCycles(0))
        {
            rightBoundary = middle;
        }
        else
        {
            leftBoundary = middle;
        }
    }

    return leftBoundary;
}

int main()
{
    InputReader inputReader;
    vector<Graph> instances = inputReader.ReadFromInput(cin);

    for (vector<Graph>::iterator instanceIt = instances.begin(); instanceIt != instances.end(); ++instanceIt)
    {
        int solution = searchSolution(*instanceIt);
        cout << to_string(solution) << endl;
    }
}
