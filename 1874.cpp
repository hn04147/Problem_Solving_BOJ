#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main(){
    int length;
    cin >> length;
    int *array = new int[length];
    stack<int> arr;
    vector<char> answer;
    int number = 1;

    for (int i=0; i<length; i++){
        int index;
        cin >> index;
        array[i] = index;
    }

    for (int i=0; i<length; i++){
        while(1){
            if (arr.empty() || arr.top()!=array[i]){
                arr.push(number);
                number++;
                answer.push_back('+');
            }
            else if (arr.top() == array[i]){
                arr.pop();
                answer.push_back('-');
                break;
            }
        }
    }

    for (int i=0; i<answer.size(); i++){
        cout<<answer[i]<<endl;
    }
}
