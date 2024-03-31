import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import pyproj

def add_utm(processed_data):
    # Define UTM projection
    utm_proj = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')

    processed_data_utm = []
    for file_data in processed_data:
        # Convert GPS coordinates to UTM
        easting, northing = utm_proj(file_data['longitude'], file_data['latitude'])

        # Append UTM coordinates to file data dictionary
        file_data['easting'] = easting
        file_data['northing'] = northing

        # Append modified file data to processed data list
        processed_data_utm.append(file_data)

    return processed_data_utm

    
def get_boundaries(file_path):
    print(file_path)

    '''
    ---- Placeholder for GDAL implementation------
    
    '''
    xy_value = {'xmin': 373179, 'ymin': 5463515 , 'xmax': 374209 , 'ymax': 5464087}
    return xy_value

def extract_gps_info(exif_data, filename):
  """
  Extracts GPS information (latitude, longitude) from Exif metadata.

  Args:
      exif_data: Exif metadata dictionary.
      filename (str): Name of the image file.

  Returns:
      Dictionary containing filename, latitude, and longitude, or None if no GPS data is found.
  """

  gps_info = {}
  if 34853 in exif_data:  # Check if GPSInfo tag exists
    gps_data = exif_data[34853]

    # Extract and convert latitude/longitude (assuming degrees/minutes/seconds format)
    if 1 in gps_data and 2 in gps_data and 4 in gps_data and 5 in gps_data:
      lat_ref = gps_data[1]
      lon_ref = gps_data[3]
 # Assuming string value
      latitude = float(gps_data[2][0] + (gps_data[2][1] / 60) + (gps_data[2][2] / 3600))
      longitude = float(gps_data[4][0] + (gps_data[4][1] / 60) + (gps_data[4][2] / 3600))

      # Apply direction multiplier based on reference (North/East positive)
      latitude *= 1 if lat_ref in ("N", "North") else -1
      longitude *= 1 if lon_ref in ("E", "East") else -1

      gps_info = {"filename": filename, "latitude": latitude, "longitude": longitude}

  return gps_info if gps_info else None




    

def move_gps_jpgs(jpg_dir):
    """
    Moves JPG files with GPS tags from the source directory to a designated GPS directory,
    and moves JPG files without GPS tags to a designated non-GPS directory.

    Args:
        jpg_dir: Path to the directory containing JPG files.
    """

    gps_dir = os.path.join(jpg_dir, 'gps')  # Directory for images with GPS tags
    no_geo_dir = os.path.join(jpg_dir, 'no_geoinfo')  # Directory for images without GPS tags
    os.makedirs(gps_dir, exist_ok=True)
    os.makedirs(no_geo_dir, exist_ok=True)
    mark_inp = []
    for filename in os.listdir(jpg_dir):
        if filename.endswith('.jpg'):
            image_path = os.path.join(jpg_dir, filename)
            sgl_inp = {'filename' : filename}
            
            try:
                # Open the image file
                with Image.open(image_path) as image:
                    # Extract Exif metadata
                    exif_data = image._getexif()

                    if exif_data is not None:
                        
                        sgl_inp = extract_gps_info(exif_data, filename)
                        
                        if sgl_inp is not None:
                            # Close the image file before moving
                            image.close()
                            try:
                                shutil.move(image_path, gps_dir)
                                print(f"{filename} moved to GPS directory.")
                            except shutil.Error as e:
                                print(f"Error moving {filename} to GPS directory: {e}")
                                sgl_inp['error'] = f"Error moving {filename} to GPS directory: {e}"
                        else:
                            # Close the image file before moving
                            image.close()
                            try:
                                shutil.move(image_path, no_geo_dir)
                                print(f"{filename} moved to non-GPS directory.")
                            except shutil.Error as e:
                                sgl_inp['error'] = f"Error moving {filename} to GPS directory: {e}"
                                print(f"Error moving {filename} to non-GPS directory: {e}")
                    else:
                       
                        image.close()
                        print(f"Error: No Exif data found in {filename}")
                        sgl_inp['error'] = f"Error moving {filename} to GPS directory: {e}"
            except Exception as e:
                print(f"Error processing {filename}: {e}")
            mark_inp.append(sgl_inp)
    return mark_inp
        
