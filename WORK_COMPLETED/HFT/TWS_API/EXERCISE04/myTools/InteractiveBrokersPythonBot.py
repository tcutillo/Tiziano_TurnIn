# #Imports
# from decimal import Decimal
# import ibapi
# from ibapi.client import EClient
# from ibapi.common import TickAttrib, TickerId
# from ibapi.ticktype import TickType, TickTypeEnum
# from ibapi.wrapper import EWrapper
# from ibapi.order import *
# from ibapi.contract import Contract, ContractDetails
# import threading
# import time

# #Vars

# #Class for Interactive Brokers Connection
# class IBApi(EWrapper, EClient):
#     def __init__(self):
#         EClient.__init__(self, self)

#     #Listen for realy time bars
#     # def realtimeBar(self, reqId, time, open_, high, low, close, volume, wap, count):
#     #     super().realtimeBar(reqId, time, open_, high, low, close, volume, wap, count)
#     #     try:
#     #         bot.on_bar_update(reqId, time, open_, high, low, close, volume, wap, count)
#     #     except Exception as e:
#     #         print(e)
#     # def error(self, id, errorCode, errorMsg):
#     #     print(errorCode)
#     #     print(errorMsg)

#     def contractDetails(self, reqId: int, contractDetails: ContractDetails):
#         print(f"contract details: {contractDetails}")
    
#     def contractDetailsEnd(self, reqId: int):
#         print("End of contractDetails")
#         self.disconnect

#     def tickSize(self, reqId: TickerId, tickType: TickType, size: Decimal):
#         print(f"tickSize: {reqId} - {TickTypeEnum.to_str(tickType)}({tickType}) - {size}")

#     def tickPrice(self, reqId: TickerId, tickType: TickType, price: float, _attrib: TickAttrib):
#         print(f"tickPrice: {reqId} - {TickTypeEnum.to_str(tickType)}({tickType}) - {price}")

# #Bot Logic
# class Bot():
#     ib = None
#     def __init__(self):
#         self.ib = IBApi()
#         self.ib.connect("127.0.0.1", 7497, clientId=0)
#         ib_thread = threading.Thread(target=self.run_loop, daemon=True)
#         ib_thread.start()
#         time.sleep(1)
#         # Get Symbol info
#         symbol = input("Enter the symbol you want to trade : ")
#         # Created our IB Contract Object
#         contract = Contract()
#         contract.symbol = symbol.upper()
#         contract.secType = "STK"
#         contract.exchange = "SMART"
#         contract.currency = "USD"

#         #Request Market Data
#         self.ib.reqMarketDataType(3)
#         self.ib.reqMktData(1, contract, "", True, False, None)
        
#         # self.ib.reqContractDetails(1, contract)



#     def run_loop(self):
#         self.ib.run()

# bot = Bot()

















#         # self.ib.reqRealTimeBars(0, contract, 5, "TRADES", 0, [])

#     #Listen to socket in seprate thread
#     # def run_loop(self):
#     #     self.ib.run()
#     #Pass realtime bar data back to our bot object
#     # def on_bar_update(self, reqId, time, open_, high, low, close, volume, wap, count):
#     #     print(close)
# # Start Bot

#     #seperate thread
#     # myContract = Contract()
#     # myContract.conId = 265598 (AAPL)
#     # myContract.conId = 15124833 (NFLX)
#     # myContract.conId = 13977 (XOM)
#     # myContract.conId = 756733 (SPY)
#     # myContract.conId = 76792991 (TSLA)
#     # myContract.conId = 11017 (PEP)
#     # myContract.conId = 9599491 (F)
#     # myContract.conId = 140070600 (AMC)
#     # myContract.conId = BITCOIN
#     # myContract.conId = DOGE
#     # myContract.symbol = "AMC"
#     # myContract.secType = "STK"
#     # myContract.exchange = "SMART"
#     # myContract.currency = "USD"

#     # time.sleep(3)

#     # app.reqMarketDataType(3)
#     # app.reqMktData(1, myContract, "", True, False, None)


#     # app.reqContractDetails(1, myContract)

#     # app.run()
#     # app.disconnect()

#     #Listen to socket in seperate thread
        
import datetime
import os
import time
from ibapi.client import EClient
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum
from ibapi.wrapper import EWrapper


