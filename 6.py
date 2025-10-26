def kilogramos_a_libras_DAAC(kg_DAAC):
    return kg_DAAC * 2.20462

def libras_a_kilogramos_DAAC(lb_DAAC):
    return lb_DAAC / 2.20462

peso_kg_DAAC = 70
print(f"{peso_kg_DAAC} kg = {kilogramos_a_libras_DAAC(peso_kg_DAAC)} lb")
peso_lb_DAAC = 154
print(f"{peso_lb_DAAC} lb = {libras_a_kilogramos_DAAC(peso_lb_DAAC)} kg")
