def convert(IP_Adress : str) -> str:
    ans=""
    for ch in IP_Adress:
        if ch ==".":
            ans+=":"
        else:
            ans+=ch
    return ans



    

ip="192.168.0.0"
print(convert(ip))