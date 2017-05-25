#include "Graph.h"

using namespace TPII;
using namespace std;

Graph::Graph(const int n, const vector<Edge>& edges) :
    _n(n),
    _edgeList(edges)
{ }

int Graph::GetN() const
{
    return this->_n;
}

EdgeIterator Graph::Edges() const
{
    return this->_edgeList.begin();
}

bool Graph::IsLast(EdgeIterator edgeIterator) const
{
    return edgeIterator == this->_edgeList.end();
}
