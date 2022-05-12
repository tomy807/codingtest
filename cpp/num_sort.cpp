#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int n;
    cin >> n;
    int arr[n+1];
    for(int i=1;i<n+1;i++){
        int num;
        cin >> num;
        arr[n-i+1]=num;
    }
    for(int i=1;i<n+1;i++){
        cout << arr[i] << endl;
    }
    return 0;
}