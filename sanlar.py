import random
sanaq = 1
while True:
    soraw = input("Oyindi baslaymizba (awa/yaq): ")
    if soraw == "yaq":
        print("Oyin tawsildi")
        break
    elif soraw == "awa":
        print("Oyin baslandi")
        a = int(input("Qaysi sanga shekem oynaysiz: "))
        san = random.randint(1,a)
        while True:
            b = input("Sandi kiritin: ")
            if b.isdigit() and int(b) == san:
                print("Siz {sanaq} marte urinip aqiri sandi taptiniz")
                break
            elif b.isdigit() and int(b) < san:
                print("Siz kiritken san juda kishi!")
                sanaq += 1
                continue
            elif b.isdigit() and int(b) > san:
                print("Siz kiritken san juda ulken!")
                sanaq += 1
                continue
            elif b.isalpha() and b == "stop":
                print(f"Oyin tawsildi ham san {san} edi")
                break
            else:
                print("Qatelik")
                continue
    else:
        continue
