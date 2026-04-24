import streamlit as st
import base64

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HBD Alifairuz Nadiah", layout="centered")

# 2. Fungsi Audio (Base64 agar bisa autoplay)
def get_audio_html(file_path, auto_play=False):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            return f'<audio {"autoplay" if auto_play else ""} controls style="width:100%; margin-bottom: 20px;"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
    except:
        return "<p style='color:red;'>File audio tidak ditemukan</p>"

# 3. CSS & Auto-Scroll Script (SUDAH DIPERBAIKI TANDA KUTIPNYA)
st.markdown("""
    <style>
    .stApp { background-color: #FFF5F7; }
    h1, h2, h3 { color: #D87093 !important; font-family: 'Georgia', serif; text-align: center; }
    .stImage img { border-radius: 30px; border: 4px solid #F4B4D0; }
    </style>
    
    <script>
    function startScroll() {
        const speed = 0.6; 
        function step() {
            window.scrollBy(0, speed);
            if ((window.innerHeight + window.scrollY) < document.body.offsetHeight) {
                window.requestAnimationFrame(step);
            }
        }
        window.requestAnimationFrame(step);
    }
    // Memulai scroll otomatis setelah 3 detik
    setTimeout(startScroll, 3000);
    </script>
""", unsafe_allow_html=True)

# 4. Logic Login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h1>For My Beautiful Wife</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        password = st.text_input("Enter Key:", type="password")
        if st.button("Unlock Surprise ✨"):
            if password.upper() == "250498":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Kuncinya salah, Sayang...")
else:
    # 5. Konten Utama
    # Musik Latar (Background.mp3)
    st.markdown(get_audio_html("Background.mp3", auto_play=True), unsafe_allow_html=True)
    
    st.markdown("<h1>Happy Birthday, <br>Alifairuz Nadiah 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Setiap detik bersamamu adalah hadiah terindah.</p>", unsafe_allow_html=True)
    st.write("<br><br><br>", unsafe_allow_html=True)

    # List Gallery (Sesuaikan nama file di folder kamu!)
    gallery = [
        {"img": "1.jpeg", "vo": "vo1.m4a", "txt": "Seorang wanita hebat lahir, wanita cantik dan sholehah"},
        {"img": "2.jpeg", "vo": "vo2.m4a", "txt": "Dunia membuat mu tumbuh menjadi wanita hebat."},
        {"img": "3.jpeg", "vo": "vo3.m4a", "txt": "Dunia tidak selalu indah tapi kamu berhasil melewati itu semua."},
        {"img": "4.jpeg", "vo": "vo4.m4a", "txt": "Kamu adalah akhirat dan duniaku."},
        {"img": "5.jpeg", "vo": "vo5.m4a", "txt": "Terima kasih sudah memilihku."},
        {"img": "6.jpeg", "vo": "vo6.m4a", "txt": "Mari menua bersama."},
        {"img": "7.jpeg", "vo": "vo7.m4a", "txt": "I love you forever, Sayang."}
    ]

    for item in gallery:
        try:
            st.image(item["img"], use_container_width=True)
            st.markdown(get_audio_html(item["vo"]), unsafe_allow_html=True)
            st.markdown(f"<h3>{item['txt']}</h3>", unsafe_allow_html=True)
            st.write("<br><br><br><br><br><br>", unsafe_allow_html=True)
        except:
            st.error(f"File {item['img']} tidak ditemukan di folder.")

    # Ucapan Internasional
    st.write("---")
    st.markdown("<h3>SELAMAT ULANG TAHUN SAYANG</h3>", unsafe_allow_html=True)
    st.write("Dari suamimu yang tercinta, hadiah selanjutnya di Kalimantan aja ya :p")
    st.balloons()
