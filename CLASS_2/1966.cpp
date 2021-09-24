#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(){
    int test_case;
    cin>>test_case;
    for (int i=0; i<test_case; i++){
        int N, M;
        cin>>N>>M;
        queue<int> imp;
        queue<int> num;
        priority_queue<int> pq;
        vector<int> ans;
        for (int j=0; j<N; j++){
            int index;
            cin>>index;
            num.push(j+1);
            imp.push(index);
            pq.push(index);
        }
        while (num.size()!=1){
            if (imp.front()==pq.top()){
                pq.pop();
                imp.pop();
                int a = num.front();
                num.pop();
                ans.push_back(a);
            }
            else{
                int a = num.front();
                int b = imp.front();
                num.pop();
                imp.pop();
                num.push(a);
                imp.push(b);
            }
        }
        int a = num.front();
        ans.push_back(a);

        int key = M+1;
        int pri = 0;
        for (pri; pri<ans.size(); pri++){
            if (key==ans[pri]){
                cout<<pri+1<<endl;
                break;
            }
        }
    }
}
