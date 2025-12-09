# Bank Customer Churn Prediction 🏦

Bu proje, bankacılık sektöründe müşteri terkini (churn) tahmin etmek amacıyla geliştirilmiş uçtan uca bir makine öğrenmesi projesidir. Kaggle üzerindeki veri seti kullanılarak, müşterilerin bankayı terk edip etmeyeceği **%86.9** doğruluk oranıyla tahmin edilmiştir.

## 🔗 Canlı Demo (Deployment)
Projenin çalışan halini ve model tahminlerini aşağıdaki linkten inceleyebilirsiniz:
- **Streamlit App:** https://bank-churn-prediction-m52dapvmvsa2hkgwgxmrzb.streamlit.app/

---

## 📝 Proje Raporu ve Süreç

### 1. Problem Tanımı
Bankalar için yeni müşteri kazanmak, mevcut müşteriyi elde tutmaktan çok daha maliyetlidir. Bu projenin amacı, müşterilerin demografik ve finansal verilerini (kredi skoru, bakiye, yaş vb.) kullanarak bankayı terk etme olasılıklarını önceden tespit etmektir.

### 2. Veri Seti ve Hazırlık
Projede Kaggle'dan alınan "Churn Modelling" veri seti kullanılmıştır. Veri seti 10.000 satır ve 14 değişkenden oluşmaktadır.
- **Hedef Değişken:** `Exited` (1: Terk Etti, 0: Kaldı).

### 3. Baseline Model (Başlangıç)
Herhangi bir özellik mühendisliği yapılmadan, ham veri ile "Random Forest Classifier" algoritması kullanılarak bir temel model (baseline) kurulmuştur.
- **Baseline Accuracy:** %86.6
- **Baseline F1-Score (Churn Sınıfı):** 0.58

### 4. Feature Engineering (Özellik Mühendisliği)
Modelin "terk eden" müşterileri yakalama başarısını artırmak için veriden yeni anlamlı değişkenler türetilmiştir:
- `BalanceSalaryRatio`: Müşterinin bakiyesinin maaşına oranı.
- `TenureByAge`: Müşterinin yaşına göre bankada kaldığı yıl oranı.
- `CreditScoreGivenAge`: Kredi skorunun yaşa oranı.

### 5. Final Model ve Optimizasyon
Random Forest algoritması üzerinde `RandomizedSearchCV` kullanılarak hiperparametre optimizasyonu yapılmıştır. `class_weight` parametresi ile veri dengesizliği yönetilmiştir.
- **Final Model:** Random Forest (Optimize Edilmiş)
- **Final Accuracy:** %86.9
- **Final F1-Score:** 0.59
- **Validasyon Yöntemi:** %20 Test seti ayrılarak modelin genelleme başarısı ölçülmüştür.

### 6. İş Hedefleri ve Canlıya Alma (Business Impact & Deployment)
Final model, özellikle churn yakalama (F1-Score) konusunda baseline modele göre iyileştirme sağlamıştır. Model, **Streamlit** kullanılarak canlıya alınmış ve son kullanıcıların (banka çalışanlarının) anlık tahmin alabileceği bir arayüze dönüştürülmüştür.

Model canlıdayken izlenmesi gereken temel metrikler: **Recall (Duyarlılık)** ve **F1-Score**'dur. Yanlışlıkla "gidecek" denilen müşteriye promosyon vermek, giden müşteriyi kaçırmaktan daha az maliyetlidir.

---

## 📂 Repo Yapısı
```text
Bank-Churn-Projesi/
├── app.py                      # Streamlit dağıtım kodu (Deployment)
├── churn_model.pkl             # Eğitilmiş final model dosyası
├── requirements.txt            # Gerekli kütüphaneler
├── data/
│   └── Churn_Modelling.csv     # Ham veri seti
└── notebooks/
    ├── 1_EDA_Churn_Analizi.ipynb               # Veri analizi
    ├── 2_Baseline_Model.ipynb                  # Temel model kurulumu
    └── 3_Feature_Engineering_Optimization.ipynb # Final model ve iyileştirmeler
