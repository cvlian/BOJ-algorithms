/*
    Segment Tree
*/

#include "segTree.h"
#include <algorithm>

namespace boj
{

    void segTree::init(int n, int v)
    {
        while (n*2 > size) size *= 2;
        init_val = v;
        std::fill(a, a+size, init_val);
    }

    int segTree::fill(int p)
    {
        if (p >= size/2) return a[p];

        a[p] = fill(2*p) + fill(2*p+1);
        return a[p];
    }

    int segTree::cal(int p, int L, int R, int nodeL, int nodeR)
    {
        if (R < nodeL || nodeR < L)
            return init_val;
        if (L <= nodeL && nodeR <= R)
            return a[p];

        int m = (nodeL + nodeR)/2;
        return cal(2*p, L, R, nodeL, m) + cal(2*p + 1, L, R, m + 1, nodeR);
    }

    void segTree::update(int p, int v)
    {
        p += size/2 - 1;
        a[p] = v;

        while (p > 1)
        {
            p /= 2;
            a[p] = a[2*p] + a[2*p + 1];
        }
    }

}
