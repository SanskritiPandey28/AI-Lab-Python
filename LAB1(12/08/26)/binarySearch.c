#include<stdio.h>
int binarySearch(int arr[], int i, int j, int k){
int mid;
if(i==j){
    if(arr[i]== k){
        return(i);
    }else return -1;
}
else{
    mid = (i+j)/2;
}
if(arr[mid]==k){
    return mid;
}
else if(arr[mid]>k){
    return binarySearch(arr, i, mid-1,k);

}
else{
    return binarySearch(arr, mid+1,j,k);
    
}
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
    int result = binarySearch(arr,0,n,7);
    printf("Result %d " , result);
    return 0;
}