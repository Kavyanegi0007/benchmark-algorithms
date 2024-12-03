import time
import gzip
import snappy
import zstandard as zstd
import os

# Create a sample data payload
data = b"This is some sample data to compress." * 100000

# Benchmarking function
def benchmark_compression(name, compress_func, decompress_func):
    print(f"\n--- {name} ---")

    # Measure compression time
    start = time.time()
    compressed_data = compress_func(data)
    compression_time = time.time() - start
    print(f"Compression Time: {compression_time:.6f} seconds")

    # Measure decompression time
    start = time.time()
    decompressed_data = decompress_func(compressed_data)
    decompression_time = time.time() - start
    print(f"Decompression Time: {decompression_time:.6f} seconds")

    # Check correctness
    if data == decompressed_data:
        print("Decompression verified successfully.")
    else:
        print("Decompression failed!")

    # Measure compression ratio
    compression_ratio = len(compressed_data) / len(data)
    print(f"Compression Ratio: {compression_ratio:.6f}")

# Define compression and decompression functions
def gzip_compress(data):
    return gzip.compress(data)

def gzip_decompress(compressed_data):
    return gzip.decompress(compressed_data)

def snappy_compress(data):
    return snappy.compress(data)

def snappy_decompress(compressed_data):
    return snappy.decompress(compressed_data)

def zstd_compress(data):
    compressor = zstd.ZstdCompressor()
    return compressor.compress(data)

def zstd_decompress(compressed_data):
    decompressor = zstd.ZstdDecompressor()
    return decompressor.decompress(compressed_data)

# Benchmark each algorithm
benchmark_compression("Gzip", gzip_compress, gzip_decompress)
benchmark_compression("Snappy", snappy_compress, snappy_decompress)
benchmark_compression("Zstd", zstd_compress, zstd_decompress)

