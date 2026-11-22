import os
from pathlib import Path

invoices_directory = Path(__file__).parent / "invoices"


def extract_month(filename: str) -> str | None:
    parts = filename.split(".")[0].split("_")
    if len(parts) < 3 or ".pdf" not in filename:
        print(f"Error: '{filename}' doesn't match First_Last_Month.pdf")
        return None
    return parts[-1].lower()


def make_directory(new_directory: Path) -> None:
    if not new_directory.is_dir():
        os.mkdir(new_directory)


def main() -> None:
    print(f"{' Python Invoice Program ':~^60}")
    invoice_files = os.listdir(invoices_directory)
    does_month_have_directory: list = []

    for invoice in invoice_files:
        month = extract_month(invoice)
        if month is not None:
            if month not in does_month_have_directory:
                make_directory(invoices_directory / month)
                does_month_have_directory.append(month)
            os.rename(invoices_directory / invoice, invoices_directory / month / invoice)
        else:
            continue


if __name__ == "__main__":
    main()
