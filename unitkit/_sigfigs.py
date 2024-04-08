def count(number):
    number = str(number).lstrip("-").split("e")[0]
    integer, _, decimal = number.partition(".")
    if decimal:
        return len((integer + decimal).lstrip("0"))
    return len(integer.strip("0"))

def round(number, n):
    #TODO: implement this function
    return number