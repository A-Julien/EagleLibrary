# EagleLibrary

A simple Kicad Library (Schematic and FootPrint)

## Library Structure :
```
project
│   README.md       
│───Category
│   └───SubCategory
│       └───Constructor
│   	      └─DataSheet
│             SubCategory_Constructor.libr
│             Readme.md (list available devices in lib)
```
 
#### To get all componant name of a lib : 

```
cat LIBNAME | grep "package name=" | cut -c16- | rev | sed 's/$/ -/' | rev
```
