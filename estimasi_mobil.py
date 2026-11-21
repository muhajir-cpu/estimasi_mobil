
import pickle
import streamlit as st

# Memuat model machine learning
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Judul aplikasi
st.title('Estimasi Harga Mobil Bekas')
st.write('Masukkan spesifikasi mobil untuk mengetahui estimasi harganya.')

# Input data mobil
year = st.number_input('Input Tahun Mobil', min_value=1900, max_value=2100, value=2020)
mileage = st.number_input('Input Km Mobil', min_value=0, value=0)
tax = st.number_input('Input Pajak Mobil', min_value=0, value=0)
mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0.0, value=0.0)
engineSize = st.number_input('Input Engine Size', min_value=0.0, value=0.0)

# Tombol estimasi
if st.button('Estimasi Harga'):

    # Prediksi harga dalam Pound Sterling
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )

    # Mengambil hasil prediksi
    harga_pound = float(predict[0])

    # Konversi Pound ke Rupiah
    kurs = 19000
    harga_rupiah = harga_pound * kurs

    # Format mata uang Pound (£)
    format_pound = f"£{harga_pound:,.2f}"

    # Format mata uang Rupiah (Rp)
    format_rupiah = f"Rp {harga_rupiah:,.0f}".replace(",", ".")

    # Menampilkan hasil
    st.success('Estimasi Harga Mobil Berhasil Dihitung')

    st.subheader('Hasil Estimasi Harga')

    st.write('**Harga dalam Pound Sterling (GBP):**')
    st.title(format_pound)

    st.write('**Harga dalam Rupiah (IDR):**')
    st.title(format_rupiah)

    st.caption(f'Kurs konversi: £1 = Rp {kurs:,.0f}'.replace(",", "."))
