# Smart Data Analyzer

Akıllı satış verisi analiz aracı: Veri üret, analiz et, dashboard ile görselleştir!

📦 **Proje Yapısı**
1. **Python Backend (smart_data_analyzer.py)**

   - **Veri Üretimi:** Gerçekçi satış verileri oluşturur
   - **Analiz Motorları:**
     - 📈 Trend analizi (büyüme/düşüş tespiti)
     - 🏆 Kategori performans analizi
     - 🌍 Bölgesel satış analizi
     - 💎 Anomali tespiti (olağanüstü satış günleri)

   - **JSON Çıktısı:** Dashboard için veri hazırlar

2. **HTML/CSS/JS Dashboard**
   - Modern, responsive ve interaktif arayüz:
     - **KPI Kartları:** 6 temel metrik
     - **4 Farklı Grafik:**
       - Line chart (trend)
       - Pie/Doughnut chart (kategori dağılımı)
       - Bar chart (bölgesel)
       - Bubble chart (performans matrisi)
     - **Akıllı İçgörüler:** Renkli kartlarla önceliklendirilmiş
     - **Strateji Önerileri:** Aksiyon planları

🎯 **Öne Çıkan Özellikler**
- Sadece grafik değil, **YORUM ve STRATEJİ**!
- ✅ Otomatik gelir düşüş/artış tespiti
- ✅ En iyi ve en kötü performans analizi
- ✅ Anomali tespiti ve pattern analizi
- ✅ Her içgörü için öncelik seviyesi (kritik/yüksek/orta)
- ✅ Her sorun için somut aksiyon planları
- ✅ Responsive tasarım (mobil uyumlu)
- ✅ CSV yükleme desteği (kendi verini analiz et!)

🚀 **Kullanım**
```bash
# 1. Python ile veriyi analiz et (veya CSV yükle)
python smart_data_analyzer.py  # Örnek veri üretir
# veya: python smart_data_analyzer.py --csv my_sales.csv

# 2. Oluşan analysis_data.json'ı HTML'e entegre et (otomatik!)

# 3. Dashboard'u tarayıcıda aç
# index.html'i çift tıkla veya live server kullan
