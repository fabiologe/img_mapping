import os
import re
import csv



class ImageData:
    def __init__(self, filename, zone, easting, northing, date, time):
        self.filename = filename
        self.zone = zone
        self.easting = easting
        self.northing = northing
        self.date = date
        self.time = time

    def __str__(self):
        return f"Filename: {self.filename},Zone: {self.zone}, Easting: {self.easting}, Northing: {self.northing}, Date: {self.date}, Time: {self.time}"



def extract_image_data(filename, pattern):
    """
    Extracts image data from a filename using a given pattern.

    Args:
        filename: The name of the image file.
        pattern: A regular expression pattern to match the filename format.

    Returns:
        An ImageData object containing the extracted data, or None if parsing fails.
    """

    match = re.match(pattern, filename)
    if match:
        # Use group names for clarity
        zone = match.group("zone")
        easting = int(match.group("easting"))
        northing = int(match.group("northing"))
        date = int(match.group("date"))
        time = int(match.group("time"))

        return ImageData(filename, zone, easting, northing, date, time)
    else:
        return None


# Define image directory and output file
image_dir = "img"
# No need to create an empty dictionary anymore

# Define the correct pattern based on your actual filename structure
pattern = r"^(?P<zone>\d{2}[A-Z]) (?P<easting>\d{6}) (?P<northing>\d{7})_(?P<date>\d{8})_(?P<time>\d{6})\.jpg$"

# Process each image file
csv_data = []  # Collect extracted data here
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg"):
        image_data = extract_image_data(filename, pattern)
        if image_data is not None:
            csv_data.append(image_data)
            print(f"Extracted data for {filename}")
        else:
            print(f"Warning: Failed to extract data for {filename}")
# Open the CSV file in write mode and create a writer
with open("extracted_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Filename", "Zone", "Easting", "Northing", "Date", "Time"])

    # Write each extracted data item to a row
    for image_data in csv_data:
        writer.writerow([
            image_data.filename,
            image_data.zone,
            image_data.easting,
            image_data.northing,
            image_data.date,  # Format date
            image_data.time # Format time
        ])

print("CSV file created successfully!")       


