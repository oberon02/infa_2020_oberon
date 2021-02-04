#include <iostream>
#include<cmath>

/*
int main()
{

    double a;
    std::cin >> a;

    double b;
    std::cin >> b;

    double c = sqrt(a*a + b*b);
    std::cout << c << std::endl;

    return 0;
}
*/


/* упр 3
int main()
{
    double a;
    std::cin >> a;
    for(int i = 0; i < a; i++) {
            for(int j = 0; j < a - 1; j++) {
                std::cout << "*";
            }
            std::cout << "*" << std::endl;

    }
}
*/

/* упр 5
int main()
{
    double a;
    std::cin >> a;
    for(int i = 0; i < a; i++) {
            for(int j = 0; j < a - 1 - i; j++) {
                std::cout << "*";
            }
            std::cout << "*" << std::endl;

    }
}
*/

/* упр 4
int main()
{
    double a;
    std::cin >> a;
    for(int i = 0; i < a; i++) {
            for(int j = 0; j < i; j++) {
                std::cout << "*";
            }
            std::cout << "*" << std::endl;

    }
}
*/

/* упр 6
int main()
{
    double a;

    std::cin >> a;
    for(int i = 0; i < a / 2; i++) {
            for(int j = 0; j < i; j++) {
                std::cout << " ";
            }
            for(int j = 0; j < a - 1 - 2 * i; j++) {
                std::cout << "*";
            }
            std::cout << "*" << std::endl;

    }
}
*/
