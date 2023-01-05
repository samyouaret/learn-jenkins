import fire


def printHello(name="Sam"):
    return "Marhba %s" % name


if __name__ == "__main__":
    fire.Fire(printHello)
