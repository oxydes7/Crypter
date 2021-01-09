# Crypter

Sıkıldığımda yazdığım bir crypter. Güvenli olduğunu iddia etmiyorum ki değil zaten, yazma amacım önemli metinlerinizi(şifre vb) şifrelemek. Decode aşaması zor olsun diye farklı şifreleme algoritmaları kullandım.

# Encode Algoritması

1)Kullanıcıdan şifrelenecek veriyi al

2)Veriyi önce rot13 algoritması ile şifrele

3)rot13 ile şifrelenen veriyi al ve base64 ile şifrele

4)base64 ile şifrelenen veriyi base32 ile şifrele

5)base32 ile şifrelenen veriyi tekrar rot13 ile şifrele

6)rot13 ile şifrelenen veriyi otp ile şifrele

# Decode Algoritması

1)Kullanıcıdan hash al

2)Kullanıcıdan key al

3)Hash ve key'i kullanıp onetimepad'de veriyi decryptle

4)Aldığın veriyi rot13 ile decode et

5)aldığın veriyi base32 ile decode et

6)Aldığın veriyi Base64 ile decode et

7)Aldığın veriyi tekrar rot13 ile decode et

