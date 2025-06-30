import os
import hashlib

def calculate_sha512(file_path):
    """Calculate the SHA-512 hash of a file."""
    sha512_hash = hashlib.sha512()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha512_hash.update(byte_block)
    return sha512_hash.hexdigest()

def get_sha512sums(directory):
    """Get SHA-512 hashes of all files in a directory."""
    sha512sums = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            sha512sums[file_path] = calculate_sha512(file_path)
    return sha512sums

def save_sha512sums_to_file(sha512sums, output_file):
    """Save SHA-512 hashes to a text file."""
    with open(output_file, "w") as f:
        for file_path, sha512sum in sha512sums.items():
            f.write(f"{file_path}: {sha512sum}\n")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    output_file_path = input("Enter the output file path (e.g., hashes.txt): ")

    sha512sums = get_sha512sums(directory_path)
    save_sha512sums_to_file(sha512sums, output_file_path)

    print(f"SHA-512 hashes have been saved to {output_file_path}")
