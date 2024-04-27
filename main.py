import streamlit as st
import pandas as pd

# Data sifat gas mulia
data = {
  "Helium": {
    "Kode atom": "H",
    "Nomor atom": 2,
    "Elektron valensi": 2,
    "Jari-jari atom": 0.5,
    "Titik leleh": -272.2,
    "Titik didih": -268.9,
    "Energi ionisasi": "2640 kJ/mol",
    "Afinitas elektron": "-48 kJ/mol"
  },
  "Neon": {
    "Kode atom": "Ne",
    "Nomor atom": 10,
    "Elektron valensi": 8,
    "Jari-jari atom": 0.65,
    "Titik leleh": -248.6,
    "Titik didih": -246.0,
    "Energi ionisasi": "2080 kJ/mol",
    "Afinitas elektron": "-120 kJ/mol"
  },
  "Argon": {
    "Kode atom": "Ar",
    "Nomor atom": 18,
    "Elektron valensi": 8,
    "Jari-jari atom": 0.95,
    "Titik leleh": -189.4,
    "Titik didih": -185.9,
    "Energi ionisasi": "1520 kJ/mol",
    "Afinitas elektron": "-96 kJ/mol"
  },
  "Krypton": {
    "Kode atom": "Kr",
    "Nomor atom": 36,
    "Elektron valensi": 8,
    "Jari-jari atom": 1.10,
    "Titik leleh": -157.2,
    "Titik didih": -153.4,
    "Energi ionisasi": "1350 kJ/mol",
    "Afinitas elektron": "-96 kJ/mol"
  },
  "Xenon": {
    "Kode atom": "Xe",
    "Nomor atom": 54,
    "Elektron valensi": 8,
    "Jari-jari atom": 1.30,
    "Titik leleh": -111.8,
    "Titik didih": -108.1,
    "Energi ionisasi": "1170 kJ/mol",
    "Afinitas elektron": "-77 kJ/mol"
  },
  "Radon": {
    "Kode atom": "Rn",
    "Nomor atom": 86,
    "Elektron valensi": 8,
    "Jari-jari atom": 1.45,
    "Titik leleh": -71,
    "Titik didih": -62,
    "Energi ionisasi": "1040 kJ/mol",
    "Afinitas elektron": "-kJ/Mol"
  }
}

# Judul aplikasi
st.title("Sifat Gas Mulia")

# Input nama atom
atom = st.selectbox("Pilih Atom", list(data.keys()))

# Output tabel sifat atom
st.header("Sifat Periodik", atom)
st.write(pd.DataFrame(data[atom], index=[0]).T)
