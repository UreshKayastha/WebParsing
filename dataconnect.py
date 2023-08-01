import pyodbc 
import json

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=KAYASTHA;'
                      'Database=SharePython;'
                      'Trusted_Connection=yes;')

# cursor.execute('SELECT * FROM Master')
with open("today_prices.json","r", encoding='utf-8') as read_file:
    data=json.load(read_file)
    json_string=json.dumps(data)
    try:
        cursor=conn.cursor()
        cursor.execute('Exec ProcInsertingShareValues @json =?',json_string)
        print("Inserted data")
    except pyodbc.Error as err:
        print('Error !!!!!%s' % err)
    except:
        print('Something else failed miserably')
    # conn.close()
    print('Closed SharePrice connection')

with open("top_gainers.json","r", encoding='utf-8') as read_file:
    data=json.load(read_file)
    json_string=json.dumps(data)
    try:
        cursor=conn.cursor()
        cursor.execute('Exec ProcInsertingTopGainers @json =?',json_string)
        print("Inserted data")
    except pyodbc.Error as err:
        print('Error !!!!!%s' % err)
    except:
        print('Something else failed miserably')
    # conn.close()
    print('Closed Top Gainers connection')

with open("top_losers.json","r", encoding='utf-8') as read_file:
    data=json.load(read_file)
    json_string=json.dumps(data)
    try:
        cursor=conn.cursor()
        cursor.execute('Exec ProcInsertingTopLosers @json =?',json_string)
        print("Inserted data")
    except pyodbc.Error as err:
        print('Error !!!!!%s' % err)
    except:
        print('Something else failed miserably')
    conn.close()
    print('Closed Top Losers connection')