#include <bits/stdc++.h>
using namespace std;

const int N = 3e5+5;
int64_t t[N];

void update(int idx, int val=1)){
    idx++;
    while(idx<N){
        t[idx]+=val;
        idx+=idx&(-idx);
    }
}

int64_t query(int idx{
    int64_t res = 0;
    while(idx>0){
        res+=t[idx];
        idx-=idx&(-idx);
    }
    return res;
}