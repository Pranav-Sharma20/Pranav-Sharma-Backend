from datetime import datetime

def trade_serializer(item) -> dict : 
    return{
        "trade_id" : str(item["trade_id"]),
        "asset_class": str(item["asset_class"]),
        "instrument_id": str(item["instrument_id"]),
        "counterparty": str(item["counterparty"]),
        "instrument_name": str(item["instrument_name"]),
        "trade_date_time": datetime.strptime(item["trade_date_time"],"%d/%m/%Y %H:%M:%S"),
        "trader": str(item["trader"]),
        "trade_details" : {
            "buySellIndicator" : str(item["buySellIndicator"]),
            "price" : float(item["price"]),
            "quantity" : int(item["quantity"])
        }
    }

def trades_serializer(items) -> list :
    return [trade_serializer(item) for item in items]