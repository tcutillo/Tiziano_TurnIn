#TWS
import datetime
import time
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
#myTools
from myTools.createContract import initContract
from myTools.styleCells import addBidAskToSh, styleBidAsk
from myTools.BidAsk import BidAsk
# for Excel
from openpyxl import Workbook
import openpyxl

from myTools.getDays import getDurationBidAsk


class GetBidAsk(EClient, EWrapper):
    def __init__(self, contract, nbDays):
        EClient.__init__(self, self)
        self.myContract = contract
        self.nbDays = nbDays
        self.queryTime = (datetime.datetime.today()).strftime("%Y%m%d-%H:%M:%S")
        self.workbook = None
        self.workBookName = None
        self.sh = None
        self.NTerm = 0

    def nextValidId(self, orderId: int):
        self.reqContractDetails(orderId, self.myContract)
        self.reqMarketDataType(4)
        self.reqHistoricalData(orderId, self.myContract, self.queryTime, getDurationBidAsk(self.nbDays), "10 mins", "BID_ASK", 1, 1, False, [])


    def contractDetails(self, reqId, contractDetails):
        self.workBookName = f"{contractDetails.contract.symbol}.xlsx"
        self.workbook = openpyxl.load_workbook(f"{contractDetails.contract.symbol}.xlsx")
        self.sh = self.workbook[f"{self.nbDays}_Days"]

    def historicalData(self, reqId, bar):
        currentSecurity = BidAsk()
        currentSecurity.minBid = bar.low
        currentSecurity.maxAsk = bar.high
        currentSecurity.maxBidAskSpread = bar.high - bar.low
        currentSecurity.Bid = bar.open
        currentSecurity.Ask = bar.close
        currentSecurity.BidAskSpread = bar.close - bar.open
        addBidAskToSh(self.sh, currentSecurity, self.NTerm + 2)
        if self.NTerm > 0:
            self.avgBidAskSpread += currentSecurity.BidAskSpread
        else:
            self.avgBidAskSpread = currentSecurity.BidAskSpread
        self.NTerm += 1

    def historicalDataEnd(self, reqId, start, end):
        time.sleep(5)
        self.disconnect()


def getMarketData(contract):
    listOfDays = [30, 60, 90]

    for nbDays in listOfDays:
        currentSecurity = GetBidAsk(contract, nbDays)
        currentSecurity.connect("127.0.0.1", 7497, 1)
        currentSecurity.run()
        styleBidAsk(currentSecurity.sh, currentSecurity)
        currentSecurity.workbook.save(currentSecurity.workBookName)

def main():
    # listContracts = initContract([296574745, 297249704, 7089, 470458975, 4215217, 13977, 6890, 5684], ["NYMEX", "IPE", "NYSE", "NYSE", "NYSE", "NYSE", "NYSE", "NYSE"]) #CL1, WTI, FCX, CHK, XLE, XOM, EOG, CVX
    # listContracts = initContract([296574745], ["NYMEX"])  #CL1        80$
    # listContracts = initContract([7089], ["NYSE"])        #FCX        45$
    # listContracts = initContract([470458975], ["NYSE"])   #CHK        90$  
    # listContracts = initContract([4215217], ["NYSE"])     #XLE        87$
    listContracts = initContract([13977], ["NYSE"])         #XOM       110$
    # listContracts = initContract([6890], ["NYSE"])        #EOG       129$
    # listContracts = initContract([5684], ["NYSE"])        #CVX       177$

    for contract in listContracts:
        getMarketData(contract)
    return 0

if __name__ == "__main__":
    main()