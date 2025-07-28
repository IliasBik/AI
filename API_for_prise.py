import requests
import pandas as pd
from tqdm import tqdm
from datetime import datetime, timedelta
#tickets_used = ["AFKS","AFLT","CHMF","FLOT","GAZP","GMKN","LKOH","MGNT","MOEX","NVTK","PHOR","PLZL","ROSN","SBER","SNGS", "SNGSP", "TATN", "TRNFP", "VKCO", "VTBR"]
#tickets = ["RUAL"]
tickets = []
f = open("first_eshelon.txt")
base = f.readlines()
for i in base:
    tickets.append(i[:-1])
f.close()




for ticket in tickets:
    print(ticket)
    if tickets.index(ticket) < tickets.index("YDEX"):
        #print(ticket)
        continue
    url = f"https://iss.moex.com/iss/engines/stock/markets/shares/securities/{ticket}/candles.json"

    start = '2012-01-01'
    end = '2025-01-20'

    start2 = datetime.strptime(start, "%Y-%m-%d")
    start2 = start2 + timedelta(days=7)

    end2 = datetime.strptime(end, "%Y-%m-%d")
    end2 = end2 + timedelta(days=7)

    dates1 = pd.date_range(start=start, end=end, freq='W')
    dates2 = pd.date_range(start=start2, end=end2, freq='W')
    #print(dates1)
    params = {
        'from': str(dates1[0])[:10],
        'till': str(dates2[0])[:10],
        'interval': '10', # Интервал месяц - 31, неделя - 7, час - 60, 10 минут - 10, 1 минута - 1 
    }
    response = requests.get(url, params=params)
    data = response.json()
    candles_data = data['candles']['data']
    columns = data['candles']['columns']
    df = pd.DataFrame(candles_data, columns=columns)
    #print(len(dates1))
    #print(len(dates2))
    for i in tqdm(range(1,len(dates1))):
        #if i % 100 == 0:
        #    print(str(int(i/len(dates1) * 10000) / 100) + "%" + "  " + ticket)
        params = {
            'from': str(dates1[i])[:10],
            'till': str(dates2[i])[:10],
            'interval': '10',  # Интервал месяц - 31, неделя - 7, час - 60, 10 минут - 10, 1 минута - 1
        }

        response = requests.get(url, params=params, timeout=500)
        data = response.json()
        candles_data = data['candles']['data']
        columns = data['candles']['columns']
        df1 = pd.DataFrame(candles_data, columns=columns)
        #print(df1)
        if (not df1.empty):
            df = pd.concat([df, df1])
        #print(str(dates1[i])[:10] + " " + str(dates2[i])[:10])


    file = "D:/Desktop/IA/IA/DATASETS/" + ticket + "_10.txt"
    df.to_csv(file, index=False)
