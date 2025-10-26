def metros_a_centimetros_DAAC(m_DAAC):
    return m_DAAC * 100

def centimetros_a_metros_DAAC(cm_DAAC):
    return cm_DAAC / 100

m_DAAC = 1.75
print(f"{m_DAAC} m = {metros_a_centimetros_DAAC(m_DAAC)} cm")
cm_DAAC = 250
print(f"{cm_DAAC} cm = {centimetros_a_metros_DAAC(cm_DAAC)} m")
