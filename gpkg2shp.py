import geopandas as gpd
import fiona

def to_shp(in_file, out_folder = '.', crs = 'EPSG:4626', out_ext = 'shp'):
    '''to_shp(in_file, out_folder = '.', crs = 'EPSG:4626' out_ext = 'shp')
    in_file:    path to folder with files
    out_folder: path to folder with results
    crs:        result projection
    out_ext:    extention of result files'''

    name = in_file.split('/')[-1].split('.')[0]

    layers = fiona.listlayers(in_file)
    
    for i in layers:
        data = gpd.read_file(in_file, layer = i).to_crs(crs)
        try: data.to_file(f'{out_folder}/{name}.{out_ext}')
        except: print(f'Error file: {name}')
        
    return 'Mission completed'

if __name__ == '__main__':
    #in_file = input('input in_file path:')
    print(to_shp.__doc__)
