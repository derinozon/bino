import sys

def Encode (text) :
    final = str()
    for i in range(0, len(text)): 
        c = ord(text[i])
        
        if (c == 32) :
            final = final + "=+"
        else :
            _c = divmod(c, len(array))
            sym = int(_c[1])
            num = _c[0]
            x = str(num + 1) + "_" + array[sym]
            final = final + x + "+"
        
    final = final[:-1]
    final = final.replace('\n', '').replace('\r', '')
    return final

def Decode (text) :
    final = str()
    textar = text.split("+")
    for i in range(0, len(textar)):
        chnk = textar[i]
        
        if (chnk[0] == "=") :
            final = final + " "
        else :
            _c = chnk.split("_")
            
            sym = _c[1]
            num = int(_c[0])
            sym_ = int()
            for i in range(0, len(array)):
                if array[i] == sym :
                    sym_ = i
            x = (num - 1) * len(array) + sym_
            final = final + chr(x)

    return final

array = [
"H" ,
"He",
"Li",
"Be",
"B",
"C",
"N",
"O",
"F",
"Ne",
"Na",
"Mg",
"Al",
"Si",
"P",
"S",
"Cl",
"Ar",
"K",
"Ca",
"Sc",
"Ti",
"V",
"Cr",
"Mn",
"Fe",
"Co",
"Ni",
"Cu",
"Zn",
"Ga",
"Ge",
"As",
"Se",
"Br",
"Kr",
"Rb",
"Sr",
"Y",
"Zr",
"Nb",
"Mo",
"Tc",
"Ru",
"Rh",
"Pd",
"Ag",
"Cd",
"In",
"Sn",
"Sb",
"Te",
"I",
"Xe",
"Cs",
"Ba",
"La",
"Ce",
"Pr",
"Nd",
"Pm",
"Sm",
"Eu",
"Gd",
"Tb",
"Dy",
"Ho",
"Er",
"Tm",
"Yb",
"Lu",
"Hf",
"Ta",
"W",
"Re",
"Os",
"Ir",
"Pt",
"Au",
"Hg",
"Tl",
"Pb",
"Bi",
"Po",
"At",
"Rn",
"Fr",
"Ra",
"Ac",
"Th",
"Pa",
"U",
"Np",
"Pu",
"Am",
"Cm",
"Bk",
"Cf",
"Es",
"Fm",
"Md",
"No",
"Lr",
"Rf",
"Db",
"Sg",
"Bh",
"Hs",
"Mt",
"Ds",
"Rg",
"Cn",
"Nh",
"Fl",
"Mc",
"Lv",
"Ts",
"Og"
]