# Author: Douglas Mejia
# CypherMaker
# 
# produces encyrpted files using simple ciphers

import sys
import click
import os  


def caeserCypher(key, file,output):
	''' 
		Classic Caeser Cipher Encryption 
			Referenced from: 
				Manual of Cryptography 1911: 28-29
				A substitution cypher that shirts characters around by a certain number
				along the ASCII table
	'''
	readingFrom = open(file,'r')
	message = readingFrom.read()
	readingFrom.close()
	writingTo = open(output,'w')
	for letter in message:
		if letter  == "\n":
			writingTo.write(letter)
		else:
			writingTo.write(chr( (ord(letter) +key) % 256 ))
	writingTo.close()
	return;


def decryptCaeser(key, encyrptedFile,output):
	''' 
		Classic Caeser Cipher Encryption 
			Referenced from: 
				Manual of Cryptography 1911: 28-29
				A decrypts messages by rotating each characters by a certain key value 
				along the ASCII table
	'''
	readingFrom = open(encyrptedFile,'r')
	message = readingFrom.read()
	readingFrom.close()
	writingTo = open(output,'w')
	for letter in message:
		if letter  == "\n":
			writingTo.write(letter)
		else:
			writingTo.write(chr( (ord(letter) - key) % 256))
	writingTo.close()
	return;


toLeet = { "a": "4", "e":"3", "i": "1", "o": "0", "v":"u", "s":"5", "t":"7", "n":"^","l":"|", "d": ")",
		   "h": "#", "r":"2" } 

fromLeet = { "4": "a", "3":"e" ,"1":"i",  "0":"o", "u":"v", "5":"s", "7": "t", "^":"n" , "|":"l" ,  ")":"d",
		   "#" : "h" , "2" : "r" }

def toLeetSpeak(file, output):
	""" substitution cipher: LeetSpeak
		Reads in given file and substitutes certain letters into leet speak.
		The letter to be changed are detailed in dictionaries defined below.

		toLeet = { "a": "4", "e":"3", "i": "1", "o": "0", "v":"u", "s":"5", "t":"7", "n":"^","l":"|", "d": ")",
				   "h": "#", "r":"2" } 

		fromLeet = { "4": "a", "3":"e" ,"1":"i",  "0":"o", "u":"v", "5":"s", "7": "t", "^":"n" , "|":"l" ,  ")":"d",
				   "#" : "h" , "2" : "r" }
		
		referenced from: 
				Link: Gamehouse.com/blog/leet-speak-cheat-sheet/ 
	"""
	readingFrom = open(file,'r')
	message = readingFrom.read()
	readingFrom.close()
	writingTo = open(output,'w')
	for letter in message:
		if toLeet.has_key(letter):
			writingTo.write(toLeet[letter])
		else:
			writingTo.write(letter)
	writingTo.close()
	return; 

def fromLeetSpeak(file, output):
	""" substitution cipher: LeetSpeak
		Reads in given file and substitutes certain letters from leet speak.
		The letter to be changed are detailed in dictionaries defined below.

		toLeet = { "a": "4", "e":"3", "i": "1", "o": "0", "v":"u", "s":"5", "t":"7", "n":"^","l":"|", "d": ")",
				   "h": "#", "r":"2" } 

		fromLeet = { "4": "a", "3":"e" ,"1":"i",  "0":"o", "u":"v", "5":"s", "7": "t", "^":"n" , "|":"l" ,  ")":"d",
				   "#" : "h" , "2" : "r" }
		
		referenced from: 
				Link: Gamehouse.com/blog/leet-speak-cheat-sheet/ 
	"""
	readingFrom = open(file,'r') 
	message = readingFrom.read()
	readingFrom.close()
	writingTo = open(output,'w')
	for letter in message:
		if fromLeet.has_key(letter):
			writingTo.write(fromLeet[letter])
		else:
			writingTo.write(letter)
	writingTo.close()
	return;


