
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
    'ottoman.':'YJ',
    'endbay/fairing.':'YK',
    'Spair pocket.':'YL',
    'Table.':'YM',
    'hydrolock.':'YN',
    'Cable recline.':'YO',
    'Lock table/latch.':'YP',
    'Seat belt.':'YQ',
}
Alphabetical_Code_IFE = {

'Drop down monitor.':'EA',
'IFE remote.':'EB',
'Media.':'EC',
'Seat back monitor.':'ED',
'Wall mounted LCD':'EE',
'WIFI.':'EF',
'A/M or udseat vid.':'EG',

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
    'Waste flapper':'GN',
    'Water boiler.':'GO',
    'Wine chiller.':'GP',
    'Hot Jug.':'GQ',
    'Plumbing System.':'GR',
    'Drawer-ice.':'GS',
    'Water filter cartridge.':'GT',
}
Alphabetical_Code_Lavatory = {
    'Aminities Box.':'VA',
    'Drain Plug.':'VB',
    'Faucet.':'VC',
    'Lavatory call speaker,':'VD',
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
    'Flushing switch/ Micro Switch.':'VO',
    'Water filter.':'VP',
    'Vacuum Blower.':'VQ',
    'Plumbing System/ Tubing (hose).':'VR',
    'toilet assy.':'VS',

}



import difflib


while True:
    user_input = input("Enter fault description: ")
    user_input1 = input("Class of item: ")

    if user_input.lower() == "exit":
        break

    class_dict = None  

    if user_input1 == "First class":
        class_dict = Alphabetical_Code_First_Class
    elif user_input1 == "Business class":
        class_dict = Alphabetical_Code_Business_Class
    elif user_input1 == "Economy class":
        class_dict = Alphabetical_Code_Economy_Class
    elif user_input1 == "IFE":
        class_dict = Alphabetical_Code_IFE
    elif user_input1 == "Galley":
        class_dict = Alphabetical_Code_Galley
    elif user_input1 == "lavatory":
        class_dict = Alphabetical_Code_Lavatory
    else:
        print("No matching Item Class")
        continue

    if class_dict:  
        close_matches = difflib.get_close_matches(user_input1, class_dict.keys(), n=1, cutoff=0.5)
        if close_matches:
            closest_match = close_matches[0]
            fault_code = class_dict[closest_match]
            print(f"Error code for '{closest_match}' is {fault_code}.")
        else:
            print("No matching item code in this class")
    else:
        print("No matching Item Class")

    close_matches = difflib.get_close_matches(user_input, fault_descriptions.keys(), n=1, cutoff=0.5)
    if close_matches:
        closest_match = close_matches[0]
        error_code = fault_descriptions[closest_match]
        print(f"Error code for '{closest_match}' is {error_code}.")
    else:
        print("No matching fault description found.")

