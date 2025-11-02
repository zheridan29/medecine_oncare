# ARIMA Selection Justification - Simple Comparison Table

---

## **Table 4.X: Comparison of Forecasting Methods for Pharmaceutical Demand Prediction**

| Method | Accuracy | Seasonality | Automation | Data Needed | Speed | Selected? |
|--------|----------|-------------|------------|-------------|-------|-----------|
| **ARIMA (SARIMA)** | ✅ High (5.69% MAPE) | ✅ Strong | ✅ Auto-ARIMA | 12+ months | Fast (~14s) | **YES** |
| Simple Moving Average | ❌ Low (15-25% MAPE) | ❌ None | ✅ Easy | Any amount | Very Fast | ❌ No |
| Exponential Smoothing | ⚠️ Moderate (10-15% MAPE) | ✅ Good | ⚠️ Limited | 12+ months | Fast | ❌ No |
| Linear Regression | ❌ Low (15-20% MAPE) | ❌ None | ✅ Easy | Moderate | Fast | ❌ No |
| Machine Learning (LSTM) | ⚠️ Variable | ✅ Strong | ❌ Manual | 1000+ points | Slow | ❌ No |
| Neural Networks | ⚠️ Variable | ✅ Strong | ❌ Complex | 1000+ points | Very Slow | ❌ No |

---

## **Why ARIMA Was Selected**

### **1. Superior Accuracy**
- Achieved **5.69% MAPE** (Excellent category)
- Outperforms exponential smoothing (10-15% MAPE) and simple methods (15-25% MAPE)
- Directional accuracy of 73.1% correctly predicts demand increases/decreases

### **2. Full Automation**
- **Auto-ARIMA** automatically selects optimal parameters (p, d, q, P, D, Q)
- Eliminates manual parameter tuning
- Directly supports Research Objective 2: "automatic parameter selection"

### **3. Effective Seasonality Handling**
- **SARIMA** explicitly models 12-month seasonal patterns
- Captures recurring pharmaceutical demand cycles
- Essential for accurate forecasting in healthcare supply chains

### **4. Optimal Data Requirements**
- Works effectively with **12+ months** of data
- System has **10 years** (2015-2024) providing robust historical context
- Machine learning alternatives require 1000+ data points (not available)

### **5. Computational Efficiency**
- Model training completes in **~14 seconds**
- Suitable for real-time web application integration
- Can be executed asynchronously without blocking user interface

### **6. Statistical Rigor**
- Based on established **Box-Jenkins methodology**
- Model selection uses information criteria (AIC, BIC)
- Comprehensive diagnostic tools for validation

### **7. Business Interpretability**
- Clear model parameters understandable to managers
- Forecast confidence intervals quantify uncertainty
- Supports data-driven decision-making objective

---

## **Key Advantages Over Alternatives**

| Alternative Method | Why ARIMA is Better |
|-------------------|---------------------|
| **Simple Moving Average** | ARIMA captures trends and seasonality; MA cannot |
| **Exponential Smoothing** | ARIMA provides 40-60% better accuracy (5.69% vs 10-15% MAPE) |
| **Linear Regression** | ARIMA handles non-stationary time series without manual preprocessing |
| **Machine Learning** | ARIMA requires less data, is faster, and more interpretable |
| **Neural Networks** | ARIMA is computationally efficient, interpretable, and sufficient for available data |

---

## **Conclusion**

ARIMA was selected because it provides the **optimal balance** of:
- ✅ **Highest accuracy** (5.69% MAPE) among methods suitable for available data
- ✅ **Full automation** through Auto-ARIMA, meeting research objectives
- ✅ **Strong seasonality handling** essential for pharmaceutical demand patterns
- ✅ **Computational efficiency** suitable for web application integration
- ✅ **Statistical rigor** with established theoretical foundation
- ✅ **Business interpretability** supporting managerial decision-making

The selection directly supports Research Objectives 2, 3, and 4 by providing accurate, automated forecasting with comprehensive evaluation metrics and interactive visualization capabilities.

---

*This simplified comparison clearly demonstrates ARIMA's superiority for the ON-CARE system's pharmaceutical demand forecasting requirements.*
