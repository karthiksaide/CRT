def reverse_number(n: int) -> int:
    pass
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])
if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))
