def search_keyword_in_file(filename, keyword):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            return keyword.lower() in content
    except FileNotFoundError:
        print(f"❗ A fájl nem található: {filename}")
        return False

if __name__ == "__main__":
    filename = "video_Keyword.txt"
    search_term = input("🔎 Add meg a keresett szót: ").strip()

    if not search_term:
        print("❗ Nem adtál meg szót!")
    else:
        found = search_keyword_in_file(filename, search_term)
        if found:
            print(f"✅ A(z) '{search_term}' szó szerepel a '{filename}' fájlban.")
        else:
            print(f"❌ A(z) '{search_term}' szó NEM szerepel a '{filename}' fájlban.")

    input("Nyomj egy Entert a kilépéshez...")
