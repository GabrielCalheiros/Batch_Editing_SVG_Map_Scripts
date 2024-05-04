import xml.etree.ElementTree as ET
import modeling_map

def main():
    
    # Loading the map with all the layers
    tree = ET.parse('fantasy_map.svg')
    root = tree.getroot()
    
    modeling_map.print_map_layers(root)
    
    # The map template contains a list of every layer to be deleted
    template_empty_map = [
                            'landmass', 
                            'ocean', 
                            'lakes', 
                            'texture', 
                            'terrs', 
                            'biomes', 
                            'cells', 
                            'coordinates', 
                            'rivers', 
                            'terrain', 
                            'regions'
                            ]
    
    root = modeling_map.remove_multiple_layers(root, template_empty_map)


    print("\n\n\n\n")
    modeling_map.print_map_layers(root)
    
                    
        
if __name__ == "__main__":
    main()
    
    
