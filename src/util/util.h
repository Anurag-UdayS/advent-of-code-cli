// util.h
// Anurag Tewary
// 30 November, 2022

#include <stdio.h>
#include <time.h>

#ifndef error
	#define error(msg) fprintf(stderr, "%c[31m%s%c[m\n", 27, msg, 27);
#endif


extern int getyear() {
	time_t _time;
	time(&_time);
	return localtime(&_time)->tm_year + 1900;
}