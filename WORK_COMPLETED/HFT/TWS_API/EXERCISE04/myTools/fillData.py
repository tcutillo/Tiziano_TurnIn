# from energieRegression import TWSApp

def fillData(marketData, currentSecurity, listOfMarketData, bar, dateSplit):
    i = 0
    currentSecurity.Nterm = marketData.NTerm - 39
    currentSecurity.date = dateSplit[0]
    currentSecurity.time = dateSplit[1]
    currentSecurity.currentPrice = bar.close
    currentSecurity.changePrevPriceDollar = currentSecurity.currentPrice - listOfMarketData[-1].currentPrice
    currentSecurity.changePrevPricePercentage = round((currentSecurity.changePrevPriceDollar / listOfMarketData[-1].currentPrice) * 100, 2)
    currentSecurity.volume = bar.volume
    currentSecurity.yestPriorVolume = listOfMarketData[len(listOfMarketData) - 39].volume

    if currentSecurity.time == "09:30:00":
        currentSecurity.yestCls = listOfMarketData[-1].currentPrice
        currentSecurity.changeYestCls = currentSecurity.currentPrice - currentSecurity.yestCls
        while i != 39:
            currentSecurity.totalVolumeYest += listOfMarketData[len(listOfMarketData) - (39 + i)].volume
            i += 1
        
    else:
        currentSecurity.yestCls = listOfMarketData[-1].yestCls
        currentSecurity.changeYestCls = currentSecurity.currentPrice - listOfMarketData[-1].yestCls
        currentSecurity.totalVolumeYest = listOfMarketData[-1].totalVolumeYest

    return currentSecurity