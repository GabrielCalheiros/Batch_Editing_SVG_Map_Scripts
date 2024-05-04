import xml.etree.ElementTree as ET

# Delete an layer of the map
def delete_map_layer(root, layer_name):
    for child in root:
        # If id of the child is viewbox, then print its children
        if child.tag == '{http://www.w3.org/2000/svg}g' and child.attrib.get('id') == 'viewbox':
            for grandchild in child:
                if grandchild.tag == '{http://www.w3.org/2000/svg}g' and grandchild.attrib.get('id') == layer_name:
                    child.remove(grandchild)

    return root
        
# Print the layers of the map
def print_map_layers(root):
    for child in root:
        # If id of the child is viewbox, then print its children
        if child.tag == '{http://www.w3.org/2000/svg}g' and child.attrib.get('id') == 'viewbox':
            for grandchild in child:
                # Layers of the SVG Map
                print(grandchild.tag, grandchild.attrib)

def remove_multiple_layers(root, layer_list):
    
    for layer in layer_list:
        root = delete_map_layer(root, layer)
    
    return root

def main():
    
    # Loading the map with all the layers
    tree = ET.parse('fantasy_map.svg')
    root = tree.getroot()
    
    print_map_layers(root)
    
    # The map template contains a list of every layer to be deleted
    template_empty_map = ['landmass', 'ocean', 'lakes', 'texture', 'terrs', 'biomes', 'cells', 'coordinates', 'rivers', 'terrain', 'regions']
    root = remove_multiple_layers(root, template_empty_map)


    print("\n\n\n\n")
    print_map_layers(root)
    
                    
        
if __name__ == "__main__":
    main()
    
    