"""Polyalphabetic Cipher key: dream
	The key wraps around the the messages and cross references the each letter against the 
	a different alphabet
	referenced from:
		Elements  of Cyptanalysis pg 34 - 40
			class notes
				wikipedia link: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
polykey = { "d" :  "asdfghjklzxcvbnmqwertyuiop",
			"r" :  "lkjhgfdsamnbvcxzpoiuytrewq",
			"e" :  "qwertyuiopzxcvbnmasdfghjkl",
			"a" :  "zaqwsxcderfvbgtyhnmjuiklop",
			"m" :  "fvredcwsxqaztgbnhyujmkilpo"
			}

def poly(key,file, output):
	"""Polyalphabetic Cipher key: dream
		The key wraps around the the messages and cross references the each letter against the 
		a different alphabet
		referenced from:
			Elements  of Cyptanalysis pg 34 - 40
				class notes
					wikipedia link: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
	"""
	readingFrom = open(file,'r')
	message = readingFrom.read()
	readingFrom.close()
	keyIndex = 0
	writingTo = open(output,'w')
	for letter in message:
		if letter.isspace():
			writingTo.write(" ")
		elif alphabet.find(letter) == -1:
			writingTo.write(letter)
 		else:
			#convert letter to lowercase for simplicity
			letterholder = letter.lower()
			#to cross reference reg alphabet with cipher alphabets; index of letter in reg alphabet
			indexOfLetter = alphabet.find(letterholder)
			#to iterate over key (dream) and decide which alphabet to use
			keyValue  = key[keyIndex] 
			letterToAdd = polykey[keyValue][indexOfLetter]
			writingTo.write(letterToAdd)
			keyIndex = keyIndex +1
			if(keyIndex > len(key)-1):
				keyIndex = 0

	writingTo.close()
	return;

def fromPoly(key, file, output):
	"""Polyalphabetic Cipher key: dream
		The key wraps around the the messages and cross references the each letter against the 
		a different alphabet
		referenced from:
			Elements  of Cyptanalysis pg 34 - 40
				class notes
					wikipedia link: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
	"""

	readingFrom = open(file,'r')
	message = readingFrom.read()
	readingFrom.close()
	keyIndex = 0
	writingTo = open(output,'w')
	for letter in message:
		if letter.isspace():
			writingTo.write(" ")
		elif alphabet.find(letter) == -1:
			writingTo.write(letter)
 		else:
			#find the index of the letter in appropriate alphabet
			keyValue  = key[keyIndex]
			#to cross reference reg alphabet with cipher alphabets; index of letter in cipher alphabet
			indexOfLetter = polykey[keyValue].find(letter)
			letterToAdd = alphabet[indexOfLetter]
			writingTo.write(letterToAdd)
			keyIndex = keyIndex +1
			if(keyIndex > len(key)-1):
				keyIndex = 0
	writingTo.close()
	return;


def transpositionCipher(file, output):
	''' Transpositon cipher:
			refrenced from: 
				Manual of Crytography 49 - 55
				https://www.youtube.com/watch?v=0um-_4SvPg0
	'''
	readingFrom = open(file,'r')
	message = readingFrom.read()
	readingFrom.close()
	shiftedMessage= ""
	for i in range( 0, len(message)):
		shiftAmount = (len(message)-i ) % len(message)-1
		shiftedMessage = shiftedMessage +  message[shiftAmount]
	writeTo = open(output,'w')
	writeTo.write(shiftedMessage)
	writeTo.close()
	return; 

def decrypt_transposition(file,output):

	''' Transpositon cipher:
			refrenced from: 
				Manual of Crytography 49 - 55
				https://www.youtube.com/watch?v=0um-_4SvPg0
	'''
	readingFrom = open(file,'r')
	message = readingFrom.read()
	readingFrom.close()
	shiftedMessage= ""
	writeTo = open(output,'w')
	for i in range(len(message),0,-1):
		shiftAmount = (i+len(message)) % len(message)-1
		shiftedMessage =   message[shiftAmount]
		writeTo.write(shiftedMessage)
	writeTo.close()
	return; 


def find_Frequecy(file):
	''' 
		Function that prints the Frequency of the message's
		letter, bigrams, and trigrams
	'''

	Frequecy ={}
	readingFrom = open(file,'r')
	message = readingFrom.read()
	readingFrom.close()
	shiftedMessage= ""

	for i, letter in enumerate(message):
		#check to see if the single letter exist
		if " " in letter or "" in letter or  '\n' in letter or '\n' in letter:
			pass
		elif letter in Frequecy:
			Frequecy[letter] = Frequecy[letter] + 1
		else:
			Frequecy.update({letter:1})

		bigramIndex = i+1
		if(bigramIndex > len(message)):
			continue

		bigram = message[i:bigramIndex+1]
		if " " in bigram or '\n' in bigram or " " and '\n' in bigram:
			pass
		elif  bigram in Frequecy:
			Frequecy[bigram] = Frequecy[bigram] + 1
		else:
			Frequecy.update({bigram:1})
		
		trigramIndex = i+2
		if(trigramIndex >len(message)):
			continue

		trigram = message[i:trigramIndex+1]
		if " " in trigram or '\n' in trigram or " " and '\n' in trigram:
			pass
		elif  trigram in Frequecy:
			Frequecy[trigram] = Frequecy[trigram] + 1
		else:
			Frequecy.update({trigram:1})

		#combinations
	for key in sorted(Frequecy.iterkeys()):
		print "{%s : %s}" % (key, Frequecy[key])
	return;

@click.group()


@click.option("--cypher", help = "produces an encrypted file from given text file ")
def cli(cypher):
	"""
		Action:
			encrypt
				to encrypt a given file using a certain encryption algorithm (see Type of Encryption)

			decrypt
				to encrypt a given file using a certain encryption algorithm (see Type of Encryption)
		Type of Encryption:
			c for caeserCipher\n
		 	l for leetSpeak\n
			p for polyalphabetic\n	
		 	t for transpositon

		Input file

		Outputfile
	"""
	pass

@cli.command()
@click.argument('type_of_encryption', type = click.STRING)
@click.argument('input_file', type = click.STRING)
@click.argument('output', type = click.STRING)
def encrypt(type_of_encryption,input_file,output):
	print(type_of_encryption)
	if ( type_of_encryption not in ["c","l","p","t"]):
		print("invalid input:  see --help")
	elif os.path.isfile(input_file)  == False:
		print("cant find that file")
	else:
		if( type_of_encryption == "c"):
			print("c")
			caeserCypher(2, input_file,output)
		elif(type_of_encryption == "l"):
			toLeetSpeak(input_file,output)
		elif type_of_encryption == "p":
			poly("dream", input_file,output)
		elif( type_of_encryption == "t"):
			print("transpo")
			transpositionCipher(input_file,output)

@cli.command()
@click.argument('type_of_decryption', type = click.STRING)
@click.argument('file_to_decrypt', type = click.STRING)
@click.argument('output', type = click.STRING)

def decrypt(type_of_decryption,file_to_decrypt,output):
	if ( type_of_decryption not in ["c","l","p","t"]):
		print("invalid input:  see --help")
	elif os.path.isfile(file_to_decrypt)  == False:
		print("cant find that file")
	else:
		if(type_of_decryption == "c"):
			print("about to call decryptCaeser")
			decryptCaeser(2, file_to_decrypt,output)
		elif(type_of_decryption == "l"):
			fromLeetSpeak(file_to_decrypt,output)
		elif( type_of_decryption == "p"):
			fromPoly("dream", file_to_decrypt,output)
		elif( type_of_decryption == "t"):
			print("transpo")
			decrypt_transposition(file_to_decrypt,output)

@cli.command()
@click.argument('file_to_freq', type = click.STRING)
def Freq(file_to_freq):
	if os.path.isfile(file_to_freq)  == False:
		print("cant find that file")
	else:
		find_Frequecy(file_to_freq)


if __name__ == '__main__':
    cli()


	

