#include<stdio.h>
int linearSearch(int arr[], int n, int k){
for(int i = 0;i<n;i++){
    if(arr[i]==k){
        return i;
    }
}
return -1;
}

int main(){
    int n;
    
    printf("Enter no of elements");
    scanf("%d", &n);
    int arr[n];
    printf("Enter elements of array");
    for(int i = 0; i<n;i++){
        scanf("%d", &arr[i]);
    }
    int result = linearSearch(arr,n,7);
    printf("Result %d " , result);
    return 0;
}