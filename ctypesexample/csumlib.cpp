#include <iostream>
#include <algorithm>

/** 
 * Compute the sum an array
 * @param n number of elements
 * @param array input array
 * @return sum
 */
extern "C" long long csum(int n, int *array)
{
    long long res = 0;
    //#pragma omp parallel for reduction(+:res)
    for (int i = 0; i < n; ++i)
    {
        res += array[i];
    }
    return res;
}

extern "C" double *add(double *a, double *b)
{
    double *res = new double[3];

    for (int i = 0; i < 3; ++i)
    {
        res[i] = a[i] + b[i];
    }

    return res;
}

extern "C" double *sub(double *a, double *b)
{
    double *res = new double[3];

    for (int i = 0; i < 3; ++i)
    {
        res[i] = a[i] - b[i];
    }

    return res;
}

/** 
 * Sort the array
 * @param array input array
 * @param n number of elements
 * @return sum
 */
extern "C" void csort(int n, double* array) {
    std::sort(array, array + n);
}
