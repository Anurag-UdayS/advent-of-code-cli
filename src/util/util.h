// util.h
// Anurag Tewary
// 30 November, 2022

#include <stdio.h>
#include <time.h>

#ifndef error
	#define error(msg) fprintf(stderr, "%c[31m[  ERROR  ]: %s%c[0m\n", 27, msg, 27)
#endif

#ifndef warn
	#define warn(msg) fprintf(stderr, "%c[33m[ WARNING ]: %s%c[0m\n", 27, msg, 27)
#endif

#ifndef debug
	#define debug(msg) fprintf(stderr, "%c[35m[  DEBUG  ]: %s%c[0m\n", 27, msg, 27)
#endif


extern int getyear() {
	time_t _time;
	time(&_time);
	return localtime(&_time)->tm_year + 1900;
}