#include <vector>
#include "util.h"

#include "InstanceReader.h"

using namespace TPII;
using namespace std;

Graph InstanceReader::ReadFromInput(int n, int m, istream& inputStream)
{
    vector<Edge> edges(m);
    for (int iEdge = 0; iEdge < m; iEdge++)
    {
        string edgeString;
        getline(inputStream, edgeString);

        vector<string> edgeData = split(edgeString, ' ');
        int v1 = stoi(trim(edgeData[0])) - 1;
        int v2 = stoi(trim(edgeData[1])) - 1;
        int weight = stoi(trim(edgeData[2]));

        edges[iEdge] = Edge { v1, v2, weight };
    }

    return Graph(n, edges);
}
