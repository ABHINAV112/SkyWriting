def autoCorrect(text):
    from gingerit.gingerit import GingerIt

    parser = GingerIt()
    return parser.parse(text)['result']

if(__name__=="__main__"):
    a = autoCorrect("sweut")
    print(a)