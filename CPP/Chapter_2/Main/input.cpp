#include <iostream>
#include "input.h"

int readUserInt()
{
	std::cout << "Enter an integer: ";
	int userInt{};
	std::cin >> userInt;
	return userInt;
}

int readNumber()
{
	std::cout << "Enter an integer: ";
	int a{};
	std::cin >> a;
	return a;
}

void writeAnswer(int a)
{
	std::cout << "The answer is: " << a << '\n';
}