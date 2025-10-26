def litros_a_mililitros_DAAC(l_DAAC):
    return l_DAAC * 1000

def mililitros_a_litros_DAAC(ml_DAAC):
    return ml_DAAC / 1000

l_DAAC = 3
print(f"{l_DAAC} L = {litros_a_mililitros_DAAC(l_DAAC)} mL")
ml_DAAC = 500
print(f"{ml_DAAC} mL = {mililitros_a_litros_DAAC(ml_DAAC)} L")
