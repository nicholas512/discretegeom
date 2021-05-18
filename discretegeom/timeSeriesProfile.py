import netCDF4 as nc

class timeSeriesProfile:

    def __init__(self):
        pass

    @staticmethod
    def multidimensional(file, station, profile, z, **kwargs):
        rootgrp = nc.Dataset(file, 'w', **kwargs)

        _  = rootgrp.createDimension('station', station)
        _  = rootgrp.createDimension('z', z)
        _  = rootgrp.createDimension('profile', profile)
        
        timeSeriesProfile.add_base_metadata(rootgrp)

        return rootgrp

    def single_station(self):
        pass

    def ragged_array(self):
        pass

    @staticmethod
    def add_base_metadata(rootgrp):
        rootgrp.setncattr("featureType", 'timeSeriesProfile')
