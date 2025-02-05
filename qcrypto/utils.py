import matplotlib.pyplot as plt

def encrypt_decrypt(message, key):
    message_bits = [int(bit) for char in message for bit in format(ord(char), '08b')]
    encrypted_bits = [m ^ k for m, k in zip(message_bits, key * (len(message_bits)//len(key) + 1))]
    encrypted_text = ''.join([chr(int(''.join(map(str, encrypted_bits[i:i+8])), 2)) for i in range(0, len(encrypted_bits), 8)])
    return encrypted_text

def plot_error_rate(alice_key, bob_key):
    mismatch = sum(a != b for a, b in zip(alice_key, bob_key))
    plt.bar(['uncoordinated', 'coordinated'], [len(alice_key) - mismatch, mismatch], color=['green', 'red'])
    plt.title('The effect of eavesdropping on the final key')
    plt.show()
