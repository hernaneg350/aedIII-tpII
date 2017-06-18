#include <iostream>
#include <tuple>
#include <string>
#include <list>
#include "DisjointSet.h"
#include "util.h"

using namespace std;
using namespace TPII;

bool sortDestructionQueue (tuple<int, int, int> a, tuple<int, int, int> b) {
    return get<2>(a) > get<2>(b);
}

bool sortConstructionQueue (tuple<int, int, int> a, tuple<int, int, int> b) {
    return get<2>(a) < get<2>(b);
}

void run_solution(int n) {
    vector<tuple<int, int, int>> constructionQueue;
    vector<tuple<int, int, int>> destructionQueue;

    for (int i = 0; i < (n*(n - 1)) / 2; i++) {
        string edgeString;
        getline(cin, edgeString);

        vector<string> edgeData = split(edgeString, ' ');

        int c1 = stoi(trim(edgeData[0])) - 1;
        int c2 = stoi(trim(edgeData[1])) - 1;
        int isPresent = (bool)stoi(trim(edgeData[2]));
        int cost = stoi(trim(edgeData[3]));

        if (isPresent) {
            destructionQueue.push_back(make_tuple(c1, c2, cost));
        } else {
            constructionQueue.push_back(make_tuple(c1, c2, cost));
        }
    }

    sort(constructionQueue.begin(), constructionQueue.end(), sortConstructionQueue);
    sort(destructionQueue.begin(), destructionQueue.end(), sortDestructionQueue);

    DisjointSet UDS(n);
    int min = 0;
    list<tuple<int, int>> routes;

    for (vector<tuple<int, int, int>>::iterator it = destructionQueue.begin(); it != destructionQueue.end(); ++it) {
        int v1 = get<0>(*it);
        int v2 = get<1>(*it);

        if (UDS.find(v1) != UDS.find(v2)) {
            UDS.setUnion(v1, v2);
            routes.push_back(make_tuple(v1, v2));
        } else {
            int cost = get<2>(*it);
            min += cost;
        }
    }

    for (vector<tuple<int, int, int>>::iterator it = constructionQueue.begin(); it != constructionQueue.end(); ++it) {
        int v1 = get<0>(*it);
        int v2 = get<1>(*it);

        if (UDS.find(v1) != UDS.find(v2)) {
            int cost = get<2>(*it);
            min += cost;
            UDS.setUnion(v1, v2);
            routes.push_back(make_tuple(v1, v2));
        }
    }

    cout << min << " " << routes.size() << " ";

    for (list<tuple<int, int>>::iterator routeIt = routes.begin(); routeIt != routes.end(); ++routeIt)
    {
        tuple<int, int> route = *routeIt;
        cout << "c" << get<0>(route) << "1 " << "c" << get<1>(route) << "2 ";
    }

    cout << endl;
}

int main()
{
    bool keepReading = true;
    while (keepReading)
    {
        string instanceSizeString;
        getline(cin, instanceSizeString);

        vector<string> instanceSize = split(instanceSizeString, ' ');

        int n = stoi(trim(instanceSize[0]));

        if (n == -1)
        {
            keepReading = false;
            break;
        }

        run_solution(n);
    }
}
