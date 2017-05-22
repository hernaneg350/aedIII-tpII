#pragma once

namespace TPII {
    class DisjointSet {
    private:
        int* height;
        int* parent;
    public:
        DisjointSet(int n);
        ~DisjointSet();
        int find(int x);
        void setUnion(int x, int y);
    };
}
