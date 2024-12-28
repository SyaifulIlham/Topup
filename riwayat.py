import streamlit as st

def purchase_history_page():
    st.title("Riwayat Pembelian")
    st.markdown("### Daftar Transaksi Kamu")

    if "purchase_history" in st.session_state and st.session_state.purchase_history:
        for idx, purchase in enumerate(st.session_state.purchase_history, start=1):
            # Menentukan jenis transaksi berdasarkan kunci yang ada
            if "game" in purchase and "uid" in purchase:
                jenis = "game"
            elif "jenis_pembayaran" in purchase and "nama_pengguna" in purchase:
                jenis = "kebutuhan"
            else:
                jenis = "tidak_diketahui"

            # Menampilkan data berdasarkan jenis transaksi
            if jenis == "game":
                st.markdown(f"### Transaksi Game {idx}")
                st.write(f"**ID Transaksi:** {purchase.get('id_transaksi', 'Tidak diketahui')}")
                st.write(f"**Nama Item:** {purchase.get('item', 'Tidak diketahui')}")
                st.write(f"**Nama Pembeli:** {purchase.get('username', 'Tidak diketahui')}")
                st.write(f"**UID:** {purchase.get('uid', 'Tidak diketahui')}")
                st.write(f"**Total Harga:** Rp {purchase.get('total_harga', 0):,}")
                st.write(f"**Metode Pembayaran:** {purchase.get('metode_pembayaran', 'Tidak diketahui')}")
            elif jenis == "kebutuhan":
                st.markdown(f"### Transaksi Kebutuhan Lainnya {idx}")
                st.write(f"**ID Transaksi:** {purchase.get('id_transaksi', 'Tidak diketahui')}")
                st.write(f"**Jenis Pembayaran:** {purchase.get('jenis_pembayaran', 'Tidak diketahui')}")
                st.write(f"**Nama provider:** {purchase.get('nama_pengguna', 'Tidak diketahui')}")
                st.write(f"**Total Harga:** Rp {purchase.get('total_harga', 0):,}")
                st.write(f"**Metode Pembayaran:** {purchase.get('metode_pembayaran', 'Tidak diketahui')}")
            else:
                st.warning(f"Transaksi tidak dikenali: {purchase}")
            
            st.markdown("---")
    else:
        st.info("Belum ada riwayat pembelian.")
