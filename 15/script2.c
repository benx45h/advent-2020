#include <stdio.h>
#include <stdlib.h>

int main() {

    int* nums;
    nums = (int*) calloc(30000001, sizeof(int));

    nums[0] = 8; nums[1] = 13; nums[2] = 1; nums[3] = 0, nums[4] = 18, nums[5] = 9;

    int last = 6;
    int len = 5;
    int age = -1;
    int timer = 0;
    int goal = 100000;
    float percent;
    for(int i = 7; i <= 30000000; i++) {
        if(timer > goal) {
            percent = ((float)timer) / 30000000.0;
            printf("Timer: %d, percent: %f\n",timer,percent);
            goal = goal + 100000;
        }
        age = -1;
        last = nums[i-2];
        for(int j = 1; j <= len; j++) {
            if(nums[i-2-j] == last) {
                age = j;
                break;
            }
        }

        if(age == -1) age = 0;

        nums[i-1] = age;
        len++;
        timer++;
//        printf("Turn: %d, num: %d\n",i,nums[i-1]);
    }

    printf("yeet %d\n",age);
}
