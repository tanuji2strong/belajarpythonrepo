def divinte(a,b):
    try:
        y=a//b
        return f"{a}/{b} = {y} "
    except ZeroDivisionError:
        print("Error, can't process Zero Division")
        return None
    except TypeError:
        print ("Error, please insert integers.")

print(divinte(10,2))