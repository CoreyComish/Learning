#include <iostream>

int readUserInt()
{
	std::cout << "Enter an integer: ";
	int userInt{};
	std::cin >> userInt;
	return userInt;
}