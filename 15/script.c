#include <stdio.h>
#include <stdlib.h>

int main() {

    int* nums;
    int* hist;
    nums = (int*) calloc(30000000, sizeof(int));
    hist = (int*) calloc(30000000, sizeof(int));

    nums[0] = 8;
    nums[1] = 13;
    nums[2] = 1;
    nums[3] = 0;
    nums[4] = 18;

    hist[0] = 1;
    hist[1] = 2;
    hist[2] = 3;
    hist[3] = 4;
    hist[4] = 5;

    int len = 5;

    int last = 9;

    int timer = 0;
    int goal = 100000;
    int num = 0;


 //   for (int i = 7; i <2021; i++) {
    for (int i = 7; i < 30000001; i++) {
        timer++;
        if(timer > goal) {
            printf("Time: %d\n", timer);
            goal = goal + 100000;
        }

        int idx = -1;
        for(int j = 0; j < len; j++) {  // check if last in nums
            if(nums[j] == last){
                idx = j;
                break;
            }
        }

        if(idx == -1) {
            num = 0;
            nums[len] = last;
            hist[len] = (i - 1);
            len++;
        } else {
            num = i - 1 - hist[idx];
            hist[idx] = i - 1;
        }
        last = num;
    }
    printf("yeet %d\n",num);
}
