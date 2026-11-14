import xml.etree.ElementTree as ET

tree = ET.parse("6502_Emulation.circ")
root = tree.getroot()

# 1. Shrink all Tunnel label fonts so their enclosing boxes fit the 2.13.8 grid
for comp in root.iter("comp"):
    if comp.get("name") == "Tunnel":
        font_attr = next((a for a in comp.findall("a") if a.get("name") == "labelfont"), None)
        if font_attr is None:
            ET.SubElement(comp, "a", {"name": "labelfont", "val": "SansSerif plain 7"})
        else:
            font_attr.set("val", "SansSerif plain 7")

# 2. Ensure subcircuits and memory/register blocks stay in classic footprint
for circuit in root.findall("circuit"):
    if not any(a.get("name") == "appearance" for a in circuit.findall("a")):
        ET.SubElement(circuit, "a", {"name": "appearance", "val": "classic"})

for comp in root.iter("comp"):
    if comp.get("name") in {"Pin", "Register", "Counter", "RAM", "ROM"}:
        app = next((a for a in comp.findall("a") if a.get("name") == "appearance"), None)
        if app is None:
            ET.SubElement(comp, "a", {"name": "appearance", "val": "classic"})
        else:
            app.set("val", "classic")

tree.write("6502_Emulation_fixed.circ", encoding="UTF-8", xml_declaration=True)
print("Saved 6502_Emulation_fixed.circ")