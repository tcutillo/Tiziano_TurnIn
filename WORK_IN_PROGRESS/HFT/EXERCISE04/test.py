import threading
from ibapi.client import EClient
from ibapi.common import BarData
from ibapi.contract import Contract

from ibapi.wrapper import EWrapper

class MyWrapper(EWrapper):
    def historicalData(self, reqId: int, bar: BarData):
        print("Time:", bar.date, "Open:", bar.open, "High:", bar.high, "Low:", bar.low, "Close:", bar.close, "Volume:", bar.volume)

class MyClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

def historical_data_thread(client, contract, whatToShow):
    client.reqHistoricalData(1, contract, "", "1 Y", "1 day", whatToShow, 1, 1, False, [])

def main():
    wrapper = MyWrapper()
    client = MyClient(wrapper)
    client.connect("127.0.0.1", 7497, 0)

    contract1 = Contract()
    contract1.symbol = "AAPL"
    contract1.secType = "STK"
    contract1.exchange = "SMART"
    contract1.currency = "USD"
    contract1.primaryExch = "NASDAQ"

    thread1 = threading.Thread(target=historical_data_thread, args=(client, contract1, "MIDPOINT"))
    thread1.start()

    contract2 = Contract()
    contract2.symbol = "GOOGL"
    contract2.secType = "STK"
    contract2.exchange = "SMART"
    contract2.currency = "USD"
    contract2.primaryExch = "NASDAQ"

    thread2 = threading.Thread(target=historical_data_thread, args=(client, contract2, "BID_ASK"))
    thread2.start()

    thread1.join()
    thread2.join()

    client.disconnect()

if __name__ == "__main__":
    main()
