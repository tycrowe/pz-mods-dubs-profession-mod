import pandas as pd

data = pd.read_excel('professions.xlsx')
data = data.fillna(0)


def get_attribute_value(value):
    return -100 if value == 0.0 or value == 0 else value

def build_professions():
    print(f"""DPMProfessionsConfig = {{""")
    for index, row in data.iterrows():
        raw_name = row[0]
        name = "dpm_" + (str(row[0]).lower().replace(" ", "_"))
        cost = row[3]
        print(f"""    {{
            type = "{name}",
            name = "{raw_name}",
            icon = "{name}.png",
            cost = {cost},
            desc = "",
            perks = {{
                Cooking = {get_attribute_value(row[5])},
                Fitness = {get_attribute_value(row[6])},
                Strength = {get_attribute_value(row[7])},
                Blunt = {get_attribute_value(row[8])},
                Axe = {get_attribute_value(row[9])},
                Sprinting = {get_attribute_value(row[10])},
                Lightfoot = {get_attribute_value(row[11])},
                Nimble = {get_attribute_value(row[12])},
                Sneak = {get_attribute_value(row[13])},
                Woodwork = {get_attribute_value(row[14])},
                Aiming = {get_attribute_value(row[15])},
                Reloading = {get_attribute_value(row[16])},
                Farming = {get_attribute_value(row[17])},
                Survivalist = {get_attribute_value(row[18])},
                Fishing = {get_attribute_value(row[19])},
                Trapping = {get_attribute_value(row[20])},
                Firearm = {get_attribute_value(row[21])},
                PlantScavenging = {get_attribute_value(row[22])},
                Doctor = {get_attribute_value(row[23])},
                Electricity = {get_attribute_value(row[24])},
                MetalWelding = {get_attribute_value(row[25])},
                Mechanics = {get_attribute_value(row[26])},
                Spear = {get_attribute_value(row[27])},
                Maintenance = {get_attribute_value(row[28])},
                SmallBlade = {get_attribute_value(row[29])},
                LongBlade = {get_attribute_value(row[30])},
                SmallBlunt = {get_attribute_value(row[31])},
                Tailoring = {get_attribute_value(row[32])}
            }}
        }},""")
    print(f"""}}""")


def build_profession_creation_check():
    for index, row in data.iterrows():
        raw_name = row[0]
        name = "dpm_" + (str(row[0]).lower().replace(" ", "_"))
        if index == 0:
            print(f"if desc_profession == \'{name}\' then")
        else:
            print(f"elseif desc_profession == \'{name}\' then")

    print("end")

build_profession_creation_check()