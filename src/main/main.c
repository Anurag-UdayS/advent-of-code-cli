// main.c
// Anurag Tewary
// 30 November, 2022

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <time.h>
#include <dirent.h>
#include <sys/stat.h>
#include <errno.h>

#include "../util/util.h"


// Function to make a event directory

int mkevent(int year, char parentDirname[]) {

	// Validate year.
	if (year < 2000 || year > 2100) {
		error("Invalid year value provided. Please provide a valid year.");
		return 1;
	}

	if (year < 2015) {
		error("No event exists before 2015.");
		return 1;
	}

	if (year > getyear()) {
		warn("Creating event folder for future. Some API features may not be available.");
	}

	// Creating the folder and settings file.
	// TODO: Interface implementing its features.

	char dirname[strlen(parentDirname) + 4];
	char filename[strlen(parentDirname) + 4 + 12 + 1]; // 4 = year, 12 = /.aocsettings
	char syear[4];
	sprintf(syear, "%d", year);
	
	strcpy(dirname, parentDirname);		// strcpy(DEST, SRC)
	strcat(dirname, "/");				// strcat(DEST, SRC)
	strcat(dirname, syear);

	strcpy(filename, dirname);
	strcat(filename, "/.aocsettings");

	DIR *ydir = opendir(dirname);
	
	if (ydir == NULL) {
		
		mkdir(dirname, 0777);
		if (errno) error(strerror(errno));		// Error handling
		ydir = opendir(dirname);

	}

	struct dirent *entry;
	char *token, currentFilename[100];
	int file_exists = 0;

	while ((entry = readdir(ydir)) != NULL) {
		token = strtok(entry -> d_name, "/");		// split
		
		while (token != NULL) {
			strcpy(currentFilename, token);
			token = strtok(NULL, " ");		// reads next token
		}

		filename == NULL ? error ("Null token.") : debug ("File not null.");
		
		char msg[12 + strlen(currentFilename)];
		sprintf(msg, "Filename = %s\n", currentFilename);
		debug(msg);

		if (!strcmp(currentFilename, ".aocsettings")) {
			error("Settings File Exists.");
			file_exists = 1;
			break;
		}
	}

	if (!file_exists) 
		fclose(fopen(filename,"w"));		// make file.

	closedir(ydir);


}

int main(int argc, char const *argv[]) {
	mkevent(5000, "../test");
	mkevent(2023, "../test");
	return 0;
}
