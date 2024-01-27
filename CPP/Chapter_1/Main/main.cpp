#include <iostream>

// The purpose of this file is to get comfortable with C++ Basics
// This file uses the teachings from Chapter 1 of learncpp.com

// This is a single line comment

/*
This is a 
multi-line
comment
*/

/*
int a, b; // two seperate int variables
int a2 = 5, b2 = 6;          // copy initialization
int c(7), d(8);        // direct initialization
int e{ 9 }, f{ 10 };     // direct brace initialization
int g = { 9 }, h = { 10 }; // copy brace initialization
int i{}, j{};            // value initialization
*/

int main()
{
	// Basic Output
	int x{ 5 };
	std::cout << "Hello world!\n";
	std::cout << 4 << '\n';
	std::cout << "Hello" << " again\n";
	std::cout << "x is equal to: " << x << '\n';

	// Basic Input and Output
	std::cout << "Enter two numbers, seperated by a space: ";
	int y{}, z{};
	std::cin >> y >> z;
	std::cout << "You entered: " << y << " and " << z << '\n';

	// 1.11 Task
	std::cout << "Enter an integer: ";
	int userInput{};
	std::cin >> userInput;
	std::cout << "Double that number is: " << userInput * 2 << '\n';
	std::cout << "Triple that number is: " << userInput * 3 << '\n';

	// 1.x Quiz Task
	int a{}, b{};
	std::cout << "Enter an integer: ";
	std::cin >> a;
	std::cout << "Enter an integer: ";
	std::cin >> b;
	std::cout << a << " + " << b << " is " << a + b << '\n';
	std::cout << a << " - " << b << " is " << a - b << '\n';

	return 0;
}