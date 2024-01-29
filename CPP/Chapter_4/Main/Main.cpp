#include <iomanip> // for std::setw (which sets the width of the subsequent output)
#include <iostream>

bool isPrime(int x)
{
    if (x == 2 || x == 3 || x == 5 || x == 7)
        return true;
    else
        return false;
}

void printCharAndASCII(char x)
{
    std::cout << "You entered '" << x << "', which has ASCII code " << static_cast<int>(x) << '\n';
}

double getDouble()
{
    double x{};
    std::cout << "Enter a double value: ";
    std::cin >> x;
    return x;
}

char getChar()
{
    char x{};
    std::cout << "Enter +, -, *, or /: ";
    std::cin >> x;
    return x;
}

void calculate(double x, double y, char c)
{
    if (c == '+' || c == '-' || c == '*' || c == '/')
    {
        std::cout << x << ' ' << c << ' ' << y << " is ";
        if (c == '+')
            std::cout << x + y << '\n';
        if (c == '-')
            std::cout << x - y << '\n';
        if (c == '*')
            std::cout << x * y << '\n';
        if (c == '/')
            std::cout << x / y << '\n';
    }
    else
        std::cout << "Invalid operator\n";    
}

int getTowerHeight()
{
    int x{};
    std::cout << "Enter Tower Height in Meters: ";
    std::cin >> x;
    return x;
}

void calcHeight(int seconds, int towerHeight)
{
    double grav{ 9.8 };
    if (seconds == 0)
        std::cout << "At 0 seconds, the ball is at height: " << towerHeight << " meters\n";
    else
    {
        double height{ towerHeight - ((grav * (seconds * seconds)) / 2.0) };
        if (height > 0)
            std::cout << "At " << seconds << " seconds, the ball is at height: " << height << " meters\n";
        else
            std::cout << "At " << seconds << " seconds, the ball is on the ground\n";
    }
}

int main()
{
    std::cout << std::left; // left justify output
    std::cout << std::setw(16) << "bool:" << sizeof(bool) << " bytes\n";
    std::cout << std::setw(16) << "char:" << sizeof(char) << " bytes\n";
    std::cout << std::setw(16) << "short:" << sizeof(short) << " bytes\n";
    std::cout << std::setw(16) << "int:" << sizeof(int) << " bytes\n";
    std::cout << std::setw(16) << "long:" << sizeof(long) << " bytes\n";
    std::cout << std::setw(16) << "long long:" << sizeof(long long) << " bytes\n";
    std::cout << std::setw(16) << "float:" << sizeof(float) << " bytes\n";
    std::cout << std::setw(16) << "double:" << sizeof(double) << " bytes\n";
    std::cout << std::setw(16) << "long double:" << sizeof(long double) << " bytes\n";

    std::cout << "Enter a number 0 through 9: ";
    int x{};
    std::cin >> x;

    if (isPrime(x))
        std::cout << "The digit is prime\n";
    else
        std::cout << "The digit is not prime\n";

    std::cout << "Enter a single character: ";
    char a{};
    std::cin >> a;
    printCharAndASCII(a);

    double d1{ getDouble() };
    double d2{ getDouble() };
    char c{ getChar() };
    calculate(d1, d2, c);

    int towerHeight{ getTowerHeight()};
    calcHeight(0, towerHeight);
    calcHeight(1, towerHeight);
    calcHeight(2, towerHeight);
    calcHeight(3, towerHeight);
    calcHeight(4, towerHeight);
    calcHeight(5, towerHeight);

    return 0;
}