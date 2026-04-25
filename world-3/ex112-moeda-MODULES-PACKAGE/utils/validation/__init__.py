def validData(data):
    data = data.replace(",", ".")
    try: float(data)
    except ValueError:
        return False
    else:
        return float(data)