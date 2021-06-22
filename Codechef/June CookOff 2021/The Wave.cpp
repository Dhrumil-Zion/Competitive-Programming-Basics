#include<bits/stdc++.h>
using namespace std;
#define variable long long

int main(){
    variable no_of_roots,queries;
    cin>>no_of_roots>>queries;
    variable arr[no_of_roots];
    for(variable i=0;i<no_of_roots;i++)
        cin>>arr[i];
    sort(arr,arr+no_of_roots);
    for(variable i=0;i<queries;i++){
        variable x;
        cin>>x;
        variable pos=lower_bound(arr,arr+no_of_roots,x)-arr;
        if(pos<no_of_roots && arr[pos]==x)
            cout<<0<<endl;
        else if(pos%2==0)
            cout<<"POSITIVE"<<endl;
        else
            cout<<"NEGATIVE"<<endl;
    }
}

// # a = [1,234,3,4,5]
// # import bisect
// # print(bisect.bisect_left(a,3))
