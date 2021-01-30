#include <bits/stdc++.h>
using namespace std;

const int N = 1e5+5;
vector<int>  adj[N];
vector<int> res;
vector<int> vis(N);

void has_cycle(){
    // some action on existence of the cycle
}

// post order traversal and append in the end
void bfs(int p, int u){
    if (vis[u]==1) {
        has_cycle();
        return;
    }
    if (vis[u]) return;
    vis[u] =1 ;
    for(int v: adj[u]){
        if (u==p) continue;
        topo(u, v);
    }
    vis[u] = 2;
    res.push_back(u);
}

void topo(int n){
    for(int i=1; i < n; i++){
        bfs(-1, i);
    }
}