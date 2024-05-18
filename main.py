import xml.etree.ElementTree as ET
import modeling_map

def main():
    
    # Loading the map with all the layers
    tree = ET.parse('fantasy_map.svg')
    root = tree.getroot()
    
    modeling_map.print_map_layers(root)
    
    # The map template contains a list of every layer to be deleted
    template_empty_map = [ 
                          'ocean',
                          'lakes',
                        #   'landmass',
                          'texture',
                          'terrs',
                          'biomes',
                          'cells',
                          'gridOverlay',
                          'coordinates',
                          'compass',
                          'rivers',
                          'terrain',
                          'relig',
                          'cults',
                          'regions',
                          'provs',
                          'zones',
                          'borders',
                          'routes',
                          'temperature',
                          'coastlines',
                          'ice',
                          'prec',
                          'population',
                          'labels',
                          'icons',
                          'armies',
                          'markers',
                          'ruler',
                          'coastline'
                          ]
    
    template_biomes_map = [ 
                                                     'ocean',
                          'lakes',
                        #   'landmass',
                          'texture',
                          'terrs',
                          'biomes',
                          'cells',
                          'gridOverlay',
                          'coordinates',
                          'compass',
                          'rivers',
                          'terrain',
                          'relig',
                          'cults',
                          'regions',
                          'provs',
                          'zones',
                          'borders',
                          'routes',
                          'temperature',
                          'coastlines',
                          'ice',
                          'prec',
                          'population',
                          'labels',
                          'icons',
                          'armies',
                          'markers',
                          'ruler',
                          'coastline'
                           ]
    
    root = modeling_map.remove_multiple_layers(root, template_empty_map)

    print("\n"*3)
    
    modeling_map.print_map_layers(root)
    
    # Saving the new map
    tree.write('fantasy_map_empty.svg', encoding='utf-8', xml_declaration=True)
    

if __name__ == "__main__":
  
    main()
    
    