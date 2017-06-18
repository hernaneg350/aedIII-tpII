#include <vector>
#include "util.h"

#include "InstanceReader.h"

using namespace TPII;
using namespace std;

Graph InstanceReader::ReadFromInput(int n, int m, istream& inputStream)
{
    // Will add ghost 'source' edge connected to all vertices
    // for processing via Bellman-Ford.
    vector<Edge> edges(m + n);

    for (int iEdge = 0; iEdge < m; iEdge++)
    {
        string edgeString;
        getline(inputStream, edgeString);

        vector<string> edgeData = split(edgeString, ' ');
        int v1 = stoi(trim(edgeData[0]));
        int v2 = stoi(trim(edgeData[1]));
        int weight = stoi(trim(edgeData[2]));

        edges[iEdge] = Edge { v1, v2, weight };
    }

    for (int iVertex = 0; iVertex < n; iEdge++)
    {
        edges[m + iVertex] = Edge { 0, iVertex, 0 }
    }

    return Graph(n + 1, edges);
}
