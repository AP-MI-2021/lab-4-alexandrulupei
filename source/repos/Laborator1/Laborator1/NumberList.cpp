#include "NumberList.h"
#include <iostream>

void NumberList::Init()
{
	this -> count = 0;
}
bool NumberList::Add(int x)
{
	if(count >= 10)
		return false;
	this->numbers[this->count] = x;
	this->count++;
	return true;

}
void NumberList::Sort()
{
	bool sorted;
	int temp;
	do {
		sorted = true;
		for (int index = 0; index < this->count - 1; index++)
		{
			if (this->numbers[index] > this->numbers[index + 1])
			{
				temp = this->numbers[index];
				this->numbers[index] = this->numbers[index + 1];
				this->numbers[index + 1] = temp;
				sorted = false;
			}
		}
	} while (!sorted);
}
void NumberList::Print()
{
	for (int index = 0; index < this->count; index++)
	{
		std::cout << this->numbers[index] << " ";
	}
	std::cout << std::endl;
}