class TWSApp(EClient, EWrapper):
    def __init__(self, list_ConId, list_Exchange):
        EClient.__init__(self, self)
        self.Contract_conId = list_ConId # récuperationn de conId dans une variable
        self.Contract_exchange = list_Exchange # récuperationn de l'exchage dans une variable
        # varible utile a la récupération des 10 informations demandé
        self.CON_ID = 0
        self.TICKER = 0
        self.PRICE = 0
        self.BAR_COUNT = 0
        self.VOLUME = 0
        self.HIGH_PRICE = 0 
        self.LOW_PRICE = 0
        self.CURRENT_PRICE = 0
        self.WAP = 0
        self.VWAP = -1
    
    def nextValidId(self, orderId: int):
        # création du contract en utilisant le conId et l'exchange, et j'ajoute le secType a crypto que quand la class est utiliser pour afficher des infos sur des crypto
        myContract = Contract()
        myContract.conId = self.Contract_conId
        myContract.exchange = self.Contract_exchange
        if myContract.exchange == "PAXOS":
            myContract.secType = "CRYPTO"

        # je crois aue cette fonction est utile pour le bon fonctionnement de reqMktData()
        self.reqMarketDataType(4)
        # cette fonction est utiles pour nous envoyer toutes les informations liées aux prices ()prices, low price, ...)
        self.reqMktData(orderId, myContract, "", 0, 0, [])
        # 
        queryTime = (datetime.datetime.today()).strftime("%Y%m%d-%H:%M:%S")
        self.reqHistoricalData(orderId, myContract, queryTime, "1 M", "1 day", "TRADES", 1, 1, False, [])

        # cette fonction est utile pour nous envoyer le conId et le ticker (sleep utile pour attendre que les données soit bien chargées)
        time.sleep(3)
        self.reqContractDetails(orderId, myContract)

    def contractDetails(self, reqId, contractDetails):
        # dans cette fonction je récupére donc les résultats de la fonction self.reqContractDetails(1, myContract) dans mes variable associée
        # print(f" contract details: {contractDetails}")
        self.CON_ID = contractDetails.contract.conId
        self.TICKER = contractDetails.contract.symbol
        # print("\n")

    def tickPrice(self, reqId, tickType, price, attrib):
        # dans cette fonction je récupére les résultats de la fonction self.reqMktData(orderId, myContract, "", 0, 0, []) dans mes variables associées

        # print(f"tickPrice. reqId: {reqId}, tickType: {tickType}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attribs: {attrib}")
        if tickType == TickTypeEnum.DELAYED_LAST or tickType == 4:
            self.PRICE = price
        if tickType == TickTypeEnum.DELAYED_HIGH or tickType == 6:
            self.HIGH_PRICE = price
        if tickType == TickTypeEnum.DELAYED_LOW or tickType == 7:
            self.LOW_PRICE = price
        if tickType == TickTypeEnum.DELAYED_ASK or tickType == 2:
            self.CURRENT_PRICE = price
        

    def historicalData(self, reqId, bar):
        # dans cette fonction je récupére les résultats de la fonction self.reqHistoricalData() dans mes variables associées

        print(f"Historical Data: {bar}")
        self.BAR_COUNT = bar.barCount
        self.VOLUME = bar.volume
        self.WAP = bar.wap
        
    def contractDetailsEnd(self, reqId):
        self.disconnect()

def main():
    # list de conId des actions (APPL, MSFT, TSLA,...)
    list_ConId = [416904]
    # list de conId des crypto (BTC et ETH)
    # list_ConId_crypto = [479624278, 495759171]
    # list d'exchange
    list_Exchange = ["CBOE", "SMART", "PAXOS"]

    if os.path.exists("TWS_result.txt"):
        os.remove("TWS_result.txt")
    f = open("TWS_result.txt", 'w')
    f.write("ConId,Ticker,Price,Bar_Count,Volume,High_Price,Low_Price,Current_Price,WAP,VWAP\n")

    # premiere boucle pour ajouter dans le fichier les actions
    i = 0
    while i != len(list_ConId):
        # appel de la class en boucle avec en parametre les conId des actions et leurs exchange "SMART"
        app = TWSApp(list_ConId[i], list_Exchange[0])
        app.connect("127.0.0.1", 7497, 1000)
        app.run()
        f.write(str(app.CON_ID) + ",")
        f.write(str(app.TICKER) + ",")
        f.write(str(app.PRICE) + ",")
        f.write(str(app.BAR_COUNT) + ",")
        f.write(str(app.VOLUME) + ",")
        f.write(str(app.HIGH_PRICE) + ",")
        f.write(str(app.LOW_PRICE) + ",")
        f.write(str(app.CURRENT_PRICE) + ",")
        f.write(str(app.WAP) + ",")
        f.write(str(app.VWAP))
        f.write("\n")
        i += 1
    # deuxieme boucle pour ajouter dans le fichier les crypto
    # j = 0
    # while j != len(list_ConId_crypto):
    #     # appel de la class en boucle avec en parametre les conId des crypto et leurs exchange "PAXOS"
    #     app = TWSApp(list_ConId_crypto[j], list_Exchange[1])
    #     app.connect("127.0.0.1", 7497, 1000)
    #     app.run()
    #     f.write(str(app.CON_ID) + ",")
    #     f.write(str(app.TICKER) + ",")
    #     f.write(str(app.PRICE) + ",")
    #     f.write(str(app.BAR_COUNT) + ",")
    #     f.write(str(app.VOLUME) + ",")
    #     f.write(str(app.HIGH_PRICE) + ",")
    #     f.write(str(app.LOW_PRICE) + ",")
    #     f.write(str(app.CURRENT_PRICE) + ",")
    #     f.write(str(app.WAP) + ",")
    #     f.write(str(app.VWAP))
    #     f.write("\n")
    #     j += 1
    f.close()

    # print("conId:", app.CON_ID)
    # print("TICKER:", app.TICKER)
    # print("PRICE:", app.PRICE)
    # print("BAR_COUNT:", app.BAR_COUNT)
    # print("VOLUME:", app.VOLUME)
    # print("HIGH_PRICE:", app.HIGH_PRICE)
    # print("LOW_PRICE:", app.LOW_PRICE)
    # print("CURRENT_PRICE:", app.CURRENT_PRICE)
    # print("WAP:", app.WAP)
    # print("VWAP:", app.VWAP)

if __name__ == "__main__":
    main()

#Dow ConID
#551801503

#S&P 500
#495512572

#YM = Dow
#ES = S&P
#NQ = Nasdaq