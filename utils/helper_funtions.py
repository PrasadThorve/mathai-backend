import random

#function to generate otp
def generate_otp():
    """Generate a 6-digit OTP"""
    return str(random.randint(100000, 999999))