import os
from pathlib import Path

invoices_directory = Path(__file__).parent / "invoices"

print()
print(f"Path: {invoices_directory}")
invoice_files = os.listdir(invoices_directory)
for invoice in invoice_files:
    print(f" - {invoice}")
