import hashlib

def check_flag(user_input):
    target = "3d4f2bf07dc1be38b20cd6e46949a1071f9d0e3d"  # sha1 of the real flag
    if hashlib.sha1(user_input.encode()).hexdigest() == target:
        print("✅ Correct! Flag validated.")
        return True
    print("❌ Incorrect.")
    return False

# Try to figure out the flag through logic, brute force, or pattern recognition
# check_flag("your_guess_here")
