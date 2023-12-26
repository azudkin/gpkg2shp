# gpkg to shp
It is batch converter from .gpkg files to .shp files

**gpkg2shp.py** is the module for transformation

**program_convert.py** is the main program

### Needed modules

**for *gpkg2shp.py***

1. geopandas - to read and write files
2. fiona - to make list of layers from .gpkg files

**for *program_convert.py***

1. os - to manage files
2. time - to the program process counting
3. progress.bar - for visualization of process

### How to use
1. download both files and put in nearby
2. install all modules
3. in program_convert.py set *path_in* as your directory with .gpkg files and and *path_out* as your destination folder for .shp files
4. !!!Important, that destination folder marked in *path_out* will be cleared!!!


