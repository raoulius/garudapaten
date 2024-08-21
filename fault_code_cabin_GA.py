import difflib

fault_descriptions = {
    'Problem is not ill.': 1,
    'The is broken.': 3,
    'N/A or missing.': 2,
    'stuck.': 4,
    'No picture.': 5,
    'Cant stow.': 12,
    'Hang.': 13,
    'No power.': 14,
    'Leak.': 17,
    'No response from the .': 21,
    'cant be turned on.': 22,
    'Wrong indication.': 23,
    'cannot be locked.': 24,
    'Clogged off.': 26,
    'Dirty.': 51,
    'torn.': 58,
    'peeled off.': 59,
    'Odor.': 60,
    'Crack.': 61,
    'improperly installed.': 63,
    'Hard to close/open.': 65,
    'Improper position.': 66,
    'is loose.': 67,
    'is weak/cant be upright/cant retract.': 68,
    'is deflated.': 70,
    'Dent.': 71,
    'Corrosion.': 72
}

Alphabetical_Code_First_Class = {
    'Bottom Cover.':'FA',
    'Leg Rest.' : 'FB',
    'actuator.' : 'FC',
    'Hiwin minirail assy.' : 'FD',
    'Back cover.' : 'FE',
    'Lumbar System.':'FF',
    'Massage System.':'FG',
    'Headrest Cover.':'FH',
    'Seat belt.':'FI',
    'Reading light.':'FJ',
    'Cushion.':'FK',
    'Ottoman.':'FL',
    'Gasper.':'FM',
    'Armrest.':'FN',
    'Sliding Door.':'FO',
    'Coat room.':'FP',
    'Rubber seal.':'FQ',
    'Trim.':'FR',
    'Shroud assy.':'FS',
    'Table.':'FT',
    'Credenza.':'FU',
    'Lid assy.':'FV',
    'Privacy divider acuator.':'FW',
    'SCU.':'FX',
    'Seat numbering.':'FY',
    'IFE.':'FZ',
}

Alphabetical_Code_Business_Class = {
    'Armrest Structure.':'CA',
    'Armcap.':'CB',
    'Back cover.':'CC',
    'Bottom cover.':'CD',
    'Cushion.':'CE',
    'Footrest cover.':'CF',
    'Headrest cover.':'CG',
    'Legrest.':'CH',
    'Footrest.':'CI',
    'Backrest.':'CJ',
    'Headrest.':'CK',
    'Lumbar System.':'CL',
    'Seat belt.':'CM',
    'Shroud.':'CN',
    'Table.':'CO',
    'Spair Pocket.':'CP',
    'Cable Rec/Ctrl bzl':'CR',
    'ECU.':'CS',
    'Actuator.':'CT',
    'Snake light.':'CU',
    'Reading light.':'CV',
    'SEB.':'CW',
    'Coat hook.':'CX',
    'Magazine rack.':'CY',
    'Pull strap/hinge L/V box.':'CZ',
}

Alphabetical_Code_Economy_Class = {
    'Armcap.':'YA',
    'Armrest.':'YB',
    'Backrest cover.':'YC',
    'Bottom cover.':'YD',
    'Cushion.':'YE',
    'Escutcheon.':'YF',
    'Headrest.':'YG',
    'Headrest cover.':'YH',
    'IAT.':'YI',
    'Ottoman.':'YJ',
    'Endbay/fairing.':'YK',
    'Spair pocket.':'YL',
    'Table.':'YM',
    'Hydrolock.':'YN',
    'Cable recline.':'YO',
    'Lock table/latch.':'YP',
    'Seat belt.':'YQ',
}

Alphabetical_Code_IFE = {
    'Drop down monitor.':'EA',
    'IFE remote.':'EB',
    'Media.':'EC',
    'Seat back monitor.':'ED',
    'Wall mounted LCD.':'EE',
    'WIFI.':'EF',
    'A/M or underseat video.':'EG',
}

Alphabetical_Code_Galley = {
    'Air Chiller.':'GA',
    'Bun Warmer.':'GB',
    'Coffee maker.':'GC',
    'Container.':'GD',
    'Espresso maker.':'GE',
    'Extractor.':'GF',
    'Galley door.':'GG',
    'Latch/Retainer.':'GH',
    'Microwave.':'GI',
    'Oven.':'GJ',
    'Spigot.':'GK',
    'Zink strainer/screen top.':'GL',
    'Waste trolley.':'GM',
    'Waste flapper.':'GN',
    'Water boiler.':'GO',
    'Wine chiller.':'GP',
    'Hot Jug.':'GQ',
    'Plumbing System.':'GR',
    'Drawer-ice.':'GS',
    'Water filter cartridge.':'GT',
}

Alphabetical_Code_Lavatory = {
    'Amenities Box.':'VA',
    'Drain Plug.':'VB',
    'Faucet.':'VC',
    'Lavatory call speaker.':'VD',
    'Lavatory ceiling.':'VE',
    'Lavatory Cover.':'VF',
    'Lavatory door.':'VG',
    'Lavatory seater.':'VH',
    'Lavatory Shroud.':'VI',
    'Lavatory Wall.':'VJ',
    'Mirror.':'VK',
    'Occupied Sign.':'VL',
    'Tissue Holder/Box.':'VM',
    'Wash Basin.':'VN',
    'Flushing switch/Micro Switch.':'VO',
    'Water filter.':'VP',
    'Vacuum Blower.':'VQ',
    'Plumbing System/Tubing (hose).':'VR',
    'Toilet assy.':'VS',
}

class_codes = {
    'First class': Alphabetical_Code_First_Class,
    'Business class': Alphabetical_Code_Business_Class,
    'Economy class': Alphabetical_Code_Economy_Class,
    'IFE': Alphabetical_Code_IFE,
    'Galley': Alphabetical_Code_Galley,
    'Lavatory': Alphabetical_Code_Lavatory
}

def get_closest_match(user_input, data_dict):
    matches = difflib.get_close_matches(user_input, data_dict.keys(), n=1, cutoff=0.5)
    if matches:
        return matches[0], data_dict[matches[0]]
    else:
        return None, None

def main():
    while True:
        print("\nEnter 'exit' at any time to quit.")
        
        fault_input = input("Enter fault description: ").strip()
        if fault_input.lower() == 'exit':
            break
        
        class_input = input("Enter class of item (e.g., First class, Business class, Economy class, IFE, Galley, Lavatory): ").strip()
        if class_input.lower() == 'exit':
            break
        
        item_input = input("Enter item description: ").strip()
        if item_input.lower() == 'exit':
            break
        
        fault_match, fault_code = get_closest_match(fault_input, fault_descriptions)
        if fault_code:
            print("Code found")
        else:
            print("No matching fault description found.")
        
        class_dict = class_codes.get(class_input)
        if not class_dict:
            print("No matching item class found.")
            continue
        
        item_match, item_code = get_closest_match(item_input, class_dict)
        if item_code:
            print(f"Fault code is {fault_code}{item_code}")
        else:
            print("No matching item description found in the specified class.")

if __name__ == "__main__":
    main()
