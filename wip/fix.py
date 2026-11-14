import xml.etree.ElementTree as ET

tree = ET.parse("6502_Emulation.circ")
root = tree.getroot()

# 1. Force all custom subcircuits to use classic footprint
for circuit in root.findall("circuit"):
    has_app = any(a.get("name") == "appearance" for a in circuit.findall("a"))
    if not has_app:
        ET.SubElement(circuit, "a", {"name": "appearance", "val": "classic"})

# 2. Force lib="0" (Pin, Tunnel) and lib="4" (RAM, Register, Counter) to classic appearance
target_names = {"Pin", "Tunnel", "Register", "Counter", "RAM", "ROM"}
for comp in root.iter("comp"):
    if comp.get("name") in target_names:
        app = next((a for a in comp.findall("a") if a.get("name") == "appearance"), None)
        if app is None:
            ET.SubElement(comp, "a", {"name": "appearance", "val": "classic"})
        else:
            app.set("val", "classic")

tree.write("6502_Emulation_v5.circ", encoding="UTF-8", xml_declaration=True)
print("Saved 6502_Emulation_v5.circ")