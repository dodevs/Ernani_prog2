def raizes(a,b,c):
    if a == 0:
        return None
    else:
        delta = b*b - 4 * a * c
        if delta < 0:
            return None, None
        else:
            r1 = (-b + (delta)**(1/2))/2
            r2 = (-b - (delta)**(1/2))/2

            return r1, r2


def main():
    print(raizes(1, -5, 6))

if __name__ == "__main__":
    main()
