import requests
import json


def get_exchange_rates():
    json_str = requests.get("https://openexchangerates.org/api/latest.json \
                            ?app_id=ba0c4dd8894d4735bad89219b50bae16").text
    exchange_rates = json.loads(json_str)
    exchange_rates = exchange_rates["rates"]
    exchange_rates = {k: 1/v for k, v in exchange_rates.items()}

    exchange_rates["DEM"] = 0.574277
    exchange_rates["ITL"] = 0.000580346
    exchange_rates['FFR'] = 1/5.82
    exchange_rates['BEF'] = 0.0278800
    exchange_rates['AZM'] = 0.000191160
    exchange_rates['YUM'] = 0.58
    exchange_rates['PTE'] = 0.00561087
    exchange_rates['VEB'] = 0.000158730
    exchange_rates['IRN'] = 1/29880
    exchange_rates['NLG'] = 0.56
    exchange_rates['FIM'] = 0.189177
    exchange_rates['GRD'] = 0.00330074
    exchange_rates['ROL'] = 0.0000254717
    exchange_rates['IEP'] = 1.42811
    exchange_rates['RUR'] = 1/64930
    exchange_rates['SKK'] = 0.0373354
    exchange_rates['AFA'] = 1/64209
    exchange_rates['BGL'] = 1/1740
    exchange_rates['GHC'] = 1/37449.4
    exchange_rates['FRF'] = 0.171470
    exchange_rates['SIT'] = 0.00469383
    exchange_rates['ATS'] = 0.0817404
    exchange_rates['EUD'] = 1.12
    exchange_rates['PLZ'] = 0.27/10000
    exchange_rates['FRR'] = 1/5.82
    exchange_rates['PZL'] = 0.27/10000
    exchange_rates['TRL'] = 1/3020000
    exchange_rates['ESP'] = 0.00675568

    return exchange_rates
