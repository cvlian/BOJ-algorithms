/*
    Segment Tree
*/

#define MAX 65536

namespace boj
{
    class segTree
    {

        private:

            int size = 1;
            int init_val;
            int a[MAX];

        public:

            segTree(int n, int init_val) { init(n, init_val); }

            void init(int n, int v);

            int fill(int p);

            int cal(int p, int L, int R, int nodeL, int nodeR);

            void update(int p, int v);

    };
}