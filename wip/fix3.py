import xml.etree.ElementTree as ET

tree = ET.parse("6502_Emulation_mod.circ")
root = tree.getroot()

count = 0
for comp in root.iter("comp"):
    if comp.get("name") == "Tunnel":
        font_attr = next((a for a in comp.findall("a") if a.get("name") == "labelfont"), None)
        if font_attr is None:
            ET.SubElement(comp, "a", {"name": "labelfont", "val": "SansSerif plain 12"})
        else:
            font_attr.set("val", "SansSerif plain 12")
        count += 1

tree.write("6502_Emulation_mod_12p.circ", encoding="UTF-8", xml_declaration=True)
print(f"Updated {count} tunnels to SansSerif plain 12")