#include <iostream>
#include <cmath>
#define M_PI 3.14159265358979323846
# define degToRad (M_PI/180.0)

//create a function that computes factorial
double factorial(int n)
{
    int m =1;
    while (n>0)
    {
        m *= n;
        n--;
    }
    return double(m);
}

//functions generatesthe (n+1)th termof the expression
double generalTerm(double angle,int n)
{
    // n starts at zero
    return ( (pow(-1, n)) * (pow(angle, (2*n+1))) / factorial(2*n + 1));
}

double absolute(float n)
{
    return n > 0? n : -n;
}

int main()
{
    int n=0;
    double calculated_value = generalTerm(30*degToRad, n);
    while (absolute(sin(30*degToRad) - calculated_value) > 0.000001 )
    {
        n++;
        calculated_value += generalTerm(30*degToRad, n);
    }
    std::cout << std::endl << n+1 << " terms are needed." << std::endl;
    return 0;
}
