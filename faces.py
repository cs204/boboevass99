def main():
    s = input()
    print(convert(s))

def convert(s):
    s2=s.replace(":)", "\N{Slightly Smiling Face}")
    s3=s2.replace(":(", "\N{Slightly Frowning Face}")
    return s3

main()