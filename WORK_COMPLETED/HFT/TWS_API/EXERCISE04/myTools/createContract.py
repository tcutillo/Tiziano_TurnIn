from ibapi.contract import Contract

def createContract(conId, exchange):
    myContract = Contract()
    myContract.conId = conId
    myContract.exchange = exchange
    return myContract

def initContract(listConID, listExchanges):
    listContract = []
    isExchangeSame = True
    conIdIndex = 0
    exchangeIndex = 0

    if len (listExchanges) > 1:
        isExchangeSame = False

    while conIdIndex < len (listConID):
        listContract.append(createContract(listConID[conIdIndex], listExchanges[exchangeIndex]))
        if isExchangeSame == False:
            exchangeIndex += 1
        conIdIndex += 1

    return listContract