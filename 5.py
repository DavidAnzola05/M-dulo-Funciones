def kilometros_a_millas_DAAC(km_DAAC):
    return km_DAAC * 0.621371

def millas_a_kilometros_DAAC(mi_DAAC):
    return mi_DAAC / 0.621371

dist_km_DAAC = 10
print(f"{dist_km_DAAC} km = {kilometros_a_millas_DAAC(dist_km_DAAC)} millas")
dist_mi_DAAC = 6.2
print(f"{dist_mi_DAAC} millas = {millas_a_kilometros_DAAC(dist_mi_DAAC)} km")
