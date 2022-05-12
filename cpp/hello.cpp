#include <iostream>
#include <string.h>

using namespace std;

int main(){
    // int num=42;
    // int& ref = num;
    // const int& kRef = num;
    // ref=0;
    // cout << ref << " " << num << " " << kRef << endl;
    // num=42;    
    // cout << ref << " " << num << " " << kRef << endl;
    // return 0;
    char filename[] ="00205.txt";
    char *pch;
    pch=strtok(filename,".");
    printf("%s\n",pch);
    while(pch!=NULL){
        printf("%s\n",pch);
        pch=strtok(NULL,".");
    }
    return 0;

}