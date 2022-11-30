// main.c
// Anurag Tewary
// 30 November, 2022

#include <stdio.h>
#include <time.h>

#include "../util/util.h"


// Function to make a event directory

int mkevent(int year) {
	
	int cyear = getyear();
	printf("%d\n", cyear);


	// Validate year:
	if (year < 2000 || year > 2100) {
		error("Invalid year value provided. Please provide a valid year.");
		return -1;
	}

	if (year < 2015) {
		error("No event exists before 2015.");
		return -1;
	}



}

int main(int argc, char const *argv[]) {
	mkevent(5000);
	return 0;
}
