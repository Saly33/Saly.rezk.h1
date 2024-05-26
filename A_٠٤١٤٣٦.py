LI = ["HTTP", "HTTPS", "FTP", "DNS"]
L2 = [80, 443, 21, 53]
d = {LI[i]: L2[i] for i in range(len(LI))}
print(d)
