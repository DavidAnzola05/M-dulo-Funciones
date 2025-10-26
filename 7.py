def horas_a_minutos_DAAC(horas_DAAC):
    return horas_DAAC * 60

def minutos_a_segundos_DAAC(minutos_DAAC):
    return minutos_DAAC * 60

def segundos_a_minutos_DAAC(segundos_DAAC):
    return segundos_DAAC / 60

h_DAAC = 2
print(f"{h_DAAC} horas = {horas_a_minutos_DAAC(h_DAAC)} minutos")
m_DAAC = 120
print(f"{m_DAAC} minutos = {minutos_a_segundos_DAAC(m_DAAC)} segundos")
s_DAAC = 360
print(f"{s_DAAC} segundos = {segundos_a_minutos_DAAC(s_DAAC)} minutos")
