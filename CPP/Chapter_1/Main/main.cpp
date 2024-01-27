#include <iostream>

// This is a single line comment

/*
This is a 
multi-line
comment
*/

int main()
{
	std::cout << "Hello world!";
	/*
	[[maybe_unused]]  int a, b; // two seperate int variables
	[[maybe_unused]]  int a2 = 5, b2 = 6;          // copy initialization
	[[maybe_unused]]  int c(7), d(8);        // direct initialization
	[[maybe_unused]]  int e{ 9 }, f{ 10 };     // direct brace initialization
	[[maybe_unused]]  int g = { 9 }, h = { 10 }; // copy brace initialization
	[[maybe_unused]]  int i{}, j{};            // value initialization
	*/
	return 0;
}