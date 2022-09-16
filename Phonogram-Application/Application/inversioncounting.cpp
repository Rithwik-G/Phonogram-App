#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<ll> tree(8 * 200000, 0);
ll n = 2 * 200000;
// function to build the tree
void build( ll arr[]) 
{ 
    // insert leaf nodes in tree
    for (ll i=0; i<n; i++)    
        tree[n+i] = arr[i];
      
    // build the tree by calculating parents
    for (ll i = n - 1; i > 0; --i)     
        tree[i] = tree[i<<1] + tree[i<<1 | 1];    
}
  
// function to update a tree node
void updateTreeNode(ll p, ll value) 
{ 
    // set value at position p
    tree[p+n] = value;
    p = p+n;
      
    // move upward and update parents
    for (ll i=p; i > 1; i >>= 1)
        tree[i>>1] = tree[i] + tree[i^1];
}
  
// function to get sum on llerval [l, r)
ll query(ll l, ll r) 
{ 
    ll res = 0;
      
    // loop to find the sum in the range
    for (l += n, r += n; l < r; l >>= 1, r >>= 1)
    {
        if (l&1) 
            res += tree[l++];
      
        if (r&1) 
            res += tree[--r];
    }
      
    return res;
}

int main() {
	ll t;
	cin >> t;

	for (ll i = 0; i < t; i++) {
		ll d, ans = 0;
		cin >> d;
		vector<ll> vec(d);
		
		for (ll i = 0; i < d; i++) {
			
			cin >> vec[i];
			
		}

		vector<ll> new_vec(d);
		iota(new_vec.begin(), new_vec.end(), 0);
		sort(new_vec.begin(), new_vec.end(), [&](ll u, ll v)
												{return vec[u] > vec[v];});

		for (auto l: new_vec) {
			ans += query(0, l);
			// cout << query(0, l) << endl;
			updateTreeNode(l, 1);
		}
		fill(tree.begin(), tree.end(), 0);
		cout << ans << endl;
	}


}