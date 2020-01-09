#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>
using namespace std;

int main(){
    priority_queue<int> pq;
    pq.push(3);
    pq.push(2);
    pq.push(4);
    while (!pq.empty()) {
        cout<<pq.top()<<" ";
        pq.pop();
    }
}
