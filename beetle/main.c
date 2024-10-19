#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct Point {
    float x;
    float y;
};

void basic_calculator(int x, int y) {
    int division = 0;
    int multiplication = 1;
    int addition = 0;

    struct Point p1;
    p1.x = 3.6;
    p1.y = 7.4;

    addition = x + y;
    division = x / y;
    multiplication = x * y;

    printf("Added: %d - Divided: %d - Multiplied: %d\n", addition, division, multiplication);
}


void make_it_opposite(const char x[]) {

}

float* generate_speed_arr(int n){
    // Allocate memory for the array dynamically
    float* x = (float*)malloc(n * sizeof(float));
    // Check if memory allocation was successful
    if (x == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;  // Return NULL if memory allocation failed
    }
    srand(time(NULL));
    for(int i=0; i<n+1; ++i) {
        float scaled_value = 70.0 + ((180.0 - 70.0) * rand() / RAND_MAX);
        x[i] = scaled_value;
    }
    return x;
}


int main() {
    basic_calculator(10, 5);
    printf("Hello C. The Gigachad lang\n");
    int n = 5; // 8 byte?
       // Get the pointer to the dynamically allocated array
    float* speed_arr = generate_speed_arr(n);

    if (speed_arr != NULL) {
        for (int i = 0; i < n; ++i) {
            printf("speed_arr[%d] = %f\n", i, speed_arr[i]);
        }
           // Free the dynamically allocated memory
           free(speed_arr);
       }
    return 0;
}
