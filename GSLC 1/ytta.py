# 2502004405 - Dimas Syauqi Syafa (LA-20)

"""
  Import function system() dari library "os"
function ini saya gunakan untuk handle error
ketika proses import library, lalu library tsb
tidak ada, maka akan otomatis eksekusi command
pip install {nama library}
"""
from os import system

# Try Except (handle error ModuleNotFoundError)
try:
  import Bio
# Jika Library tidak ditemukan, maka download library
except ModuleNotFoundError:
  system("pip install biopython")
  import Bio

# Try Except (handle error ImportError)
try:
  import Bio
# Jika Library tidak dapat diimport, maka akan exit(1)
except ImportError:
  exit(1)

# Import library yang dibutuhkan
from Bio import Seq
from Bio.SeqUtils import GC, MeltingTemp as mt, molecular_weight as mw

# --- Penyelesaian untuk nomor 1 ---

# Deklarasi sequence variable berdasarkan yang ada di soal
genericDNA_1 = 'ATGATCTCGTAA'
genericDNA_2 = 'ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAA'

# --- Penyelesaian untuk nomor 2 ---

# Dapatkan jumlah frekuensi setiap basa pada seq 1,
# Kemudian tampilkan langsung hasilnya
print("\n # Frequensi DNA Sequence-1 :")
print(f"   A berjumlah {genericDNA_1.count('A')}")
print(f"   T berjumlah {genericDNA_1.count('T')}")
print(f"   C berjumlah {genericDNA_1.count('C')}")
print(f"   G berjumlah {genericDNA_1.count('G')}")

# Dapatkan jumlah frekuensi setiap basa pada seq 2,
# Kemudian tampilkan langsung hasilnya
print("\n # Frequensi DNA Sequence-2 :")
print(f"   A berjumlah {genericDNA_2.count('A')}")
print(f"   T berjumlah {genericDNA_2.count('T')}")
print(f"   C berjumlah {genericDNA_2.count('C')}")
print(f"   G berjumlah {genericDNA_2.count('G')}")

# --- Penyelesaian untuk nomor 3 ---

# Membuat function untuk mencari kandungan AT
def AT(seq):
  # Rumus dari PPT Comp. BIO LAB Sesi-2 (slide 5)
  return float(seq.count('A') + seq.count('T')) / len(seq) * 100
  
# Menghitung Kandungan GC dengan function GC() => tampilkan
print("\n # Kandungan GC :")
print(f"   sequence-1 sebesar {GC(genericDNA_1)}")
print(f"   sequence-2 sebesar {GC(genericDNA_2)}")

# Menghitung Kandungan AT dengan function AT() => tampilkan
print("\n # Kandungan AT :")
print(f"   sequence-1 sebesar {AT(genericDNA_1)}")
print(f"   sequence-2 sebesar {AT(genericDNA_2)}")

# Menghitung titik leleh dengan function *.Tm_Wallace() => tampilkan
print("\n # Titik Leleh :")
print(f"   sequence-1 sebesar {mt.Tm_Wallace(genericDNA_1)}")
print(f"   sequence-2 sebesar {mt.Tm_Wallace(genericDNA_2)}\n")

# --- Penyelesaian untuk nomor 4 ---

# Tampilkan berat molekul
print("\n # Berat Molekul :")
print(f"   sequence-1 sebesar {mw(genericDNA_1)}")
print(f"   sequence-2 sebesar {mw(genericDNA_2)}")

# Tampilkan titik didihnya
print("\n # Titik Didih Molekul :")
print(f"   sequence-1 sebesar {mt.Tm_NN(genericDNA_1)}")
print(f"   sequence-2 sebesar {mt.Tm_NN(genericDNA_2)}\n")
