#include <iostream>


int getNumber()
{
	std::cout << "Enter a number: ";
	int x{};
	std::cin >> x;
	return x;
}

constexpr bool isEven(int x)
{
	return (x % 2) == 0;
}

int main()
{
	// Chapter 6.3, Question #2
	int x{ getNumber() };
	bool y{ isEven(x) };
	if (y)
		std::cout << x << " is even\n";
	else
		std::cout << x << " is odd\n";

	std::cout << true && false << '\n';
	std::cout << true && true << '\n';
	std::cout << false && false << '\n';

	std::cout << true || false << '\n';
	std::cout << true || true << '\n';
	std::cout << false || false << '\n';
	
	
	return 0;
}