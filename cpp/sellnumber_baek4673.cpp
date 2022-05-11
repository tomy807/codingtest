#include<iostream>
using namespace std;
int constructor(int num);
int main(){
    int nums[10001];
    for(int i=1;i<10001;i++){
        int tmp=constructor(i);
        if(tmp>=1 && tmp<10001){
            nums[tmp]=1;
        }
    }
    for(int i=1; i<10001;i++){
        if(nums[i]!=1){
            cout<< i <<endl;
        }
    }
    return 0;

}
int constructor(int n){
    int temp = n + n / 1000 + n % 1000 / 100 + n % 100 / 10 + n % 10;
    return temp;
}