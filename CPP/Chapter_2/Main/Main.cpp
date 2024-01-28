// Chapter 2 Learnings from learncpp.com
#include <iostream>
#include "subtract.h"
#include "input.h"

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

int add(int x, int y); // Function Declaration

int main()
{
	std::cout << "Starting main()\n";
	doPrint();
	std::cout << return5() << '\n';
	int x = readUserInt();
	std::cout << "Double your number is: " << doubleNumber(x) << '\n';
	std::cout << add(10, 12) << '\n';
	std::cout << subtract(15, 10) << '\n';

	int a{ readNumber() };
	int b{ readNumber() };
	std::cout << "Adding your numbers together..\n";
	writeAnswer(a + b);

	std::cout << "Ending main()\n";
	return 0;
}

int add(int x, int y)
{
	return x + y;
}