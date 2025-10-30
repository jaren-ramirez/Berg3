class Material_Layer():
    def __init__(self):
        self.material_number = None
        self.layer_thickness = None
        
        """Thaw Cycle""" 
        self.frozen_percent_moisture = None
        self.frozen_density_layer = None
        self.frozen_heat_capacity = None
        self.conductivity = None
        self.latent_heat = None
        self.thawed_percent_moisture = None
        self.thawed_density_layer = None
        self.thawed_heat_capacity = None
        self.thawed_conductivity = None
        
        """Freeze Cycle"""
        
        self.latent_heat_fusion = None
        self.frozen_density = None
        self.frozen_heat_capacity = None
        self.frozen_conductivity = None

class Location():
    def __init__(self):
        self.__location_number = None
        self.location_name = None
        self.thaw_n_factor = None
        self.freeze_n_factor = None 
        self.air_thawing_index = None #degree days
        self.air_freezing_index = None #degree days
        self.mean_annual_air_temp = None #degree F
        self.ampl_of_air_temp = None #Sine wave
        
        self.surface_thawing_index = None #degree days
        self.surface_freezing_index = None #degree days
        self.mean_annual_surface_temp = None #degree F
        self.ampl_of_surface_temp = None #Sine wave
        
        self.thaw_season_length = None
        self.freeze_season_lenght = None
        
        
class Soil_Profile():
    def __init__(self):
        self.material_layers = []
        self.num_material_layers = 0
        
        