import qrcode
import os


def generate_qr(data, filename="qrcode.png"):
    # Ensure the 'qr_codes' directory exists
    os.makedirs("qr_codes", exist_ok=True)

    # Save the QR code inside the 'qr_codes' folder
    filepath = os.path.join("qr_codes", filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filepath)
    print(f"QR Code saved as {filepath}")


def main():
    print("QR Code Generator")
    while True:
        data = input("Enter text or URL (or type 'exit' to quit): ").strip()
        if data.lower() == "exit":
            print("Goodbye!")
            break
        filename = input("Enter filename to save as (default: qrcode.png): ").strip() or "qrcode.png"

        # Ensure filename has a .png extension
        if not filename.endswith(".png"):
            filename += ".png"

        generate_qr(data, filename)


if __name__ == "__main__":
    main()
