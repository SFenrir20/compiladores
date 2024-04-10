from Scanner_comp import Scanner

def main():
    sc = Scanner("input.isis")
    token = None
    while True:
        token = sc.next_token()
        token.to_string()
        if token == None:
            break


if __name__ == "__main__":
    main()