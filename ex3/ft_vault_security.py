def secure_archive(
        filename: str, action: str = 'read', content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == 'read':
            with open(filename, 'r') as f:
                data: str = f.read()
            return (True, data)
        elif action == 'write':
            with open(filename, 'w') as f:
                f.write(content)
            return (True, 'Content successfully written to file')
        else:
            return (False, "Invalid action specified.")
    except Exception as e:
        return (False, str(e))

# Example usage for your own testing (not required for submission):
# if __name__ == "__main__":
#     print("=== Cyber Archives Security ===")
#     # Test 1: File doesn't exist
#     print("Using 'secure_archive' to read from a nonexistent file:")
#     print(secure_archive('/not/existing/file', 'read'))
#     # Test 2: Permission denied (Linux/Mac specific)
#     print("Using 'secure_archive' to read from an inaccessible file:")
#     print(secure_archive('/etc/master.passwd', 'read'))
#     # Test 3: Successful Write
#     print("Using 'secure_archive' to write previous content to a new file:")
#     print(secure_archive('test_vault.txt', 'write',
#  'This is highly classified data.\n')
#     # Test 4: Successful Read
#     print("Using 'secure_archive' to read from a regular file:")
#     print(secure_archive('test_vault.txt', 'read')).
