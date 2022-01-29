#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Unicode


def convert(inp):
    # convert string to unicode

    # variables
    to_unicode = []

    # creating/setting unicode unicode
    unicode = {}
    unicode[" "] = "0x20"
    unicode["!"] = "0x21"
    unicode['"'] = "0x22"
    unicode["#"] = "0x23"
    unicode["$"] = "0x24"
    unicode["%"] = "0x25"
    unicode["&"] = "0x26"
    unicode["'"] = "0x27"
    unicode["("] = "0x28"
    unicode[")"] = "0x29"
    unicode["*"] = "0x2a"
    unicode["+"] = "0x2b"
    unicode[","] = "0x2c"
    unicode["-"] = "0x2d"
    unicode["."] = "0x2e"
    unicode["/"] = "0x2f"
    unicode["0"] = "0x30"
    unicode["1"] = "0x31"
    unicode["2"] = "0x32"
    unicode["3"] = "0x33"
    unicode["4"] = "0x34"
    unicode["5"] = "0x35"
    unicode["6"] = "0x36"
    unicode["7"] = "0x37"
    unicode["8"] = "0x38"
    unicode["9"] = "0x39"
    unicode[":"] = "0x3a"
    unicode[";"] = "0x3b"
    unicode["<"] = "0x3c"
    unicode["="] = "0x3d"
    unicode[">"] = "0x3e"
    unicode["?"] = "0x3f"
    unicode["@"] = "0x40"
    unicode["A"] = "0x41"
    unicode["B"] = "0x42"
    unicode["C"] = "0x43"
    unicode["D"] = "0x44"
    unicode["E"] = "0x45"
    unicode["F"] = "0x46"
    unicode["G"] = "0x47"
    unicode["H"] = "0x48"
    unicode["I"] = "0x49"
    unicode["J"] = "0x4a"
    unicode["K"] = "0x4b"
    unicode["L"] = "0x4c"
    unicode["M"] = "0x4d"
    unicode["N"] = "0x4e"
    unicode["O"] = "0x4f"
    unicode["P"] = "0x50"
    unicode["Q"] = "0x51"
    unicode["R"] = "0x52"
    unicode["S"] = "0x53"
    unicode["T"] = "0x54"
    unicode["U"] = "0x55"
    unicode["V"] = "0x56"
    unicode["W"] = "0x57"
    unicode["X"] = "0x58"
    unicode["Y"] = "0x59"
    unicode["Z"] = "0x5a"
    unicode["["] = "0x5b"
    unicode["\\"] = "0x5c"
    unicode["]"] = "0x5d"
    unicode["^"] = "0x5e"
    unicode["_"] = "0x5f"
    unicode["`"] = "0x60"
    unicode["a"] = "0x61"
    unicode["b"] = "0x62"
    unicode["c"] = "0x63"
    unicode["d"] = "0x64"
    unicode["e"] = "0x65"
    unicode["f"] = "0x66"
    unicode["g"] = "0x67"
    unicode["h"] = "0x68"
    unicode["i"] = "0x69"
    unicode["j"] = "0x6a"
    unicode["k"] = "0x6b"
    unicode["l"] = "0x6c"
    unicode["m"] = "0x6d"
    unicode["n"] = "0x6e"
    unicode["o"] = "0x6f"
    unicode["p"] = "0x70"
    unicode["q"] = "0x71"
    unicode["r"] = "0x72"
    unicode["s"] = "0x73"
    unicode["t"] = "0x74"
    unicode["u"] = "0x75"
    unicode["v"] = "0x76"
    unicode["w"] = "0x77"
    unicode["x"] = "0x78"
    unicode["y"] = "0x79"
    unicode["z"] = "0x7a"
    unicode["{"] = "0x7b"
    unicode["|"] = "0x7c"
    unicode["}"] = "0x7d"
    unicode["~"] = "0x7e"

    # process
    for char in inp:
        to_unicode.append(unicode[char])

    # return list
    return to_unicode


def main():
    # main function, calling convert

    # input
    inp = input("String: ")

    # output/calling function
    print(f"{inp} in hex is: {convert(inp)}")

    # done
    print("\nDone.")

if __name__ == "__main__":
    main()
