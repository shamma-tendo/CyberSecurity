import random

def generate_dh_params():
    # In production, use standardized large primes (RFC 3526) — this is simplified for learning
    p = 23  # small prime for demo (real DH uses 2048+ bit primes)
    g = 5   # generator
    return p, g

def dh_key_exchange():
    p, g = generate_dh_params()

    # Alice's side
    alice_private = random.randint(1, p - 1)
    alice_public = pow(g, alice_private, p)

    # Bob's side
    bob_private = random.randint(1, p - 1)
    bob_public = pow(g, bob_private, p)

    # Exchange public values, compute shared secret independently
    alice_shared = pow(bob_public, alice_private, p)
    bob_shared = pow(alice_public, bob_private, p)

    print(f"Alice's shared secret: {alice_shared}")
    print(f"Bob's shared secret:   {bob_shared}")
    print(f"Match: {alice_shared == bob_shared}")

dh_key_exchange()