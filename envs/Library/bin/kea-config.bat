@echo off

IF "%1"=="" (
   echo kea-config.bat [OPTIONS]
   echo Options:
   echo     [--prefix]
   echo     [--version]
   echo     [--libs]
   echo     [--cflags]
   echo     [--includes]
   EXIT /B 1
) ELSE (
:printValue
    if "%1" neq "" (
	    IF "%1"=="--prefix" echo C:/Users/emili/OneDrive/Documents/projets/Weather_diffusion/earth/earth/envs/Library
	    IF "%1"=="--version" echo 1.5.0
	    IF "%1"=="--cflags" echo -IC:/Users/emili/OneDrive/Documents/projets/Weather_diffusion/earth/earth/envs/Library/include
	    IF "%1"=="--libs" echo -LIBPATH:C:/Users/emili/OneDrive/Documents/projets/Weather_diffusion/earth/earth/envs/Library/lib libkea.lib 
	    IF "%1"=="--includes" echo C:/Users/emili/OneDrive/Documents/projets/Weather_diffusion/earth/earth/envs/Library/include
		shift
		goto :printValue
    )
	EXIT /B 0
)
