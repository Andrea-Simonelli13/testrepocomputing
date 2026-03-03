#import sys
import argparse
import time
import string
import matplotlib.pyplot as plt

def letters(file_path__, start_marker=None, end_marker=None):
    with open(file_path__, "r", encoding="utf-8") as file:
        contenuto = file.read().lower()
        contenuto = estrai_contenuto_custom(
            contenuto,
            start_marker=start_marker,
            end_marker=end_marker
        )
        #dizionario_alfabeto = {chr(i): 0 for i in range(65, 91)}  # A-Z
        #dizionario_alfabeto.update({chr(i): 0 for i in range(97, 123)})  # a-z
        dizionario_alfabeto = {chr(i): 0 for i in range(97, 123)} # a-z
        for lettera in contenuto:
            if lettera in dizionario_alfabeto:
                dizionario_alfabeto[lettera] += 1

        return dizionario_alfabeto

#def stampa_help():
 #   print("""
#Utilizzo: py letters.py <percorso_file.txt> o python letters.py <percorso_file.txt>

#Analizza il file specificato e conta la frequenza delle lettere dell'alfabeto (a-z).

#Opzioni:
 # --help        Mostra questo messaggio di aiuto.
#""")

#if __name__ == "__main__":
 #   if "--help" in sys.argv:
  #      stampa_help()
   # elif len(sys.argv) < 2:
    #    print("Uso: py letters.py <percorso_file.txt> o python letters.py <percorso_file.txt>")
    #else:
     #   path = sys.argv[1]
      #  risultato = letters(path)
       # print(risultato)

def print_histogram(freq_dict):
    print("Istogramma delle frequenze delle lettere:")
    max_count = max(freq_dict.values()) if freq_dict else 0
    max_stars = 50  # lunghezza massima della barra

    for lettera, count in freq_dict.items():
        if count > 0:
            # scala il numero di stelle in base al valore massimo
            stars = int(count / max_count * max_stars)
            print(f"{lettera}: {'*' * stars} ({count})")

def text_stats(file_path__):
    with open(file_path__, "r", encoding="utf-8") as file:
        testo = file.read()
        testo_senza_spazi = testo.translate(str.maketrans('', '', string.whitespace))
        num_characters = len(testo_senza_spazi)
        num_words = len(testo.split())
        num_lines = testo.count('\n') + 1 if testo else 0

        print("Statistiche base del libro:")
        print(f"Numero di caratteri: {num_characters}")
        print(f"Numero di parole: {num_words}")
        print(f"Numero di righe: {num_lines}")

def estrai_contenuto_custom(testo, start_marker=None, end_marker=None):
    """Estrae una porzione di testo delimitata da marker personalizzati"""
    start = 0
    end = len(testo)

    if start_marker:
        pos = testo.find(start_marker)
        if pos != -1:
            start = pos + len(start_marker)
        else:
            print(f"[ATTENZIONE] Start marker '{start_marker}' non trovato. Uso inizio file.")
    
    if end_marker:
        pos = testo.find(end_marker)
        if pos != -1:
            end = pos
        else:
            print(f"[ATTENZIONE] End marker '{end_marker}' non trovato. Uso fine file.")

    return testo[start:end].strip()

def plot_histogram(freq_dict):
    lettere = list(freq_dict.keys())
    frequenze = list(freq_dict.values())

    plt.figure(figsize=(10, 5))
    plt.bar(lettere, frequenze, color='skyblue')
    plt.title("Frequenze delle lettere")
    plt.xlabel("Lettere")
    plt.ylabel("Frequenza")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()    

#Utilizzo di argparse
def main():
    parser = argparse.ArgumentParser(
        description="Analizza un file .txt e conta la frequenza delle lettere dell'alfabeto (a-z)."
    )

     #Argomento posizionale: il file da analizzare
    parser.add_argument(
        "file",
        type=str,
        help="Percorso del file .txt da analizzare"
    )

    parser.add_argument(
        "--histogram",
        action="store_true",
        help="Mostra un istogramma testuale delle frequenze"
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Mostra il n° di caratteri, di parole e di linee del testo"
    )

    parser.add_argument(
        "--start_marker",
        type=str,
        help="Stringa di testo che indica dove inizia il contenuto del libro"
    )

    parser.add_argument(
        "--end_marker",
        type=str,
        help="Stringa di testo che indica dove finisce il contenuto del libro"
    )

    args = parser.parse_args()

    start_time = time.time()

    try:
        risultato = letters(
            args.file,
            args.start_marker,
            args.end_marker
        )
        print("Frequenza lettere nel file:")
        for lettera, conteggio in risultato.items():
            print(f"{lettera}: {conteggio}")
        if args.histogram:
            print_histogram(risultato)
            plot_histogram(risultato)
        if args.stats:
            text_stats(args.file)
    except FileNotFoundError:
        print(f"Errore: file non trovato → {args.file}")
    except Exception as e:
        print(f"Errore durante l'elaborazione del file: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nTempo totale: {elapsed_time:.4f} secondi")

if __name__ == "__main__":
    main()
