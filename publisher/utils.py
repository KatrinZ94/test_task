import zlib


def compress_message(text):
    compressed_text = zlib.compress(text.encode())
    return compressed_text


def decompress_body(body):
    decompressed_body = zlib.decompress(body).decode()
    return decompressed_body
