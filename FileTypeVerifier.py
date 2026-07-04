FILE_SIGNATURES = {
    b'\xFF\xD8\xFF': 'JPEG',
    b'\x89PNG\r\n\x1a\n': 'PNG',
    b'%PDF': 'PDF',
    b'PK\x03\x04': 'ZIP/DOCX/XLSX',
    b'MZ': 'EXE/DLL',
}

def identify_file_type(filepath):
    with open(filepath, 'rb') as f:
        header = f.read(8)

    for signature, filetype in FILE_SIGNATURES.items():
        if header.startswith(signature):
            return filetype
    return "Unknown"

# result = identify_file_type("suspicious_file.jpg")
# print(f"Actual file type: {result}")