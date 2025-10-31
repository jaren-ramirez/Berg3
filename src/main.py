from dataclasses import dataclass


@dataclass
class Material_Layer():
    layer_thickness: float
    latent_heat: float
    thawed_percent_moisture: float
    thawed_density: float
    thawed_heat_capacity: float
    thawed_conductivity: float
    frozen_percent_moisture: float
    latent_heat_fusion: float
    frozen_density: float
    frozen_heat_capacity: float
    frozen_conductivity: float
    
@dataclass
class Location():
    location_name: str
    thaw_n_factor: float
    freeze_n_factor: float 
    design_air_thawing_index: float #degree days
    design_air_freezing_index: float #degree days
    mean_air_thawing_index: float
    mean_air_freezing_index: float
    mean_annual_air_temp: float #degree F
    ampl_of_air_temp: float #Sine wave
    design_surface_thawing_index: int #degree days
    design_surface_freezing_index: int #degree days
    mean_surface_thawing_index: int
    mean_surface_freezing_index: int
    mean_annual_surface_temp: float #degree F
    ampl_of_surface_temp: float #Sine wave
    thaw_season_length: int
    freeze_season_length: int

class Soil_Profile():
    def __init__(self):
        self.material_layers = []
        self.num_material_layers = 0
        self.air_thawing_freezing_indices = []

def load_default_locations():
    return [{
        "location_name": "Fairbanks, Ak",
        "thaw_n_factor": 1.7,
        "freeze_n_factor":1,
        "design_air_thawing_index":4000,
        "design_air_freezing_index":6900,
        "mean_air_thawing_index":3500,
        "mean_air_freezing_index":5600,
        "mean_annual_air_temp":26.2,
        "ampl_of_air_temp":38.7,
        "design_surface_thawing_index":6800,
        "design_surface_freezing_index":6900,
        "mean_surface_thawing_index":5950,
        "mean_surface_freezing_index":5600,
        "mean_annual_surface_temp":33,
        "ampl_of_surface_temp":49.7,
        "thaw_season_length_air":165.2,
        "freeze_season_length_air":199.8,
        "thaw_season_length_surface":184.7,
        "freeze_season_length_surface":180.3,
    },
    {
        "location_name": "Anchorage, Ak",
        "thaw_n_factor": 1.7,
        "freeze_n_factor":1,
        "design_air_thawing_index":4000,
        "design_air_freezing_index":3200,
        "mean_air_thawing_index":3500,
        "mean_air_freezing_index":2300,
        "mean_annual_air_temp":35.3,
        "ampl_of_air_temp":24.7,
        "design_surface_thawing_index":6800,
        "design_surface_freezing_index":3200,
        "mean_surface_thawing_index":5950,
        "mean_surface_freezing_index":2300,
        "mean_annual_surface_temp":42,
        "ampl_of_surface_temp":34,
        "thaw_season_length_air":198.0,
        "freeze_season_length_air":167.0,
        "thaw_season_length_surface":217.2,
        "freeze_season_length_surface":147.8,
    },{
        "location_name": "Juneau, Ak",
        "thaw_n_factor": 1.7,
        "freeze_n_factor":1,
        "design_air_thawing_index":4400,
        "design_air_freezing_index":1500,
        "mean_air_thawing_index":3800,
        "mean_air_freezing_index":1000,
        "mean_annual_air_temp":39.7,
        "ampl_of_air_temp":19.1,
        "design_surface_thawing_index":7480,
        "design_surface_freezing_index":1500,
        "mean_surface_thawing_index":6460,
        "mean_surface_freezing_index":1000,
        "mean_annual_surface_temp":47.0,
        "ampl_of_surface_temp":28.0,
        "thaw_season_length_air":230.5,
        "freeze_season_length_air":134.5,
        "thaw_season_length_surface":248.0,
        "freeze_season_length_surface":117.0,
    }]



def main():
    pass
     

if __name__ == "__main__":
    main()