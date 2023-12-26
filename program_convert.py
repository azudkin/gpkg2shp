import os
import time
from progress.bar import IncrementalBar
from gpkg2shp import to_shp

path_in = "/gpfs/glad1/Peter/Depot/Martin_Brandt_Africa_Tree_Cover/downloaded"
path_out = 'shp_result'

#clearing output directory
list_files = os.listdir(path_out)
if list_files:
    print(f'Deleting old files in {path_out}')
    bar = IncrementalBar('Countdown', max = len(list_files))

    for i in list_files:
        if '.' in i: os.remove(os.path.join(path_out, i))
        bar.next()

    bar.finish()

#saving files from gpkg to shp from input directory
print('Process ongoing...')
files = [(path_in + '/' + file) for file in os.listdir(path_in) if '.gpkg' in file]
bar = IncrementalBar('Countdown', max = len(files))
count_start = time.time()

for file in files:
    #print(file)
    to_shp(file, path_out)    
    bar.next()
    
    

bar.finish()
count_fin = time.time()
print('Total time:',(count_fin - count_start)/(60*60), 'hours')

