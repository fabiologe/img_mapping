import matplotlib
import os
import subprocess
import matplotlib.pyplot as plt
from osgeo import gdal
import glob
from pyproj import Proj, transform

def process_geotiff(file_path):
    ds = gdal.Open(file_path)
    if ds is None:
        print(f"Failed to open {file_path}")
        return
    
    data = ds.ReadAsArray()
    gt = ds.GetGeoTransform()

    # Define the extent using the coordinates inside the geotiff
    x_min = gt[0]
    y_min = gt[3] + ds.RasterYSize * gt[5]
    x_max = gt[0] + ds.RasterXSize * gt[1]
    y_max = gt[3]

    # Plot the data with the coordinates from the geotiff
    plt.imshow(data.transpose(1, 2, 0), extent=[x_min, x_max, y_min, y_max])
    plt.title(os.path.basename(file_path))
    plt.show()
    

    return print("Map with GeoTIFFs created")




def mosaick_geotiffs(folder_path):
    #geotiff_files = glob.glob("map_tiles/UTM_[1-4].tif")
    geotiff_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.tif')]    
    print(geotiff_files)
    # Construct the command with the file names string
    cmd = "gdal_merge.py -ps 0.25 -0.25 -o map_tiles/merged/mosaik.tif " 
    subprocess.call(cmd.split()+ geotiff_files)
    


