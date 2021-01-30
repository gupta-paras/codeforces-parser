#include <bits/stdc++.h>
using namespace std;

const int N = 1<<18; // 2.5e6

int t[N<<1], lazy[N<<1];
string s, f;

void build(int id, int l, int r){
    if (l+1==r){
        t[id] = f[l] - '0';
        return;
    }
    int mid = (l+r) / 2;
    build(id*2, l, mid);
    build(id*2 + 1, mid, r);

    t[id] = t[id*2] + t[id*2+1];
    lazy[id] = -1;
}

void change(int id, int l, int r, char d){
    if (d >= '0') lazy[id] = d - '0';
    if (d >= '0') t[id] = (r-l)* (d - '0');
}

void push(int id, int l, int r){
    int mid = (l + r) / 2;
    change(id*2 , l, mid, '0' + lazy[id]);
    change(id*2+1 , mid, r, '0' + lazy[id]);
    lazy[id] = -1;
}

void upd(int id , int l, int r, int x, int y, char d){
    if (r <= x || l >=y) return;
    if (x <=l && y >=r) {
        change(id, l, r, d);
        return;
    }
    push(id, l, r);
    int mid = (l + r) >> 1;
    upd(id*2, l, mid, x, y, d);
    upd(id*2+1, mid, r, x, y, d);
    t[id] = t[id*2+1] + t[id*2];
}

int query(int id, int l, int r, int x, int y){
    if (r <= x || l >=y) return 0;
    if(x <= l && r <= y)	return t[id];
    push(id, l, r);
    int mid = (l + r) / 2;
    return query(id*2, l, mid, x, y) + query(id*2 + 1, mid, r, x, y);
}