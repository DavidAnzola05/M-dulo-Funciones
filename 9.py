def usd_a_eur_DAAC(usd_DAAC, tasa_DAAC):
    return usd_DAAC * tasa_DAAC

def eur_a_usd_DAAC(eur_DAAC, tasa_DAAC):
    return eur_DAAC / tasa_DAAC

tasa_cambio_DAAC = 0.92
usd_DAAC = 100
print(f"{usd_DAAC} USD = {usd_a_eur_DAAC(usd_DAAC, tasa_cambio_DAAC)} EUR")
eur_DAAC = 92
print(f"{eur_DAAC} EUR = {eur_a_usd_DAAC(eur_DAAC, tasa_cambio_DAAC)} USD")
