
def main(P, Q, R):
    print(min([P+Q, Q+R, P+R]))

if __name__ == "__main__":
    P, Q, R = [int(x) for x in input().split()]

    main(P, Q, R)
