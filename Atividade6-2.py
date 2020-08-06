known_m = {0:0, 1:1}
known_n = {0:0, 1:1}
def ack(m,n):
    if m not in known_m:
        known_m[m] = m
    if n not in known_n:
        known_n[n] = n
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1,n)
    return ack(m-1, ack(m,n-1))

print(ack(3,4))