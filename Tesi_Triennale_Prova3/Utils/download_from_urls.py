import urllib.request

#2)Funzione per rinominare gli URL e restituire la lista dei siti
def rename_urls(site_list):
    s_raw = []
    for id, s in enumerate(site_list):
        a = s.split('.com')[0] + 'usercontent.com'
        b = s.split('.com')[1]
        c = 'http://raw.' + a.split('//')[1] + b + '/master/README.md'
        s_raw.append(c)
    return s_raw

#3)Funzione per scaricare i file Markdown
def download_md_file(link_list, path_md_file):
    i = 0
    for link in link_list:
        try:
            urllib.request.urlretrieve(link, path_md_file + str(i) + ".md")
            i += 1
        except:
            pass
    return i

