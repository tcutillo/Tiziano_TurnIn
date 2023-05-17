from ib_insync import *
import csv
from datetime import datetime

def months_between_dates(start_date, end_date):
    start = datetime.strptime(start_date, '%m/%d/%y')
    end = datetime.strptime(end_date, '%m/%d/%y')
    num_months = (end.year - start.year) * 12 + (end.month - start.month)
    return num_months

def getSeaRule(capitale, months):
    if months < 12:
        return capitale * 0.02
    if months >= 12 and months < 24:
        return capitale * 0.03
    if months >= 24 and months < 36:
        return capitale * 0.05
    if months >= 36 and months < 60:
        return capitale * 0.06
    if months >= 60 and months < 120:
        return capitale * 0.07
    if months >= 120 and months < 180:
        return capitale * 0.075
    if months >= 180 and months < 240:
        return capitale * 0.08
    if months >= 240 and months < 300:
        return capitale * 0.085
    if months >= 300:
        return capitale * 0.09

def bond_contract_details(bond_type, exchange, con_id):
    contract = Contract()
    contract.secType = bond_type
    contract.exchange = exchange
    contract.conId = con_id
    return contract

def save_to_csv(filename, header, rows):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)

def main():
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)
    exchange = 'SMART'
    contractID = [29157676, 185858451, 415066061, 285736417, 242880990, 150258828]
    header = ['contractID', 'contract Details', 'Position', 'Quantity', 'Price', 'Cash Allocation', 'SEA Rule', 'REG-T']
    rows = []

    for conID in contractID:
        contract = bond_contract_details('BOND', exchange, conID)
        contractDetails = ib.reqContractDetails(contract)
        ib.sleep(1)

        ib.reqMarketDataType(1)
        data = ib.reqMktData(contract, '', False, False)
        ib.sleep(1)

        order = MarketOrder('BUY', 10)
        trade = ib.placeOrder(contract, order)
        trade_order = trade.order
        ib.sleep(1)

        row = [conID, contractDetails[0].descAppend, "LONG", 10, data.close, (data.close*10)*10, getSeaRule((data.close*10)*10, months_between_dates('05/15/23', contractDetails[0].descAppend.split()[-1])), ((data.close*10)*10) * 0.5]
        print(row)
        rows.append(row)
        # print(contractDetails[0].descAppend)

    save_to_csv('data.csv', header, rows)
    ib.disconnect()

if __name__ == "__main__":
    main()
