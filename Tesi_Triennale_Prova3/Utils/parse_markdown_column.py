import re

from markdown_it import MarkdownIt

"""
Inizializza una tabella di dati per i file Markdown.

Args:
    num_file_md (int): Numero di file Markdown da elaborare.
    link_list (list): Lista di link associati ai file Markdown.

Returns:
    list: Una lista di dizionari, ciascuno contenente dati iniziali per un file Markdown.
"""
def initialize_data_table(num_file_md, link_list):
    data_table = []
    for i in range(num_file_md):
        file_data = {
            "file_name": f"{i}.md",
            "h1_titles": [],
            "char_counts": [],
            "no_h1_titles": [],
            "link": link_list[i]
        }
        data_table.append(file_data)
    return data_table

    """
    Estrae i titoli H1 e H2/H3... da un file Markdown.

    Args:
        md_file (str): Il percorso del file Markdown da analizzare.

    Returns:
        tuple: Due liste contenenti i titoli H1 e H2/H3..., e il testo del file Markdown.
    """
def find_titles_md(md_file):
    try:
        with open(md_file, 'r', encoding='utf-8') as file:
            md_text = file.read()
    except UnicodeDecodeError:
        md_text = ""

    md = MarkdownIt()
    tokens = md.parse(md_text)

    h1_titles = []
    h2_3_titles = []
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            level = int(token.tag[1:])
            if level == 1:
                h1_titles.append((tokens[i + 1].content, level))
            else:
                h2_3_titles.append((tokens[i + 1].content, level))

    return h1_titles, h2_3_titles, md_text

    """
    Calcola la lunghezza di una sezione di testo in un file Markdown.

    Args:
        md_text (str): Il testo del file Markdown.
        h1_title (str): Il titolo H1 della sezione.
        next_h1_title (str): Il titolo H1 della sezione successiva.

    Returns:
        int: La lunghezza del testo della sezione, contando solo lettere, numeri e vocali.
    """
def calculate_section_length(md_text, h1_title, next_h1_title):
    section_start = md_text.find(h1_title) + len(h1_title)
    section_end = md_text.find("# " + next_h1_title) if next_h1_title else len(md_text)

    # Estrai il testo della sezione
    section_text = md_text[section_start:section_end].strip()

    # Rimuovi tutto tranne vocali, consonanti e numeri
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', section_text)  # Mantiene solo lettere e numeri
    return len(cleaned_text)

    """
    Estrae i titoli e le informazioni sulle sezioni da file Markdown e aggiorna la data_table.

    Args:
        data_table (list): La tabella di dati da aggiornare.
        path_md_file (str): Il percorso della cartella contenente i file Markdown.

    Returns:
        list: La tabella di dati aggiornata con titoli e conteggi caratteri.
    """
def extract_sections(data_table, path_md_file):
    for file_data in data_table:
        h1_titles, h2_3_titles, md_text = find_titles_md(path_md_file + file_data["file_name"])
        # Popola h1_titles e calcola char_counts
        for i, (title, _) in enumerate(h1_titles):
            file_data["h1_titles"].append(title)
            next_h1_title = h1_titles[i+1][0] if i+1 < len(h1_titles) else None
            next_h2_title = h2_3_titles[i][0] if i < len(h2_3_titles) else None
            char_count = calculate_section_length(md_text, title, next_h1_title)
            file_data["char_counts"].append(char_count)

        # Popola la colonna no_h1_titles
        file_data["no_h1_titles"] = [title[0] for title in h2_3_titles]

    return data_table

    """
    Recupera e inizializza la tabella di dati da file Markdown.

    Args:
        num_file_md (int): Numero di file Markdown da elaborare.
        link_list (list): Lista di link associati ai file Markdown.
        path_md_file (str): Il percorso della cartella contenente i file Markdown.

    Returns:
        list: La tabella di dati con titoli e conteggi caratteri estratti.
    """
def get_data_table(num_file_md, link_list,path_md_file):
    data_table=initialize_data_table(num_file_md,link_list)
    a=extract_sections(data_table, path_md_file)
    return a


