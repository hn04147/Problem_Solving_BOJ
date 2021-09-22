h, m = map(int, input().split())
_h = h if m >= 45 else (h+23)%24
_m = m-45 if m >= 45 else m+15
print(_h, _m)