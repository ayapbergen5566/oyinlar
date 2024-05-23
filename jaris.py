oyinshi1 = input("1-oyinshi ati: ")
oyinshi2 = input("2-oyinshi ati: ")
while True:
    soraw = input("Oyindi baslaymizba (awa/yaq): ")
    if soraw == "yaq":
        print("Oyin tawsildi")
        break
    elif soraw == "awa":
        harip1 = input(f"{oyinshi1} ushin (so'z/harip/san): ")
        harip2 = input(f"{oyinshi2} ushin (so'z/harip/san): ")
        print("Oyin baslandi")
        oyin = input("Jazin: ")
        o1 = oyin.count(harip1)
        o2 = oyin.count(harip2)
        print(f"{harip1} : {o1}")
        print(f"{harip2} : {o2}")
        if o1 > o2:
            print(f"{oyinshi1} utti")
        elif o2 > o1:
            print(f"{oyinshi2} utti")
        else:
            print("Ten")
    else:
        continue
