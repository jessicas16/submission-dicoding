import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Menampilkan judul aplikasi
st.title("Dashboard Analisis Data E-Commerce")

# Sidebar
with st.sidebar:
    # Title
    st.title("Submission Dicoding")
    st.title("Jessica Susanto")

# Memuat dataset
customers_df = pd.read_csv('./dataset/customers_dataset.csv')
geo_df = pd.read_csv('./dataset/geolocation_dataset.csv')
order_items = pd.read_csv('./dataset/order_items_dataset.csv')
order_pay = pd.read_csv('./dataset/order_payments_dataset.csv')
order_rev = pd.read_csv('./dataset/order_reviews_dataset.csv')
orders_df = pd.read_csv('./dataset/orders_dataset.csv')
product_cat = pd.read_csv('./dataset/product_category_name_translation.csv')
products_df = pd.read_csv('./dataset/products_dataset.csv')
sellers_df = pd.read_csv('./dataset/sellers_dataset.csv')

# Menampilkan visualisasi Tren Penjualan dari waktu ke waktu
st.subheader("Tren Penjualan dari Waktu ke Waktu")

# Convert the order_purchase_timestamp to datetime format
orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])

# Extract year and month for grouping
orders_df['year_month'] = orders_df['order_purchase_timestamp'].dt.to_period('M')

# Group by year and month to count the number of orders
sales_trend = orders_df.groupby('year_month').size()

# Plot the trend of orders over time
fig, ax = plt.subplots(figsize=(10, 6))
sales_trend.plot(ax=ax)
ax.set_title('Tren Penjualan dari Waktu ke Waktu')
ax.set_xlabel('Waktu (Year-Month)')
ax.set_ylabel('Jumlah Pesanan')
ax.grid(True)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Menampilkan penjelasan visualisasi Tren Penjualan
with st.expander("See Explanation"):
    st.write("""
        Data Tertinggi: Pada bulan Oktober 2017, penjualan mencapai puncaknya dengan lebih dari 7.000 pesanan. \n
        Data Terendah: Penjualan terendah terjadi pada bulan September 2016 dengan hampir 0 pesanan. \n
        Wawasan: Penjualan meningkat secara signifikan dari awal 2017 dan mencapai puncaknya di akhir tahun. Kemudian, tren mulai turun setelah awal tahun 2018.
    """)

# Menampilkan visualisasi Metode Pembayaran
st.subheader("Distribusi Metode Pembayaran")

# Group by payment_type to count the number of payments for each method
payment_type_distribution = order_pay['payment_type'].value_counts()

# Plot the distribution of payment types
fig, ax = plt.subplots(figsize=(8, 6))
payment_type_distribution.plot(kind='bar', ax=ax)
ax.set_title('Distribusi Metode Pembayaran')
ax.set_xlabel('Metode Pembayaran')
ax.set_ylabel('Jumlah Penggunaan')
ax.grid(True)
st.pyplot(fig)

# Menampilkan penjelasan visualisasi Metode Pembayaran
with st.expander("See Explanation"):
    st.write("""
        Metode Pembayaran Tertinggi: Kartu Kredit digunakan paling sering dengan lebih dari 75.000 kali penggunaan.  \n
        Metode Pembayaran Terendah: Voucher digunakan paling sedikit, dengan kurang dari 5.000 kali penggunaan. \n
        Wawasan: Kartu kredit adalah metode pembayaran yang paling dominan, sedangkan metode alternatif seperti voucher dan kartu debit hanya digunakan oleh sebagian kecil pelanggan.
    """)

# Menampilkan visualisasi Distribusi Ulasan Pelanggan
st.subheader("Distribusi Skor Ulasan Pelanggan")

# Group by review_score to count the number of reviews for each score
review_score_distribution = order_rev['review_score'].value_counts().sort_index()

# Plot the distribution of review scores
fig, ax = plt.subplots(figsize=(8, 6))
review_score_distribution.plot(kind='bar', ax=ax)
ax.set_title('Distribusi Skor Ulasan Pelanggan')
ax.set_xlabel('Skor Ulasan')
ax.set_ylabel('Jumlah Ulasan')
ax.grid(True)
st.pyplot(fig)

# Menampilkan penjelasan visualisasi ulasan pelanggan
with st.expander("See Explanation"):
    st.write("""
        kor Ulasan Tertinggi: Skor 5 adalah skor yang paling sering diberikan oleh pelanggan, dengan lebih dari 60.000 ulasan.  \n
        Skor Ulasan Terendah: Skor 2 adalah yang paling jarang diberikan, dengan kurang dari 5.000 ulasan. \n
        Wawasan: Sebagian besar pelanggan memberikan ulasan positif dengan skor tinggi, menunjukkan kepuasan yang tinggi terhadap produk dan layanan. Namun, ada juga sejumlah kecil pelanggan yang memberikan skor rendah, yang mungkin perlu ditelusuri lebih lanjut.
    """)
