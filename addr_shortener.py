# Shorten a full EVM address for clean UI display
def shorten_address(address):
    if len(address) < 10:
        return address
    # Keep first 6 characters and last 4 characters
    return f"{address[:6]}...{address[-4:]}"

full_addr = "0x71C7656EC7ab88b098defB751B7401B5f6d1476B"
print(f"Display Version: {shorten_address(full_addr)}")
