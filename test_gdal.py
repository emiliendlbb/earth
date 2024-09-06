import xarray as xr
import os
import time
 
variables = [
    # atmospheric
    "temperature",
    "u_component_of_wind",
    "v_component_of_wind",
    "geopotential",
    "specific_humidity",
    "vertical_velocity",
    # single
    "2m_temperature",
    "10m_u_component_of_wind",
    "10m_v_component_of_wind",
    "mean_sea_level_pressure",
    "sea_surface_temperature",
    "total_precipitation",
]
 
# 20 years
start_time = '1999-01-01T00:00:00.000000000'
end_time = '1999-01-07T00:00:00.000000000'
 
# Opening a view
data = xr.open_zarr("gs://weatherbench2/datasets/era5/1959-2022-full_37-1h-0p25deg-chunk-1.zarr-v2")
data = data[variables]
data = data.sel(time=slice(start_time, end_time))
print("Dataset Size: ", data.nbytes / 1e9, "GB")
 
#path = "/gpfs/scratch/acad/sail/era5"
path = "."
filename = "era5_1999-2019-1h-1440x721-gencast.zarr"
 
# Creating folder to save the data
dir_name = os.path.dirname(f"{path}")
if dir_name and not os.path.exists(dir_name):
    os.makedirs(dir_name, exist_ok=True)
 
# Only load 4 hours of data at a time 
data = data.chunk({'time': 4})
 
# Save the data
start = time.time()
data.to_zarr(f"{path}/{filename}", mode="a")
end = time.time()
 
print("Time to save the data: ", end - start, " seconds")