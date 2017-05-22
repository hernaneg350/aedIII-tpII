#include <iostream>
#include "DisjointSet.h"

TPII::DisjointSet::DisjointSet(int n) {
    this->height = new int[n];
    this->parent = new int[n];

    for (int i = 0; i < n; i++) {
        this->height[i] = 1;
        this->parent[i] = i;
    }
}

TPII::DisjointSet::~DisjointSet() {
    delete this->height;
    delete this->parent;
}

int TPII::DisjointSet::find(int x) {
    if (this->parent[x] != x) {
        this->parent[x] = this->find(this->parent[x]);
    }

    return this->parent[x];
}

void TPII::DisjointSet::setUnion(int x, int y) {
    x = this->find(x);
    y = this->find(y);

    if (this->height[x] < this->height[y]) {
        this->parent[x] = y;
    } else {
        this->parent[y] = x;
    }

    if (this->height[x] == this->height[y]) {
        this->height[x]++;
    }
}
