import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Use regular expression to split the string into email addresses
        # The pattern matches email addresses and separates them by spaces or commas
        pattern = r'\s|,\s*'
        addresses = re.split(pattern, self.email_addresses)

        # Use a set to get unique addresses
        unique_addresses = set()

        # Filter out non-email strings and add valid emails to the set
        for address in addresses:
            if re.match(r"[^@]+@[^@]+\.[^@]+", address):
                unique_addresses.add(address)

        # Sort the addresses alphabetically
        sorted_addresses = sorted(unique_addresses)

        return sorted_addresses
