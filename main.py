import os


def cari_file(direktori, nama_file, ekstensi):
    found_files = []

    for root, dirs, files in os.walk(direktori):
        for file in files:
            file_lower = file.lower()
            query_lower = nama_file.lower()
            query_parts = query_lower.split()
            match = all(part in file_lower for part in query_parts)
            if match and file_lower.endswith(ekstensi.lower()):
                found_files.append(os.path.join(root, file))

    return found_files


def main():
    while True:
        input("contoh : D:/diretory/directory -- (klik enter)")
        direktori = input("Masukkan direktori tempat pencarian file: ")
        nama_file = input("Masukkan nama file yang ingin dicari(opsional): ")
        ekstensi = input("Masukkan ekstensi file (e.g., pdf, docx, txt): ")

        hasil = cari_file(direktori, nama_file, ekstensi)
        if len(hasil) > 0:
            print("File yang mungkin anda ingin buka:")
            for index, file_path in enumerate(hasil, start=1):
                print(f"{index}. {file_path}")

            file_choice = input("Masukkan nama file yang ingin dibuka (masukkan nomor): ")
            try:
                file_choice = int(file_choice)
                if 1 <= file_choice <= len(hasil):
                    selected_file = hasil[file_choice - 1]
                    try:
                        os.startfile(selected_file)  # Membuka file dengan aplikasi default terkait
                    except OSError as e:
                        print("Gagal membuka file:", e)
                else:
                    print("Nomor file tidak valid.")
            except ValueError:
                print("Masukkan nomor file yang valid.")
        else:
            print("File tidak ditemukan.")

        lanjut = input("Ingin mencari file lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break


if __name__ == "__main__":
    main()
