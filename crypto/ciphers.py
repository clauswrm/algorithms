""" Collection of basic cryptographic ciphers """
__author__ = 'Claus Martinsen'

from random import randint, choice
from math import gcd
import Cryptography.crypto_utils as crypto


class Cipher:
    # All legal characters
    alphabet = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
                '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
                '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

    alphabetLength = len(alphabet)

    def encode(self, text, key):
        return text

    def decode(self, encodedText, key):
        return encodedText

    def verify(self, text, key):
        return text == self.decode(self.encode(text, key[0]), key[1])

    def generateKeys(self):
        pass


class Caesar(Cipher):
    def encode(self, text, key):
        encodedText = []
        for c in text:
            encodedText.append(chr((ord(c) + key - 32) % self.alphabetLength + 32))
        return ''.join(encodedText)

    def decode(self, encodedText, key):
        decodedText = []
        for c in encodedText:
            decodedText.append(chr((ord(c) - key - 32) % self.alphabetLength + 32))
        return ''.join(decodedText)

    def generateKeys(self):
        return tuple([randint(1, self.alphabetLength)] * 2)  # Må returnere to av samme nøkkel (til sender og mottaker)


class Multiplicative(Cipher):
    def encode(self, text, key):
        encodedText = []
        for c in text:
            encodedText.append(chr(((ord(c) - 32) * key) % self.alphabetLength + 32))
        return ''.join(encodedText)

    def decode(self, encodedText, key):
        decodedText = []
        for c in encodedText:
            decodedText.append(chr(((ord(c) - 32) * key) % self.alphabetLength + 32))
        return ''.join(decodedText)

    def generateKeys(self):
        _key1, _key2 = 0, 0
        while gcd(_key1 * _key2, self.alphabetLength) != 1:
            _key1 = randint(2, self.alphabetLength)
            _key2 = crypto.modular_inverse(_key1, self.alphabetLength)
        return _key1, _key2


class Affine(Cipher):
    def __init__(self):
        self.caesar = Caesar()
        self.multi = Multiplicative()

    def encode(self, text, key):
        return self.caesar.encode(self.multi.encode(text, key[0]), key[1])

    def decode(self, encodedText, key):
        return self.multi.decode(self.caesar.decode(encodedText, key[1]), key[0])

    def generateKeys(self):
        mk = self.multi.generateKeys()
        ck = self.caesar.generateKeys()
        return (mk[0], ck[0]), (mk[1], ck[1])


class Unbreakable(Cipher):
    def encode(self, text, key):
        encodedText = []
        for i in range(len(text)):
            encodedText.append(chr((ord(text[i]) + ord(key[i % len(key)]) - 32) % self.alphabetLength + 32))
        return ''.join(encodedText)

    def decode(self, encodedText, key):
        decodedText = []
        for i in range(len(encodedText)):
            decodedText.append(chr((ord(encodedText[i]) - ord(key[i % len(key)]) - 32) % self.alphabetLength + 32))
        return ''.join(decodedText)

    def generateKeys(self):
        with open('english_words.txt', 'r') as f:
            _keyWord = choice(list(f)).rstrip()
        return _keyWord, _keyWord  # Må returnere to av samme nøkkel (til sender og mottaker)


class RSA(Cipher):
    def __init__(self, bits):
        self._bits = bits
        self._publicKey = None

    def encode(self, text, key):
        blocks = crypto.blocks_from_text(text, self._bits // 8)
        for i in range(len(blocks)):
            blocks[i] = pow(blocks[i], key[1], key[0])
        return blocks

    def decode(self, encodedBlocks, key):
        encodedBlocks = encodedBlocks.copy()  # For å ikke endre på orginalteksten
        for i in range(len(encodedBlocks)):
            encodedBlocks[i] = pow(encodedBlocks[i], key[1], key[0])
        return crypto.text_from_blocks(encodedBlocks, self._bits)

    def generateKeys(self):
        _p, _q = 0, 0
        while _p == _q:
            _p = crypto.generate_random_prime(self._bits)
            _q = crypto.generate_random_prime(self._bits)
        _n = _p * _q
        _phi = (_p - 1) * (_q - 1)
        _e = randint(3, _phi - 1)
        _d = crypto.modular_inverse(_e, _phi)
        while gcd(_e * _d, _phi) != 1:
            _e = randint(3, _phi - 1)
            _d = crypto.modular_inverse(_e, _phi)
        self._publicKey = (_n, _e)
        return (_n, _e), (_n, _d)  # Public key: (n,e), private key (n,d)

    def getPublicKey(self):
        return self._publicKey
