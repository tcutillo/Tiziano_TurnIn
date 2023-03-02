
def getDuration(nbDays):
    if nbDays == 30:
        return "31 D"
    if nbDays == 60:
        return "61 D"
    if nbDays == 90:
        return "91 D"
    return "31 D"

def getDurationBidAsk(nbDays):
    if nbDays == 30:
        return "30 D"
    if nbDays == 60:
        return "60 D"
    if nbDays == 90:
        return "90 D"
    return "30 D"

def getAvgVolumeBar(avgVolume, nbDays):
    if nbDays == 30:
        return avgVolume / 1170
    if nbDays == 60:
        return avgVolume / 2322
    if nbDays == 90:
        return avgVolume / 3491

def getAvgBidAskSpread(avgBidAskSpread, nbDays):
    if nbDays == 30:
        return avgBidAskSpread / 1170
    if nbDays == 60:
        return avgBidAskSpread / 2322
    if nbDays == 90:
        return avgBidAskSpread / 3491