#include <bits/stdc++.h>
using namespace std;

const int N = 1e5+5;
vector<int> adj[N];

int vis[N];
int64_t d[N];

void bfs(int p){
    memset(vis, 0, sizeof vis);

    vis[p] = 1; d[p] = 0;
    queue<int> q; q.push(p);

    while(q.size()){
        int u = q.front(); q.pop();
        for(auto e: adj[u]){
            if (vis[e]) continue;
            q.push(e);
            vis[e] = 1; d[e] = d[u]+1;
        }
    }
}