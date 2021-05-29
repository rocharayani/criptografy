#encoding: utf-8
#coding: latin-1
letras = {
	"A": "P",
    "B": "Y",
	"C": "F",
    "D": "G",
	"E": "C",
    "F": "R",
	"G": "L",
    "H": "A",
	"I": "O",
    "J": "E",
	"K": "U",
    "L": "I",
    "M": "D",
    "N": "H",
	"O": "T",
    "P": "N",
	"Q": "S",
    "R": "Q",
	"S": "J",
    "T": "K",
	"U": "X",
    "V": "B",
	"W": "M",
    "X": "W",
    "Y": "V",
    "Z": "Z"
}

#entrada da palavra a ser criptografada. 
criptografado = input(str("Digite a mensagem a ser encriptada: "))

#passagem da palavra para letra maiuscula e assim evitar que o programa apresente erro ao inserirmos letras minusculas
criptografado = criptografado.upper()

#input digitado "junta" as letras criptografadas
criptografado = "".join([letras[l] if l in letras else l for l in criptografado])

#definindo máximo de carateres digitados
def diminuir(str):
    max = 128 
    if len(criptografado) > max:
        return criptografado[:max]
    else:
        return (criptografado)

stringPequena = diminuir(criptografado)
print ('A mensagem encriptada é: ', stringPequena)

letras2 = {
	"P": "A",
    "Y": "B",
	"F": "C",
    "G": "D",
	"C": "E",
    "R": "F",
	"L": "G",
    "A": "H",
	"O": "I",
    "E": "J",
	"U": "K",
    "I": "L",
	"D": "M",
    "H": "N",
	"T": "O",
    "N": "P",
	"S": "Q",
    "Q": "R",
	"J": "S",
    "K": "T",
	"X": "U",
    "B": "V",
	"M": "W",
    "W": "X",
	"V": "Y",
    "Z": "Z"	
}
#mesmo esquema de codigo para decripitar
descriptografado = input(str("Digite a mensagem a ser decifrada: "))
descriptografado = descriptografado.upper()
descriptografado = "".join([letras2[l2] if l2 in letras2 else l2 for l2 in descriptografado])

print ("A mensagem decifrada é: ", descriptografado)
