#include <iostream>

void printValue(int value)
{
    std::cout << value << '\n';
}

void a()
{
	std::cout << "a() called\n";
}

void b()
{
	std::cout << "b() called\n";
	a();
}

int readNumber()
{
	int x{};
	std::cout << "Please enter a number: ";
	std::cin >> x;
	return x;
}

void writeAnswer(int x)
{
	std::cout << "The sum is: " << x << '\n';
}

int readNumber2()
{
	std::cout << "Please enter a number: ";
	int x{};
	std::cin >> x;
	return x;
}

void writeAnswer2(int x)
{
	std::cout << "The quotient is: " << x << '\n';
}

int main()
{
    printValue(5);

	int x{ 1 };
	std::cout << x << ' ';

	x = x + 2;
	std::cout << x << ' ';

	x = x + 3;
	std::cout << x << ' ';

	a();
	b();

	x = readNumber() + readNumber();
	writeAnswer(x);

	int y{ };
	x = readNumber2();
	y = readNumber2();
	writeAnswer2 (x / y);

    return 0;
}