from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import matplotlib.pyplot as plt


def generate_keys(key_size=2048):
    """
    Generates an RSA key pair.

    :param key_size: Length of the RSA key in bits.
    :return: (public_key, private_key)
    """
    private_key = RSA.generate(key_size)
    public_key = private_key.publickey()
    return public_key, private_key


def rsa_encrypt(message: bytes, public_key) -> bytes:
    """
    Encrypts a message using RSA and OAEP padding.

    :param message: Plaintext bytes to encrypt.
    :param public_key: RSA public key for encryption.
    :return: Ciphertext bytes.
    """
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(message)


def rsa_decrypt(ciphertext: bytes, private_key) -> bytes:
    """
    Decrypts an RSA-encrypted message using OAEP padding.

    :param ciphertext: Encrypted bytes to decrypt.
    :param private_key: RSA private key for decryption.
    :return: Decrypted plaintext bytes.
    """
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(ciphertext)


def measure_timing(message: bytes, public_key, private_key) -> tuple:
    """
    Measures encryption and decryption times for a given message.

    :param message: Plaintext bytes.
    :param public_key: RSA public key.
    :param private_key: RSA private key.
    :return: (encryption_time_ms, decryption_time_ms, ciphertext, plaintext)
    """
    start_enc = time.perf_counter()
    ciphertext = rsa_encrypt(message, public_key)
    enc_time = (time.perf_counter() - start_enc) * 1000

    start_dec = time.perf_counter()
    plaintext = rsa_decrypt(ciphertext, private_key)
    dec_time = (time.perf_counter() - start_dec) * 1000

    assert plaintext == message, "Decryption failed: message mismatch"

    return enc_time, dec_time, ciphertext, plaintext


def display_results(message: bytes, timing_data: tuple):
    """
    Prints the results of encryption/decryption timing and messages.

    :param message: Original plaintext bytes.
    :param timing_data: Tuple from measure_timing.
    """
    enc_time, dec_time, ciphertext, plaintext = timing_data

    print(f"Original message:    {message.decode()}")
    print(f"Encrypted message:   {ciphertext}")
    print(f"Decrypted message:   {plaintext.decode()}")
    print(f"Encryption time:     {enc_time:.3f} ms")
    print(f"Decryption time:     {dec_time:.3f} ms")
    print("=" * 80)


def print_summary_table(results):
    """
    Prints an ASCII summary table of timing results.

    :param results: List of tuples (index, length, enc_time, dec_time, success).
    """
    header = ["No.", "Message Length", "Encryption Time (s)", "Decryption Time (s)", "Result"]
    col_widths = [4, 15, 18, 18, 10]
    sep = " | "

    # Print header
    print("-" * (sum(col_widths) + len(sep) * (len(header)-1) + 4))
    print("=== SUMMARY TABLE ===")
    print("-" * (sum(col_widths) + len(sep) * (len(header)-1) + 4))
    print(sep.join(h.ljust(w) for h, w in zip(header, col_widths)))
    print("-" * (sum(col_widths) + len(sep) * (len(header)-1) + 4))

    # Print rows
    for idx, length, enc, dec, res in results:
        row = [str(idx), str(length), f"{enc:.6f}", f"{dec:.6f}", res]
        print(sep.join(r.ljust(w) for r, w in zip(row, col_widths)))

    print("-" * (sum(col_widths) + len(sep) * (len(header)-1) + 4))


def plot_timings(lengths, enc_times, dec_times):
    """
    Plots encryption and decryption times vs. plaintext length.

    :param lengths: List of message lengths in bytes.
    :param enc_times: Corresponding encryption times (s).
    :param dec_times: Corresponding decryption times (s).
    """
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, enc_times, label='Encryption Time', marker='o')
    plt.plot(lengths, dec_times, label='Decryption Time', marker='x')
    plt.xlabel('Plaintext Length (bytes)')
    plt.ylabel('Time (seconds)')
    plt.title('RSA Encryption/Decryption Time vs. Message Length')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Generate key pair
    pub_key, priv_key = generate_keys()

    # Sample messages: display detailed prints
    samples = [b"Hello, I'm Truong", b"My partner is Vu", b"Thank you for reading our essay"]
    for msg in samples:
        timing = measure_timing(msg, pub_key, priv_key)
        display_results(msg, timing)

    # Collect summary for a smaller set
    summary = []
    small_samples = [b"Hi", b"Example!", b"Longer message example."]
    for i, msg in enumerate(small_samples, start=1):
        enc, dec, _, _ = measure_timing(msg, pub_key, priv_key)
        summary.append((i, len(msg), enc/1000, dec/1000, "Success"))

    # Print summary table
    print_summary_table(summary)

    # Measure for varying lengths and plot
    lengths = list(range(10, 201, 10))
    enc_times, dec_times = [], []
    for length in lengths:
        msg = b'a' * length
        enc, dec, _, _ = measure_timing(msg, pub_key, priv_key)
        enc_times.append(enc/1000)
        dec_times.append(dec/1000)

    plot_timings(lengths, enc_times, dec_times)
