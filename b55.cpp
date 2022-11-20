#include <iostream>
#include <set>
using namespace std;
int main() {
    long long Q, QueryType[100009], x[100009];
    cin >> Q;
    for (int i=1; i<=Q; i++) cin >> QueryType[i] >> x[i];

    set<long long> S;
    set<long long> S_m;
    for (int i=1; i<=Q; i++) {
        if (QueryType[i]==1) {
            S.insert(x[i]);
            S_m.insert(-x[i]);
        }
        else if (QueryType[i]==2) {
            long long ans = 0;  // intじゃオーバーフロー
            if (S.size()==0) ans = -1;
            else {
                auto itr2 = S.lower_bound(x[i]);
                auto itr1 = S_m.lower_bound(-x[i]);
                if (itr1 != S_m.end() && itr2 != S.end()) {
                    ans = (x[i]+*itr1)<=(*itr2-x[i]) ? x[i]+*itr1 : *itr2-x[i];
                } 
                else if (itr1 != S_m.end()) ans = x[i]+*itr1;
                else if (itr2 != S.end()) ans = *itr2-x[i];
            }
            cout << ans << endl;
        }
    }
    return 0;
}