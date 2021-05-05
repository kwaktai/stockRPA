import FinanceDataReader as fdr
# print(fdr.__version__)


def day_price(shares):
    df = fdr.DataReader(shares)
    df = df[['Close']].tail(1).values
    # df = df.values
    # https://grand-unified-engine.tistory.com/17
    return print(df)


day_price("tqqq")
