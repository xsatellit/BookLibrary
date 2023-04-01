import json
from typing import Union


class jsonHandler:

    def __init__(self) -> None:
        """
        Initialize the class with the content of the json file.
        """
        with open("./helpers/List_of_books.json", "r", encoding="utf-8") as jsonfile:
            self.jsonData = json.load(jsonfile)

    def getDict(self) -> dict:
        """
        Returns a dictionary with all content of the json file.
        """
        return self.jsonData

    def getMasterKeys(self) -> list:
        """
        Returns a list with all master keys of the json file.
        """
        master_keys = [key for key in self.jsonData.keys()]
        return master_keys

    def getKeysFromMasterKey(self, masterKey: str) -> list:
        """
        Returns a list with all keys from a given master key.
        """
        keys = [key for key in self.jsonData[masterKey].keys()]
        return keys

    def getAllkeys(self) -> list:
        """
        Returns a list with all keys from all master keys (just the keys, not the values).
        """
        return [key for masterkey in self.jsonData.keys() for key in self.jsonData[masterkey].keys()]

    def getAllValuesForKey(self, masterKey: str, key: str) -> dict:
        """
        Returns a dictionary with all attributes of a given key from a given master key.
        """
        if key in self.jsonData[masterKey]:
            return dict(self.jsonData[masterKey][key])
        else:
            return f"Key '{key}' not found in '{masterKey}'"

    def getAllValuesForSubKey(self, masterKey: str, subkey: str) -> list:
        """
        Returns a list with all values of a given subkey inside a given master key.
        """
        result = []
        if masterKey in self.jsonData:
            for info in self.jsonData[masterKey].values():
                telegram_value = info.get(subkey)
                if telegram_value:
                    result.append(telegram_value)
        return result

    def getValueForSubKey(self, key: str, subkey: str) -> str:
        """
        Returns the value of a given subkey from a given key.
        """
        result = [self.jsonData[masterkey][key][subkey] for masterkey in self.jsonData.keys() 
        for keyK in self.jsonData[masterkey].keys() if keyK == key]

        return result[0]

    def getSubkeysValue(self, subkey: str) -> list:
        """
        Returns a list with all values of a given subkey across all master keys.
        """
        values = []
        for genre in self.jsonData:
            for book in self.jsonData[genre]:
                values.append(self.jsonData[genre][book].get(subkey))

        return values

    def getMasterkeyForKey(self, key: str) -> str:
        """
        Returns a masterkey value for a given key value.
        """
        for masterkey in self.jsonData:
            for keyUnit in self.jsonData[masterkey].keys():
                if key == keyUnit:
                    return masterkey
        
        return None

    def getKeyForSubkey(self, subkey: str, value: str) -> str:
        """
        Returns a key value for a given subkey value.
        """
        for masterkey in self.jsonData:
            for key, item in self.jsonData[masterkey].items():
                if item.get(subkey) == value:
                    return key

        return None

    def getAttr2ValueFromAttr1Value(self, value: Union[str, int], attribute1: str, attribute2: str) -> Union[str, int]:
        """
        Returns the value of a given attribute2 from a book that has a given value in attribute1.
        """
        for genre in self.jsonData:
            for book in self.jsonData[genre]:
                if self.jsonData[genre][book].get(attribute1) == value:
                    return self.jsonData[genre][book].get(attribute2)

        return 0

    def add_key(self, masterkey: str, key: str, value: dict) -> None:
        self.jsonData[masterkey][key] = value
        self.commit()

    def remove(self, masterKey: str, key: str):
        del self.jsonData[masterKey][key]
        self.commit()

    def updateKey(self, masterkey: str, oldkey: str, newkey: str) -> None:
        self.jsonData[masterkey][newkey] = self.jsonData[masterkey].pop(oldkey)
        self.commit()

    def updateValue(self, masterkey: str, key: str, subkey: str, newvalue: str) -> None:
        self.jsonData[masterkey][key][subkey] = newvalue
        self.commit()

    def commit(self) -> None:
        with open("./helpers/List_Of_books.json", 'w', encoding="utf-8") as f:
            json.dump(self.jsonData, f)
