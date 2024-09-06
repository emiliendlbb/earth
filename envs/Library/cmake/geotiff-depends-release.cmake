#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "geotiff_library" for configuration "Release"
set_property(TARGET geotiff_library APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(geotiff_library PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/geotiff_i.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "C:/Users/emili/OneDrive/Documents/projets/Weather_diffusion/earth/earth/envs/Library/lib/tiff.lib;PROJ::proj;C:/Users/emili/OneDrive/Documents/projets/Weather_diffusion/earth/earth/envs/Library/lib/z.lib;C:/Users/emili/OneDrive/Documents/projets/Weather_diffusion/earth/earth/envs/Library/lib/libjpeg.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/geotiff.dll"
  )

list(APPEND _cmake_import_check_targets geotiff_library )
list(APPEND _cmake_import_check_files_for_geotiff_library "${_IMPORT_PREFIX}/lib/geotiff_i.lib" "${_IMPORT_PREFIX}/bin/geotiff.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
