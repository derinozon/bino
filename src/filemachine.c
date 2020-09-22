#include <sys/stat.h>

#include <stdlib.h>
#include <stdio.h>
#include <dirent.h>
#include <stdbool.h>
#include <string.h>

#include "filemachine.h"



bool DirectoryExists (char* path) {
	struct stat info;

	if (stat(path, &info) == 0 ) return true;
	else return false;
}

char* ReadFile (char* path) {
	FILE* file = fopen(path, "r");

	if (!file) {
		printf("file not found\n");
		return NULL;
	}

	fseek(file, 0L, SEEK_END);
	size_t numbytes = ftell(file);

	fseek(file, 0L, SEEK_SET);	

	char* buffer = (char*)calloc(numbytes, sizeof(char));	
	if (!buffer) {
		printf("buffer errors\n");
		return NULL;
	}
	fread(buffer, sizeof(char), numbytes, file);
	fclose(file);
	
	return buffer;
}

void WriteFile (char* path,char* content) {
	printf("opening file at \n");
	printf("%s",path);
	FILE* file = fopen(path, "w") ; 

    if (!file) { 
        printf("file not found\n");
		return;
    } 

    fputs(content, file) ;    
    fclose(file) ;
}

char* ListDirectory (char* path, bool showHidden) {
	DIR *d = opendir(path);
	struct dirent *dir;

	char* finalList = (char*) malloc(1024);
	if (d) {
	    while ((dir = readdir(d))) {
			char* d_name = dir->d_name;
			
			bool canPrint = !((strlen(d_name) == 1 && d_name[0] == '.')||(strlen(d_name) == 2 && d_name[0] == '.' && d_name[1] == '.'));
			if (canPrint) {
				canPrint = (showHidden)||(d_name[0] != '.');
			}
			if (canPrint) {
				strcat(finalList, d_name);
				strcat(finalList, "\n");
			}
	    }
	    closedir(d);
	}
	return finalList;
}