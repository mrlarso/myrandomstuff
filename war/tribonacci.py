def tribonacci(signature,n):
    if n < 3:
        return signature[:n]
    while len(signature) != n:
        signature.append(sum(signature[-3:]))
    return signature
