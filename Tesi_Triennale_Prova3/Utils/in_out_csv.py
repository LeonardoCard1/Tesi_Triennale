import csv

"""
Legge un file CSV e restituisce una lista di URL.

Args:
    path (str): Il percorso del file CSV da leggere.

Returns:
    list: Una lista di URL che iniziano con 'http'.
"""
def read_urls(path):
    site_list = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for raw in csv_reader:
            if raw[1].startswith('http'):
                site_list.append(raw[1])
    return site_list

    """
    Scrive i dati in un file CSV.

    Args:
        data_table (list): Una lista di dizionari contenenti dati da scrivere.
        name_file_csv_out (str): Il nome del file CSV di output.
    """
def get_csv_tab(data_table, name_file_csv_out):
    with open(name_file_csv_out, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            "File_name",
            "H1_titles",
            "Char_counts",
            "Non_h1_titles",
            "Repository_link"
        ])

        for file_data in data_table:
            for i, title in enumerate(file_data["h1_titles"]):
                writer.writerow([
                    file_data["file_name"],
                    title,
                    file_data["char_counts"][i],
                    file_data["no_h1_titles"],
                    file_data["link"]
                ])