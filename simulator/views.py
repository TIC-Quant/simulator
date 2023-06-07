from django.shortcuts import render
import cosi

# Create your views here.
def index(request):
    per = get_performance()
    print(cosi.test())
    return render(request, 'simulator/index.html',{
        "performance": get_performance()
    })

def get_performance():
    symbol = 'KRW-BTC'
    df = cosi.get_price(symbol, start_date='2020-01-01', end_date='2020-12-31', interval="day")
    cosi.rsi(df, w=14)
    cosi.indicator_to_signal(df, factor='rsi', buy=30, sell=70)
    cosi.position(df)
    cosi.evaluate(df, cost=.001)
    per = cosi.performance(df, rf_rate=.01)
    print(per)
    return per

def test_dic():
    a = {}
    a['hello'] = "bye"
    return a