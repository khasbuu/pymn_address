import os.path

import pymn_address.db

try:
    from pkg_resources import resource_filename
except ImportError:
    def resource_filename(package_or_requirement, resource_name):
        return os.path.join(os.path.dirname(__file__), resource_name)

DATABASE_DIR = resource_filename('pymn_address', 'databases')

class CityProvinces(pymn_address.db.Database):
    data_class_name = 'City'


class DistrictSum(pymn_address.db.Database):
    data_class_name = 'District'


provinces = CityProvinces(os.path.join(DATABASE_DIR, 'province.json'))
districts = DistrictSum(os.path.join(DATABASE_DIR, 'district.json'))
