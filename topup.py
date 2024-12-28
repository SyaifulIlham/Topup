import streamlit as st
from statistik_pengguna import user_statistics_page
from lainnya import KebutuhanBulanan
from riwayat import purchase_history_page
from form_beli.form_page import (
    mobile_legend_form,
    free_fire_form,
    pubg_form,
    valorant_form,
    genshin_form,
)

def show_header():
    image_path = "img/CS.PNG"
    st.image(image_path, use_container_width=True)

def topup_main_page():
    show_header()
    st.title(f"🎮 CIHOOY.STORE - Selamat Datang, {st.session_state.get('username', 'User')}!")
    st.subheader("Top-Up Game & Voucher Online - Cepat dan Terpercaya")
    st.markdown(
        """
        *Selamat datang di CIHOOY.STORE!* 🚀  
        *Platform top-up terbaik untuk kebutuhan gaming kamu.*  
        Pilih game favoritmu dan nikmati proses top-up yang cepat, aman, dan mudah!
        """
    )
    if st.session_state.get("selected_game"):
        display_selected_game_form()
    else:
        display_game_choices()

def display_game_choices():
    st.markdown("### Pilih Game Favoritmu:")
    games = [
        {"name": "Mobile Legends", "icon": "https://downloadr2.apkmirror.com/wp-content/uploads/2024/05/42/6632d219632fb_com.mobile.legends-384x384.png"},
        {"name": "Free Fire", "icon": "https://cdn6.aptoide.com/imgs/4/8/3/483528c77a19be6735661c5f68a749ea_icon.png"},
        {"name": "PUBG Mobile", "icon": "https://cdn6.aptoide.com/imgs/e/b/e/ebe4c3a3d00e00e9b26d18fcde77a3b6_icon.png"},
        {"name": "Valorant", "icon": "https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png"},
        {"name": "Genshin Impact", "icon": "https://i.pinimg.com/736x/6c/c7/44/6cc7444ea5e7628b57486c5e5d7d8040.jpg"},
    ]
    for game in games:
        show_game_button(game)

def show_game_button(game):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image(game["icon"], width=100, use_container_width=True)
    with col2:
        st.markdown(f"#### {game['name']}")
        st.markdown("##### ✨ Proses Top-Up Cepat & Mudah!")
    with col3:
        if st.button(f"Top-Up {game['name']}"):
            st.session_state.selected_game = game["name"]
            st.session_state.is_form_open = True
            st.rerun()

def display_selected_game_form():
    game = st.session_state.selected_game
    st.markdown(f"### Form Top-Up untuk {game}")
    if game == "Mobile Legends":
        mobile_legend_form()
    elif game == "Free Fire":
        free_fire_form()
    elif game == "PUBG Mobile":
        pubg_form()
    elif game == "Valorant":
        valorant_form()
    elif game == "Genshin Impact":
        genshin_form()

def render_sidebar():
    st.sidebar.title("💡 Pilihan Menu")
    if st.sidebar.button("🎮 Top-Up Game"):
        st.session_state["current_page"] = "topup"
        st.session_state["selected_game"] = None
    if st.sidebar.button("📦 Kebutuhan Lainnya"):
        st.session_state["current_page"] = "other_needs"
    if st.sidebar.button("🛒 Riwayat Pembelian"):
        st.session_state["current_page"] = "purchase_history"
    if st.sidebar.button("📊 Statistik Pengguna"):
        st.session_state["current_page"] = "user_statistics"

if __name__ == "__main__":
    if "username" not in st.session_state:
        st.session_state["username"] = "User"
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "topup"

    render_sidebar()

    # Render halaman sesuai current_page
    if st.session_state["current_page"] == "topup":
        topup_main_page()
    elif st.session_state["current_page"] == "other_needs":
        kebutuhan = KebutuhanBulanan()
        kebutuhan.run()
    elif st.session_state["current_page"] == "purchase_history":
        purchase_history_page()
    elif st.session_state["current_page"] == "user_statistics":
        user_statistics_page()
