import xml.etree.ElementTree as ET
from xml.dom import minidom

def convert_bookmarks_to_stations(input_filename='bookmarks.xml', output_filename='stations.xml'):
    # Parser le fichier d'entrée
    tree = ET.parse(input_filename)
    root = tree.getroot()
    
    # Créer la nouvelle racine pour le nouveau format
    new_root = ET.Element('Stations')
    
    # Trouver le groupe racine dans l'ancien format
    group = root.find('.//group')
    
    # Convertir chaque bookmark en Station
    for bookmark in group.findall('bookmark'):
        station = ET.SubElement(new_root, 'Station')
        
        # Créer les éléments uri et name
        uri = ET.SubElement(station, 'uri')
        uri.text = bookmark.attrib['url']
        
        name = ET.SubElement(station, 'name')
        name.text = bookmark.attrib['name']
    
    # Créer un nouvel arbre ElementTree
    new_tree = ET.ElementTree(new_root)
    
    # Convertir directement en chaîne XML formatée
    xml_string = minidom.parseString(ET.tostring(new_root)).toprettyxml(indent="  ")
    
    # Écrire le résultat final
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(xml_string)

# Exemple d'utilisation
convert_bookmarks_to_stations()
