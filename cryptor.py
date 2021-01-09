"""
Encoder pseudo ;
1)Kullanıcıdan şifrelenecek veriyi al
2)Veriyi önce rot13 algoritması ile şifrele
3)rot13 ile şifrelenen veriyi al ve base64 ile şifrele
4)base64 ile şifrelenen veriyi base32 ile şifrele
5)base32 ile şifrelenen veriyi tekrar rot13 ile şifrele
6)rot13 ile şifrelenen veriyi otp ile şifrele
"""

try:
    # imports
    import subprocess
    from time import sleep
    import base64
    import onetimepad
    import colorama
    import codecs
    import pyperclip

    class Cryptography:
        def banner():
            print("""
              ______________________________
             / ___|  _ \ \ / /  _ \_   _/ _ \ 
            | |   | |_) \ V /| |_) || || | | |
            | |___|  _ < | | |  __/ | || |_| |
             \____|_| \_\|_| |_|    |_| \___/ 

            """)
        def encode():
            subprocess.run(["clear"])
            subprocess.run(["figlet", "ENCODER"])
            while True:
                text = input("Encode edilecek veriyi girin >> ")
                if text != "":
                    # rot13 encoding
                    rot13 = codecs.encode(text, "rot_13")
                    print(colorama.Fore.GREEN + f"1.ADIM BAŞARILI --> {rot13}")
                    sleep(1)

                    # base64 encoding
                    encodedBytes = base64.b64encode(rot13.encode("utf-8"))
                    base64EncodedString = str(encodedBytes, "utf-8")
                    print(
                        colorama.Fore.GREEN
                        + f"2. ADIM BAŞARILI --> {base64EncodedString}"
                    )
                    sleep(1)

                    # base32 encoding
                    encodedBytes2 = base64.b32encode(
                        base64EncodedString.encode("utf-8")
                    )
                    base32EncodedString = str(encodedBytes2, "utf-8")
                    print(
                        colorama.Fore.GREEN
                        + f"3. ADIM BAŞARILI --> {base32EncodedString}"
                    )
                    sleep(1)

                    # rot13 encoding step 2
                    rot13step2 = codecs.encode(base32EncodedString, "rot_13")
                    print(colorama.Fore.GREEN + f"4.ADIM BAŞARILI --> {rot13step2}")
                    sleep(1)

                    # onetimepad encode
                    key = input("\nLütfen bir anahtar girin >> ")
                    encodedOTP = onetimepad.encrypt(rot13step2, key)
                    sleep(1)
                    print(colorama.Fore.GREEN + f"5. ADIM BAŞARILI --> {encodedOTP}")
                    sleep(3)

                    subprocess.run(["clear"])
                    sleep(1)
                    print(
                        f"Şifreleme işlemi bitti, '{text}' verisinin şifrelenmiş hali > {encodedOTP}"
                    )
                    pyperclip.copy(encodedOTP)
                    print(
                        f"Şifrelenen veri panoya kopyalandı"
                    )
                    False
                    break
                    print(
                        f""
                    )

                if text == "":
                    print("Boş değer giremezsiniz!")
                    encode()

        """
        Decoder pseudo ;
        1)Kullanıcıdan hash al
        2)Kullanıcıdan key al
        3)Hash ve key'i kullanıp onetimepad'de veriyi decryptle
        4)Aldığın veriyi rot13 ile decode et
        5)aldığın veriyi base32 ile decode et
        6)Aldığın veriyi Base64 ile decode et
        7)Aldığın veriyi tekrar rot13 ile decode et
        """

        def decode():
            subprocess.run(["clear"])
            subprocess.run(["figlet", "DECODER"])
            # hashi al
            myHash = input(colorama.Fore.CYAN + "Decode edilecek veriyi girin >> ")
            print(colorama.Fore.GREEN + "Decode işlemi 2sn sonra başlayacak.")
            sleep(2)
            subprocess.run(["clear"])
            # anahtarı al ve decode et
            key4decode = input(colorama.Fore.RED + "Anahtarı girin >> ")
            decodeOTP = onetimepad.decrypt(myHash, key4decode)
            print(colorama.Fore.GREEN + f"Decode işlemi başarılı, sonuç --> {decodeOTP}")
            sleep(1)
            # rot13 decode
            decodeROT13 = codecs.decode(decodeOTP, "rot_13")
            print(colorama.Fore.GREEN + f"Decode işlemi yapıldı, sonuç --> {decodeROT13}")
            sleep(1)
            # base32
            b32bytes = decodeROT13.encode("utf-8")
            messageBytes = base64.b32decode(b32bytes)
            message = messageBytes.decode("utf-8")
            print(colorama.Fore.GREEN + f"Decode işlemi yapıldı, sonuç --> {message}")
            sleep(1)
            # base64
            b64bytes = message.encode("utf-8")
            messageBytes2 = base64.b64decode(b64bytes)
            message2 = messageBytes2.decode("utf-8")
            print(colorama.Fore.GREEN + f"Decode işlemi yapıldı, sonuç --> {message2}")
            sleep(1)
            # rot13 step 2
            decodeROT13step2 = codecs.decode(message2, "rot_13")
            print(colorama.Fore.GREEN + f"Decode işlemi yapıldı, sonuç --> {decodeROT13step2}")
            # end
            sleep(5)
            subprocess.run("clear")
            print(
                colorama.Fore.GREEN + f"Şifreleme işlemi bitti, '{myHash}' hashinin '{key4decode}' anahtarı ile şifrelenmiş hali > {decodeROT13step2}"
            )
            pyperclip.copy(decodeROT13step2)
            print(
                colorama.Fore.GREEN + f"\nŞifre panoya kopyalandı."
            )

        while True:
            sleep(5)
            banner()
            subprocess.run(["clear"])
            print(
                colorama.Fore.GREEN + 
                """
                1)Encode
                2)Decode
                3)Encode Algorithm
                4)Decode Algorithm
                5)Exit
                """
            )
            secim = int(input(colorama.Fore.CYAN + "\n\nSeçiminizi girin >> "))
            if secim == 1:
                encode()
            elif secim == 2:
                decode()
            elif secim == 3:
                print("""
                Encoder pseudo ;
                1)Kullanıcıdan şifrelenecek veriyi al
                2)Veriyi önce rot13 algoritması ile şifrele
                3)rot13 ile şifrelenen veriyi al ve base64 ile şifrele
                4)base64 ile şifrelenen veriyi base32 ile şifrele
                5)base32 ile şifrelenen veriyi tekrar rot13 ile şifrele
                6)rot13 ile şifrelenen veriyi otp ile şifrele
                """)
            elif secim == 4:
                print("""
                Decoder pseudo ;
                1)Kullanıcıdan hash al
                2)Kullanıcıdan key al
                3)Hash ve key'i kullanıp onetimepad'de veriyi decryptle
                4)Aldığın veriyi rot13 ile decode et
                5)aldığın veriyi base32 ile decode et
                6)Aldığın veriyi Base64 ile decode et
                7)Aldığın veriyi tekrar rot13 ile decode et
                """)
            elif secim == 5:
                subprocess.run(["clear"])
                print("Hoşçakal")
                sleep(2)
                subprocess.run(["clear"])
                False
                break
            elif secim == "":
                print(colorama.Fore.RED + "Boş Değer Giremezsiniz.")
                False
            else:
                print(colorama.Fore.RED + "Hata.")
                False


except KeyboardInterrupt:
    subprocess.run(["clear"])
    print("Hoşçakal.")
    sleep(2)
    subprocess.run("clear")
    # decode()
    # encode()


crypt = Cryptography()
