from cryptographyFramework import *

initializeWrite()
user = "Mateus"
password = "8765"
encryptedText = encryptMessage(user, password, "Aqui há um segredo")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Aqui é outro segredo")
saveNewLine(encryptedText)

