#include <iostream>
#include <tuple>
#include <string>
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

int main() {
    string nString;
    getline(cin, nString);
    int n = stoi(nString);

    vector<tuple<int, int, int>> constructionQueue;
    vector<tuple<int, int, int>> destructionQueue;

    for (int i = 0; i < (n*(n - 1)) / 2; i++) {
        string edgeString;
        getline(cin, edgeString);

        vector<string> edgeData = split(edgeString, ' ');

        int c1 = stoi(trim(edgeData[0]));
        int c2 = stoi(trim(edgeData[1]));
        int isPresent = (bool)stoi(trim(edgeData[2]));
        int cost = stoi(trim(edgeData[3]));

        vector<tuple<int, int, int>>* queue;

        if (isPresent) {
            queue = &destructionQueue;
        } else {
            queue = &constructionQueue;
        }

        queue->push_back(make_tuple(c1, c2, cost));
    }

    sort(constructionQueue.begin(), constructionQueue.end(), sortConstructionQueue);
    sort(destructionQueue.begin(), destructionQueue.end(), sortDestructionQueue);

    DisjointSet UDS(n);
    int min = 0;

    for (vector<tuple<int, int, int>>::iterator it = destructionQueue.begin(); it != destructionQueue.end(); ++it) {
        int v1 = get<0>(*it);
        int v2 = get<1>(*it);

        if (UDS.find(v1) != UDS.find(v2)) {
            UDS.setUnion(v1, v2);
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
        }
    }

    cout << min << endl;
}
