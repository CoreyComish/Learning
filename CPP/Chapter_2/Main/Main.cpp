// Chapter 2 Learnings from learncpp.com
#include <iostream>

void doPrint()
{
	std::cout << "In doPrint()\n";
}

int return5()
{
	return 5;
}

int doubleNumber(int num)
{
	return num * 2;
}

int readUserInt()
{
	std::cout << "Enter an integer: ";
	int userInt{};
	std::cin >> userInt;
	return userInt;
}

int main()
{
	std::cout << "Starting main()\n";
	doPrint();
	std::cout << return5() << '\n';
	int x = readUserInt();
	std::cout << "Double your number is: " << doubleNumber(x) << '\n';
	std::cout << "Ending main()\n";
	return 0;
}