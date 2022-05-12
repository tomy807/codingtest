#include <iostream>
#include <cmath>
using namespace std;
int answer=0;
int n=0;
int arr[15];


bool promising(int x){
    for (int i = 0; i < x; i++)
    {
        if (arr[x]==arr[i] || abs(i-x)==abs(arr[x]-arr[i]))
        {
           return false;
        }

    }
    return true;
    
}

void dfs(int x){
    if (x==n)
    {
        answer++;
    }else{
        for (int i = 0; i < n; i++)
        {
            arr[x]=i;
            if (promising(x))
            {
                dfs(x+1);
            }
            
        }
        
    }
    
}
int main(){
    cin>>n;
    dfs(0);
    cout << answer;
    return 0;
}
