import periodic_en as func

term = {
	"RESET": "\033[0m",
	"BLACK": "\033[30m",
	"RED": "\033[31m",
	"GREEN": "\033[32m",
	"YELLOW":  "\033[33m",
	"BLUE":    "\033[34m",
	"MAGENTA": "\033[35m",
	"CYAN":    "\033[36m",
	"WHITE":   "\033[37m",
	"BOLDBLACK":   "\033[1m\033[30m",
	"BOLDRED":     "\033[1m\033[31m",
	"BOLDGREEN":   "\033[1m\033[32m",
	"BOLDYELLOW":  "\033[1m\033[33m",
	"BOLDBLUE":    "\033[1m\033[34m",
	"BOLDMAGENTA": "\033[1m\033[35m",
	"BOLDCYAN":    "\033[1m\033[36m",
	"BOLDWHITE":   "\033[1m\033[37m"
}

def main () :
    method = input(term["BLUE"] + "encode / decode >>> " + term["RESET"])

    if (method == "encode") :
        txt = input(term["BLUE"] + "Text to encode >>> " + term["RESET"])
        ret = func.Encode(txt)
        input(ret)
    elif (method == "decode") :
        txt = input(term["BLUE"] + "Text to decode >>> " + term["RESET"])
        ret = func.Decode(txt)
        input(ret)
    else :
        print("Command not found")

    main()

main()