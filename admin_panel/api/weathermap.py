import requests

api_key = 'ac1e1a88b8-0075e8d73d-9e27ab2655'

BASE_URL = 'https://px6.link/api/'
class Proxy6:
    def __init__(self, api_key):
        self.api_key = api_key
        self.proxies = {
            "http": "http://B7JpTk:mEC4ph@94.131.54.6:9054",
            "https": "http://B7JpTk:mEC4ph@94.131.54.6:9054"
        }

    def _get(self, method, proxi, params=None):
        url = f"{BASE_URL}/{self.api_key}/{method}"
        res = requests.get(url, params=params, proxies=proxi)
        if res.status_code == 200:
            data = res.json()
            return data
        else:
            print(res.status_code)
            return None


    def getprice(self, count, period, version=6):
        params = {
            'count': count,
            'period': period,
            'version': version
        }
        return self._get('getprice',self.proxies, params)


    def getcount(self,country,version=6):
        params = {
            'country': country,
            'version': version

        }
        return self._get('getcount',self.proxies, params)

    def getcountry(self, version=6):
        params = {
            'version': version
        }
        return self._get('getcountry',self.proxies, params)

    def getproxy(self, state="all", descr=None, nokey=None, page=1, limit=1000):
        params = {
            "state": state,
            "page": page,
            "limit": limit,
        }
        if descr is not None:
            params["descr"] = descr
        if nokey is not None:
            params["nokey"] = ""
        return self._get("getproxy",self.proxies, params)


    def buy(self, count, period, country, version=6, type_="http", descr=None, auto_prolong=False, nokey=False):
        """
        Покупка прокси.

        Параметры:
            count (int): количество прокси (обязательный)
            period (int): период в днях (обязательный)
            country (str): страна iso2 (обязательный)
            version (int): версия прокси (по умолчанию 6)
            type_ (str): тип прокси "http" или "socks" (по умолчанию "http")
            descr (str): технический комментарий, макс длина 50
            auto_prolong (bool): флаг автопродления (без значения)
            nokey (bool): флаг возврата списка без ключей (без значения)
        """
        params = {
            "count": count,
            "period": period,
            "country": country,
            "version": version,
            "type": type_,
        }
        if descr:
            if len(descr) > 50:
                raise ValueError("descr max length is 50")
            params["descr"] = descr
        if auto_prolong:
            params["auto_prolong"] = ""  # флаг без значения
        if nokey:
            params["nokey"] = ""  # флаг без значения

        return self._get("buy",self.proxies, params)



    def prolong(self, period, ids, nokey=False):
        """
        Продление прокси.

        Параметры:
            period (int): период продления в днях (обязательный)
            ids (str or list): строка с номерами прокси через запятую или список
            nokey (bool): флаг возврата списка без ключей (без значения)
        """
        if isinstance(ids, list):
            ids = ",".join(str(i) for i in ids)
        params = {
            "period": period,
            "ids": ids,
        }
        if nokey:
            params["nokey"] = ""

        return self._get("prolong",self.proxies, params)