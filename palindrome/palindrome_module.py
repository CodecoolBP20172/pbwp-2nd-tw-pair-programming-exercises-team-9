def palindrome(para):
    if para.replace(" ", "").lower() == para.replace(" ", "").lower()[::-1]:
        return True
    else:
        return False


def main():
    return


if __name__ == '__main__':
    main()

lofasz = "A nut for a jar of tuna"
print(lofasz.replace(" ", "").lower()[::-1])