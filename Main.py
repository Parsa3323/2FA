import time
import pyotp
import qrcode
import DataBaseManager

key = "44XATGPU7I6SPRSHGDC3BDBPRADFP36O"
#key = pyotp.random_base32()
#d
totp = pyotp.TOTP(key)
#
# print(totp.now())
#
# input_val = input("Enter your code: ")
#
# print(totp.verify(input_val))
#
# UIRL = pyotp.totp.TOTP(key).provisioning_uri(name="Tesst", issuer_name="tests")
#
# print(UIRL)

# qrcode.make(UIRL).save("twat.png")

def get_and_check(user:str, code_provided:str):
    """get it"""
    values = totp.verify(code_provided)
    return values

def create_a_key() -> str:
    """Creates and returns a key for a user this has to be saved to a database"""
    return pyotp.random_base32()
def check_from_custom_key(key:str, code_provided:str) -> bool:
    custom_totp = pyotp.TOTP(key)
    valuess = custom_totp.verify(code_provided)
    return valuess