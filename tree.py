import xml.etree.ElementTree as ET

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

def main():
    
    tree = ET.parse('Cania 2024-05-04-08-35.svg')
    root = tree.getroot()
    
    print_map_layers(root)
    root = delete_map_layer(root, 'landmass')
    root = delete_map_layer(root, 'ocean')
    root = delete_map_layer(root, 'lakes')
    root = delete_map_layer(root, 'texture')
    root = delete_map_layer(root, 'terrs')
    root = delete_map_layer(root, 'biomes')
    root = delete_map_layer(root, 'cells')
    root = delete_map_layer(root, 'coordinates')
    root = delete_map_layer(root, 'rivers')
    root = delete_map_layer(root, 'terrain')
    root = delete_map_layer(root, 'regions')

    print("\n\n\n\n")
    print_map_layers(root)

                    
        
if __name__ == "__main__":
    main()
    
    
