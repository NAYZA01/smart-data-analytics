import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

class SmartDataAnalyzer:
    """
    Akıllı Veri Analiz Motoru
    Verileri analiz edip, grafikler için JSON çıktısı ve yorumlar üretir
    """
    
    def __init__(self):
        self.df = None
        self.insights = []
        self.strategies = []
        
    def load_sample_data(self):
        """Örnek satış verisi oluştur"""
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        np.random.seed(42)
        
        categories = ['Elektronik', 'Giyim', 'Gıda', 'Ev & Yaşam', 'Kozmetik']
        regions = ['İstanbul', 'Ankara', 'İzmir', 'Antalya', 'Bursa']
        
        data = []
        for date in dates:
            for _ in range(np.random.randint(5, 15)):
                data.append({
                    'Tarih': date,
                    'Kategori': np.random.choice(categories),
                    'Bölge': np.random.choice(regions),
                    'Satış_Miktarı': np.random.randint(1, 20),
                    'Birim_Fiyat': np.random.uniform(50, 500),
                    'Müşteri_Memnuniyeti': np.random.uniform(3.0, 5.0)
                })
        
        self.df = pd.DataFrame(data)
        self.df['Toplam_Gelir'] = self.df['Satış_Miktarı'] * self.df['Birim_Fiyat']
        self.df['Ay'] = self.df['Tarih'].dt.to_period('M').astype(str)
        
    def analyze_trends(self):
        """Trend analizi ve yorumlar"""
        monthly = self.df.groupby('Ay').agg({
            'Toplam_Gelir': 'sum',
            'Satış_Miktarı': 'sum'
        }).reset_index()
        
        # Son 3 ay vs önceki 3 ay karşılaştırması
        last_3 = monthly.tail(3)['Toplam_Gelir'].sum()
        prev_3 = monthly.tail(6).head(3)['Toplam_Gelir'].sum()
        change = ((last_3 - prev_3) / prev_3) * 100
        
        if change > 10:
            self.insights.append({
                'type': 'success',
                'title': '📈 Güçlü Büyüme Trendi',
                'message': f'Son 3 ayda gelir %{change:.1f} arttı. Mevcut stratejiler etkili.',
                'priority': 'high'
            })
            self.strategies.append({
                'title': 'Momentum Koruma',
                'actions': [
                    'Başarılı kampanyaları tekrarla',
                    'Stok seviyelerini artır',
                    'Pazarlama bütçesini %20 yükselt'
                ]
            })
        elif change < -10:
            self.insights.append({
                'type': 'warning',
                'title': '⚠️ Dikkat: Gelir Düşüşü',
                'message': f'Son 3 ayda gelir %{abs(change):.1f} düştü. Acil aksiyon gerekli!',
                'priority': 'critical'
            })
            self.strategies.append({
                'title': 'Acil Müdahale Planı',
                'actions': [
                    'Fiyat stratejisini gözden geçir',
                    'Müşteri geri bildirimlerini analiz et',
                    'Rakip analizi yap',
                    'Promosyon kampanyası başlat'
                ]
            })
        
        return monthly
    
    def analyze_categories(self):
        """Kategori analizi"""
        cat_analysis = self.df.groupby('Kategori').agg({
            'Toplam_Gelir': 'sum',
            'Satış_Miktarı': 'sum',
            'Müşteri_Memnuniyeti': 'mean'
        }).reset_index()
        
        cat_analysis['Kar_Marjı'] = np.random.uniform(15, 45, len(cat_analysis))
        cat_analysis = cat_analysis.sort_values('Toplam_Gelir', ascending=False)
        
        # En iyi ve en kötü performans
        best = cat_analysis.iloc[0]
        worst = cat_analysis.iloc[-1]
        
        self.insights.append({
            'type': 'info',
            'title': f'🏆 En İyi Kategori: {best["Kategori"]}',
            'message': f'₺{best["Toplam_Gelir"]:,.0f} gelir ile lider. Ortalama memnuniyet: {best["Müşteri_Memnuniyeti"]:.2f}/5',
            'priority': 'medium'
        })
        
        self.insights.append({
            'type': 'warning',
            'title': f'📉 Zayıf Performans: {worst["Kategori"]}',
            'message': f'Sadece ₺{worst["Toplam_Gelir"]:,.0f} gelir. İyileştirme gerekli.',
            'priority': 'medium'
        })
        
        self.strategies.append({
            'title': f'{best["Kategori"]} - Büyüme Fırsatı',
            'actions': [
                'Ürün çeşitliliğini artır',
                'Premium segment oluştur',
                'Cross-selling stratejileri uygula'
            ]
        })
        
        self.strategies.append({
            'title': f'{worst["Kategori"]} - İyileştirme',
            'actions': [
                'Ürün portföyünü gözden geçir',
                'Fiyatlandırma stratejisini test et',
                'Müşteri anketleri düzenle',
                'Kârsızsa kategoriden çıkışı değerlendir'
            ]
        })
        
        return cat_analysis
    
    def analyze_regions(self):
        """Bölgesel analiz"""
        region_data = self.df.groupby('Bölge').agg({
            'Toplam_Gelir': 'sum',
            'Satış_Miktarı': 'sum'
        }).reset_index().sort_values('Toplam_Gelir', ascending=False)
        
        top_region = region_data.iloc[0]
        
        self.insights.append({
            'type': 'info',
            'title': f'🌍 En Güçlü Pazar: {top_region["Bölge"]}',
            'message': f'₺{top_region["Toplam_Gelir"]:,.0f} gelir ile öne çıkıyor.',
            'priority': 'low'
        })
        
        return region_data
    
    def detect_anomalies(self):
        """Anormal durumlar tespit et"""
        daily_revenue = self.df.groupby('Tarih')['Toplam_Gelir'].sum()
        mean_rev = daily_revenue.mean()
        std_rev = daily_revenue.std()
        
        anomalies = daily_revenue[daily_revenue > mean_rev + 2*std_rev]
        
        if len(anomalies) > 0:
            self.insights.append({
                'type': 'success',
                'title': '💎 Olağanüstü Günler Tespit Edildi',
                'message': f'{len(anomalies)} günde normalin çok üstünde satış yapıldı. Pattern analizi öneriliyor.',
                'priority': 'high'
            })
            
            self.strategies.append({
                'title': 'Başarı Faktörleri Analizi',
                'actions': [
                    'Yüksek satış günlerindeki kampanyaları listele',
                    'Müşteri davranış paternlerini incele',
                    'Başarılı günlerin özelliklerini tekrarla',
                    'Sezonsal faktörleri değerlendir'
                ]
            })
    
    def calculate_kpis(self):
        """Ana KPI'lar"""
        return {
            'toplam_gelir': float(self.df['Toplam_Gelir'].sum()),
            'ortalama_siparis': float(self.df['Toplam_Gelir'].mean()),
            'toplam_satis': int(self.df['Satış_Miktarı'].sum()),
            'ortalama_memnuniyet': float(self.df['Müşteri_Memnuniyeti'].mean()),
            'aktif_kategori': int(self.df['Kategori'].nunique()),
            'aktif_bolge': int(self.df['Bölge'].nunique())
        }
    
    def generate_chart_data(self):
        """Grafikler için veri hazırla"""
        monthly = self.analyze_trends()
        categories = self.analyze_categories()
        regions = self.analyze_regions()
        
        return {
            'monthly_trend': {
                'labels': monthly['Ay'].tolist(),
                'data': monthly['Toplam_Gelir'].tolist()
            },
            'category_pie': {
                'labels': categories['Kategori'].tolist(),
                'data': categories['Toplam_Gelir'].tolist()
            },
            'region_bar': {
                'labels': regions['Bölge'].tolist(),
                'data': regions['Toplam_Gelir'].tolist()
            },
            'category_performance': {
                'labels': categories['Kategori'].tolist(),
                'satisfaction': categories['Müşteri_Memnuniyeti'].tolist(),
                'margin': categories['Kar_Marjı'].tolist()
            }
        }
    
    def run_full_analysis(self):
        """Tam analiz çalıştır"""
        self.load_sample_data()
        self.analyze_trends()
        self.analyze_categories()
        self.analyze_regions()
        self.detect_anomalies()
        
        result = {
            'kpis': self.calculate_kpis(),
            'charts': self.generate_chart_data(),
            'insights': self.insights,
            'strategies': self.strategies,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return result

# Ana çalıştırma
if __name__ == '__main__':
    analyzer = SmartDataAnalyzer()
    results = analyzer.run_full_analysis()
    
    # JSON olarak kaydet (HTML ile entegrasyon için)
    with open('analysis_data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("✅ Analiz tamamlandı! Dashboard için veri hazır.")
    print(f"📊 Toplam Gelir: ₺{results['kpis']['toplam_gelir']:,.2f}")
    print(f"🎯 {len(results['insights'])} içgörü ve {len(results['strategies'])} strateji oluşturuldu.")