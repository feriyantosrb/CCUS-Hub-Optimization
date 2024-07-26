import pandas as pd
import re
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Function to convert WKT linestring to a list of latlon tuples
def wkt_linestring_to_latlon(wkt_linestring, linestring_id):
    # Extract coordinates from WKT linestring using regex
    coordinates = re.findall(r"[-+]?\d*\.\d+|\d+", wkt_linestring)
    
    # Convert coordinates to tuples of (lat, lon)
    latlon_list = [(float(coordinates[i+1]), float(coordinates[i])) for i in range(0, len(coordinates), 2)]
    
    # Create a DataFrame from the latlon list and add linestring_id column
    df_linestring = pd.DataFrame(latlon_list, columns=['lat', 'lon']).assign(linestring_id=linestring_id)
    
    return df_linestring

# Example WKT linestrings
wkt_linestrings = [
    "LINESTRING (104.27900052233664 -3.366430252481158, 104.19088439065328 -4.4438941787185415)"
]

# Create an empty DataFrame to store all latlon data
df_combined = pd.DataFrame(columns=['lat', 'lon', 'linestring_id'])

# Loop through each linestring
for linestring_id, wkt_linestring in enumerate(wkt_linestrings, 1):
    # Convert WKT linestring to latlon DataFrame and add linestring_id column
    df_linestring = wkt_linestring_to_latlon(wkt_linestring, linestring_id)
    
    # Append the DataFrame to the combined DataFrame
    #df_combined = pd.concat([df_combined, df_linestring], ignore_index=True)
    df_combined = pd.concat([df_combined, df_linestring], ignore_index=True, sort=False)


# Save the combined DataFrame to Excel
df_combined.to_excel("output_file.xlsx", index=False)
