import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "index.html"

def customize():
    print("=" * 60)
    print("      ☕ CLIENT WEBSITE INSTANT CUSTOMIZER TOOL")
    print("=" * 60)
    print("Easily update your cafe website for any new client in seconds.\n")

    if not HTML_FILE.exists():
        print(f"Error: Could not find {HTML_FILE}")
        return

    with open(HTML_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Gather client details
    cafe_name = input("1. Enter Client's Cafe/Bakery Name [e.g. The Roastery House]: ").strip()
    tagline = input("2. Enter Short Tagline [e.g. Artisan Coffee & Fresh Bakes]: ").strip()
    phone = input("3. Enter Client's WhatsApp Number with country code [e.g. 919876543210]: ").strip()
    address = input("4. Enter Full Address [e.g. 14 Linking Road, Bandra West, Mumbai]: ").strip()
    rating = input("5. Enter Google Rating [e.g. 4.9 ★ (380+ Reviews)]: ").strip()

    # Perform intelligent replacements
    if cafe_name:
        content = re.sub(r"Velvet & Roast", cafe_name, content)
        print(f"  ✓ Updated Cafe Name to: {cafe_name}")

    if tagline:
        content = re.sub(r"Artisan Bakehouse", tagline, content)
        print(f"  ✓ Updated Tagline to: {tagline}")

    if phone:
        # Remove any spaces, dashes, or + signs from phone number for wa.me format
        clean_phone = re.sub(r"[^\d]", "", phone)
        content = re.sub(r"919876543210", clean_phone, content)
        print(f"  ✓ Updated WhatsApp links to: {clean_phone}")

    if address:
        content = re.sub(r"42 Artisan Lane, Arts & Heritage District", address, content)
        print(f"  ✓ Updated Address to: {address}")

    if rating:
        content = re.sub(r"4\.9 ★ on Google \(420\+ Reviews\)", rating, content)
        content = re.sub(r"4\.9 on Google \(420\+ Reviews\)", rating, content)
        print(f"  ✓ Updated Google Rating to: {rating}")

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print("\n" + "=" * 60)
    print("🎉 SUCCESS: index.html has been updated with client's details!")
    print("=" * 60)
    print("Double-click view_site.bat to preview your changes immediately.")

if __name__ == "__main__":
    customize()
