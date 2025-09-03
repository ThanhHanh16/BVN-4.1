def ceasar(plaintext, k):
    S = ""
    for i in plaintext:
        if i.isalpha():
            base = ord("A") if i.isupper() else ord("a")
            S = S + (chr((ord(i) - base + k) % 26 + base))
        else:
            S = S + i
    return S
K = 14
plaintext = "HANH"
ciphertext = ceasar(plaintext, K)
print(f"Chuỗi được mã hóa: {ciphertext}")
             