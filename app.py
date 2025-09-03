import streamlit as st
from PIL import Image
import numpy as np
import io

# =============================
# Konfigurasi Halaman
# =============================
st.set_page_config(
    page_title="Solidaritas Indonesia Filter",
    page_icon="🇮🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# Custom CSS untuk UI yang lebih menarik
# =============================
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #18472c, #ec5dab);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .upload-section {
        border: 2px dashed #ec5dab;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        background: linear-gradient(145deg, #f8f9fa, #ffffff);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #18472c;
    }
    
    .color-preview {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 1rem 0;
    }
    
    .color-box {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .stats-container {
        background: linear-gradient(135deg, #18472c, #ec5dab);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .download-section {
        background: linear-gradient(135deg, #18472c20, #ec5dab20);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# =============================
# Header Section
# =============================
st.markdown('<h1 class="main-header">🇮🇩 Solidaritas Indonesia Filter</h1>', unsafe_allow_html=True)
st.markdown('''
<div class="subtitle">
    Ubah fotomu jadi gaya <strong>hijau & pink</strong> yang sedang tren di Indonesia 
    sebagai bentuk solidaritas dan dukungan. Gratis, mudah, dan cepat! ✨
</div>
''', unsafe_allow_html=True)

# =============================
# Sidebar dengan informasi
# =============================
with st.sidebar:
    st.header("📋 Panduan Penggunaan")
    st.markdown("""
    1. **Upload foto** dari galeri Anda
    2. **Tunggu proses** filter otomatis
    3. **Download hasil** dengan 1 klik
    4. **Bagikan** ke media sosial!
    """)
    
    st.header("🎨 Warna Filter")
    st.markdown('''
    <div class="color-preview">
        <div class="color-box" style="background-color: rgb(24, 71, 36);">Hijau</div>
        <div class="color-box" style="background-color: rgb(236, 93, 171);">Pink</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.header("ℹ️ Tentang Filter")
    st.markdown("""
    Filter ini menggunakan teknik **duotone** yang mengubah foto hitam-putih 
    menjadi kombinasi dua warna simbolis untuk menunjukkan solidaritas.
    """)
    
    st.header("📊 Statistik")
    st.markdown('''
    <div class="stats-container">
        <h3>🎯 Filter Terpopuler</h3>
        <p>Digunakan ribuan orang Indonesia</p>
    </div>
    ''', unsafe_allow_html=True)

# =============================
# Main Content
# =============================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('''
    <div class="upload-section">
    ''', unsafe_allow_html=True)
    
    st.subheader("📷 Upload Foto Anda")
    uploaded_file = st.file_uploader(
        "Pilih foto (JPG, JPEG, PNG)", 
        type=["jpg", "jpeg", "png"],
        help="Ukuran maksimal 5MB untuk hasil terbaik"
    )
    
    if uploaded_file is None:
        st.info("👆 Pilih foto untuk memulai transformasi!")
        st.markdown("**Tips:** Gunakan foto dengan kontras yang baik untuk hasil optimal.")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("✨ Hasil Filter")
    
    # =============================
    # Proses Foto
    # =============================
    if uploaded_file is not None:
        try:
            # Progress bar untuk pengalaman yang lebih baik
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text('🔄 Memuat gambar...')
            progress_bar.progress(25)
            
            # Buka gambar & konversi grayscale
            img = Image.open(uploaded_file).convert("L")
            img_array = np.array(img)
            
            status_text.text('🎨 Menerapkan filter...')
            progress_bar.progress(50)
            
            # Warna duotone (sesuai gambar tren)
            dark_color = np.array([24, 71, 36])     # Hijau gelap
            light_color = np.array([236, 93, 171])  # Pink magenta
            
            # Normalisasi pixel (0–255 -> 0–1)
            norm = img_array / 255.0
            
            status_text.text('🌈 Memproses warna...')
            progress_bar.progress(75)
            
            # Interpolasi linear hijau → pink
            colored = (dark_color[None, None, :] * (1 - norm[..., None]) +
                       light_color[None, None, :] * norm[..., None]).astype(np.uint8)
            
            result = Image.fromarray(colored)
            
            status_text.text('✅ Selesai!')
            progress_bar.progress(100)
            
            # Tampilkan hasil dengan border yang menarik
            st.image(
                result, 
                caption="🎯 Foto dengan Filter Solidaritas", 
                use_container_width=True
            )
            
            # Hapus progress bar setelah selesai
            progress_bar.empty()
            status_text.empty()
            
            # =============================
            # Section Download
            # =============================
            st.markdown('''
            <div class="download-section">
            ''', unsafe_allow_html=True)
            
            # Simpan ke buffer untuk download
            buf = io.BytesIO()
            result.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            # Informasi file
            col_info1, col_info2 = st.columns(2)
            with col_info1:
                st.metric("📏 Dimensi", f"{result.size[0]} × {result.size[1]}")
            with col_info2:
                st.metric("💾 Ukuran", f"{len(byte_im) / 1024:.1f} KB")
            
            # Tombol download yang menarik
            st.download_button(
                label="⬇️ Download Foto Solidaritas",
                data=byte_im,
                file_name=f"solidaritas_indonesia_{uploaded_file.name.split('.')[0]}.png",
                mime="image/png",
                use_container_width=True
            )
            
            st.markdown("**💡 Tips Sharing:** Tag teman-temanmu dan gunakan hashtag #SolidaritasIndonesia")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {str(e)}")
            st.info("Coba upload foto dengan format dan ukuran yang berbeda.")
    else:
        st.info("🎯 Upload foto di sebelah kiri untuk melihat hasil filter!")
        
        # Tampilkan contoh hasil
        st.markdown("**Contoh Hasil Filter:**")
        st.markdown('''
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #18472c20, #ec5dab20); border-radius: 15px; margin: 1rem 0;">
            <p style="font-size: 4rem; margin: 0;">🖼️</p>
            <p style="color: #666;">Foto Anda akan tampil di sini</p>
        </div>
        ''', unsafe_allow_html=True)

# =============================
# Footer Section
# =============================
st.markdown("---")
st.markdown('''
<div style="text-align: center; padding: 1rem; color: #666;">
    <p>🇮🇩 <strong>Dibuat dengan ❤️ untuk Indonesia</strong></p>
    <p><small>Filter ini dibuat untuk menunjukkan solidaritas dan persatuan bangsa Indonesia</small></p>
</div>
''', unsafe_allow_html=True)

# =============================
# Features Cards
# =============================
st.subheader("🌟 Keunggulan Filter Ini")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
    <div class="feature-card">
        <h4>⚡ Super Cepat</h4>
        <p>Proses foto dalam hitungan detik tanpa menunggu lama</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="feature-card">
        <h4>🎨 Kualitas Tinggi</h4>
        <p>Hasil foto tetap tajam dan berkualitas untuk dibagikan</p>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="feature-card">
        <h4>🔒 Aman & Privat</h4>
        <p>Foto Anda tidak disimpan di server, 100% aman</p>
    </div>
    ''', unsafe_allow_html=True)
