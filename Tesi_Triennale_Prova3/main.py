import Utils.in_out_csv as ioc, Utils.download_from_urls as dfu, Utils.parse_markdown_column as pmc

name_file_csv_in = "./in/mini_apps.csv"
name_file_csv_out = "./out/output_sections.csv"
path_md_file = "./md_file/"

readed_csv=ioc.read_urls(name_file_csv_in)
print(readed_csv)

link_list= dfu.rename_urls(readed_csv)
print(link_list)

num_file_downloaded=dfu.download_md_file(link_list,path_md_file)
print(f'scaricato {num_file_downloaded} file nella cartella {path_md_file}')

#la tabella viene creata nel file parse_markdown_column.py
#initialize
a=pmc.get_data_table(num_file_downloaded,link_list,path_md_file)
print (a)

ioc.get_csv_tab(a, name_file_csv_out)



