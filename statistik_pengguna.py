import streamlit as st

def user_statistics_page():
    st.title("📊 Statistik Pengguna")
    
    username = st.session_state.get("username", "User")
    st.subheader(f"Statistik untuk {username}")

    # Ambil riwayat pembelian pengguna
    purchase_history = st.session_state.get("purchase_history", [])

    # Jika tidak ada pembelian
    if not purchase_history:
        st.write("Anda belum melakukan pembelian.")
        return

    # Menghitung total pengeluaran dan transaksi per item
    item_stats = {}
    total_spent = 0
    total_transactions = 0

    for purchase in purchase_history:
        item_name = purchase.get("item", "Tidak Diketahui")
        jumlah = purchase.get("jumlah", 0)
        total_harga = purchase.get("total_harga", 0)

        # Update total
        total_spent += total_harga
        total_transactions += 1

        # Update stats per item
        if item_name not in item_stats:
            item_stats[item_name] = {"jumlah_transaksi": 0, "total_dana": 0}
        item_stats[item_name]["jumlah_transaksi"] += 1
        item_stats[item_name]["total_dana"] += total_harga

    # Item dengan jumlah transaksi dan dana terbanyak
    item_most_transactions = max(item_stats, key=lambda x: item_stats[x]["jumlah_transaksi"], default=None)
    item_highest_spent = max(item_stats, key=lambda x: item_stats[x]["total_dana"], default=None)

    # Tampilkan statistik
    st.write(f"🔹 **Total Pengeluaran**: Rp {total_spent:,}")
    st.write(f"🔹 **Jumlah Transaksi yang Telah Dilakukan**: {total_transactions}")

    st.markdown("### Statistik Per Item")
    for item, stats in item_stats.items():
        st.write(f"- **{item}**: {stats['jumlah_transaksi']} transaksi, Rp {stats['total_dana']:,}")

    st.markdown("### Item Terpopuler")
    if item_most_transactions:
        st.write(f"🔸 **Jumlah Transaksi Terbanyak**: {item_most_transactions} ({item_stats[item_most_transactions]['jumlah_transaksi']} transaksi)")
    else:
        st.write("🔸 **Jumlah Transaksi Terbanyak**: Tidak ada data")

    if item_highest_spent:
        st.write(f"🔸 **Dana Terbanyak Dikeluarkan**: {item_highest_spent} (Rp {item_stats[item_highest_spent]['total_dana']:,})")
    else:
        st.write("🔸 **Dana Terbanyak Dikeluarkan**: Tidak ada data")
