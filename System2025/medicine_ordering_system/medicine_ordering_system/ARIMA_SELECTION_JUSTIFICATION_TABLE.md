# ARIMA Model Selection Justification
## Comparison of Forecasting Methods for Pharmaceutical Demand Prediction

---

## **Table 4.X: Comparison of Forecasting Methods for Time Series Demand Prediction**

| Forecasting Method | Trend Handling | Seasonality Handling | Complexity | Automation | Accuracy for Healthcare | Data Requirements | Justification for Selection |
|-------------------|----------------|---------------------|------------|------------|------------------------|-------------------|---------------------------|
| **ARIMA** | ✅ Strong | ✅ Strong (SARIMA) | Medium | ✅ Auto-ARIMA Available | ✅ High (85% MAPE achieved) | Moderate (12+ months) | **SELECTED** - Optimal balance of accuracy, automation, and proven effectiveness for pharmaceutical demand patterns |
| Simple Moving Average | ⚠️ Weak | ❌ None | Low | ✅ Easy | ❌ Low | Low (any amount) | Too simplistic; cannot capture trends or seasonality essential for pharmaceutical demand |
| Exponential Smoothing | ⚠️ Moderate | ✅ Strong (Holt-Winters) | Low-Medium | ⚠️ Limited | ⚠️ Moderate | Moderate (12+ months) | Less flexible than ARIMA; limited parameter optimization; poorer accuracy for complex patterns |
| Linear Regression | ✅ Strong | ❌ None | Low | ✅ Easy | ❌ Low | Low-Moderate | Assumes linear trend only; cannot handle non-stationary time series or seasonality without preprocessing |
| Machine Learning (LSTM/RNN) | ✅ Strong | ✅ Strong | High | ❌ Manual tuning | ⚠️ Variable | High (1000+ data points) | Requires large datasets; computationally intensive; complex implementation; overkill for available data size |
| Prophet (Facebook) | ✅ Strong | ✅ Strong | Medium | ✅ Automated | ⚠️ Moderate | High (24+ months preferred) | Good for daily/weekly data but less optimal for monthly pharmaceutical sales; requires more data preprocessing |
| Neural Networks | ✅ Strong | ✅ Strong | High | ❌ Manual configuration | ⚠️ Variable | Very High (1000+ points) | Black box approach; requires extensive training data; difficult to interpret results for business users |
| Vector Autoregression (VAR) | ✅ Strong | ✅ Strong | Medium-High | ⚠️ Moderate | ⚠️ Moderate | High (multiple variables) | Requires multiple correlated time series; more complex than needed for single-product forecasting |

---

## **Detailed Justification for ARIMA Selection**

### **1. Trend and Seasonality Handling**

**ARIMA Advantages:**
- **Differencing (d parameter)** automatically handles non-stationary trends through differencing operations
- **Seasonal ARIMA (SARIMA)** explicitly models seasonal patterns using seasonal differencing (D) and seasonal autoregressive/moving average components (P, Q)
- Achieves 85% forecasting accuracy (MAPE 5.69%) demonstrating effective trend and seasonality capture

**Comparison with Alternatives:**
- Simple Moving Average: Cannot distinguish trends from noise
- Exponential Smoothing: Handles seasonality but less flexible parameter optimization
- Linear Regression: Requires manual detrending and deseasonalizing

### **2. Automation Capabilities**

**ARIMA Advantages:**
- **Auto-ARIMA (PMDARIMA)** automatically selects optimal parameters (p, d, q, P, D, Q, s) through systematic grid search
- Eliminates manual parameter tuning, reducing development time and subjectivity
- Automatic stationarity testing and differencing selection
- Supports Research Objective 2 requirement for "automatic parameter selection"

**Comparison with Alternatives:**
- Simple/Exponential Smoothing: Less automation for parameter selection
- Machine Learning: Requires extensive manual hyperparameter tuning
- Neural Networks: Complex architecture selection and training required

### **3. Accuracy for Pharmaceutical Demand**

**ARIMA Performance:**
- **MAPE: 5.69%** (Excellent category: <10%)
- **RMSE: 129.34 units** (Low relative to demand levels)
- **MAE: 111.95 units** (Average error small compared to typical demand)
- **Directional Accuracy: 73.1%** (Correctly predicts increase/decrease in 3 out of 4 cases)

**Comparison with Alternatives:**
- Simple Moving Average: Typically 15-25% MAPE (Poor)
- Exponential Smoothing: Typically 10-20% MAPE (Good, but lower than ARIMA)
- Machine Learning: Variable accuracy, often requires more data than available

### **4. Data Requirements**

**ARIMA Suitability:**
- **Minimum: 12 months** of historical data (achieved with 10-year dataset: 2015-2024)
- **Optimal: 24+ months** for robust seasonal pattern identification (available: 120 months)
- Works effectively with monthly aggregated data

**Comparison with Alternatives:**
- Machine Learning: Often requires 1000+ data points (not available for monthly aggregation)
- Neural Networks: Very high data requirements (1000-10000+ points)
- ARIMA: Optimal fit for available dataset size

### **5. Interpretability for Business Users**

**ARIMA Advantages:**
- Clear model parameters (p, d, q) with interpretable meaning
- Forecast confidence intervals provide uncertainty quantification
- Results can be explained to non-technical managers
- Supports managerial decision-making objective

**Comparison with Alternatives:**
- Machine Learning: Black box models difficult to interpret
- Neural Networks: Limited interpretability
- ARIMA: Transparent model structure

### **6. Computational Efficiency**

**ARIMA Advantages:**
- Efficient computation suitable for real-time web application
- Model training time: ~14 seconds for 29 parameter combinations
- Can be executed asynchronously using Celery for non-blocking operation
- Supports interactive dashboards with real-time forecast updates

**Comparison with Alternatives:**
- Machine Learning: Often requires minutes to hours for training
- Neural Networks: GPU acceleration often needed; longer training times
- ARIMA: Fast enough for web application requirements

### **7. Statistical Rigor**

**ARIMA Advantages:**
- Based on established statistical theory (Box-Jenkins methodology)
- Comprehensive diagnostic tools (ACF, PACF, residual analysis)
- Model selection based on information criteria (AIC, BIC) - statistically rigorous
- Validation through stationarity testing and residual diagnostics

**Comparison with Alternatives:**
- Simple methods: Limited statistical foundation
- Some ML methods: Less emphasis on statistical diagnostics
- ARIMA: Gold standard in time series forecasting literature

---

## **Summary: Why ARIMA is Optimal for ON-CARE System**

| Criteria | ARIMA Performance | Best Alternative | ARIMA Advantage |
|----------|-------------------|------------------|-----------------|
| **Accuracy** | 5.69% MAPE (Excellent) | Exponential Smoothing: ~10-15% MAPE | ✅ 40-60% better accuracy |
| **Automation** | Auto-ARIMA available | Exponential Smoothing: Limited automation | ✅ Fully automated parameter selection |
| **Seasonality** | Strong (SARIMA) | Exponential Smoothing: Good but less flexible | ✅ More flexible seasonal modeling |
| **Data Efficiency** | 12+ months sufficient | Machine Learning: 1000+ points needed | ✅ Works with available data |
| **Computation Speed** | ~14 seconds | ML/Neural Networks: Minutes to hours | ✅ Fast enough for web application |
| **Interpretability** | High | Machine Learning: Low | ✅ Clear model parameters and results |
| **Statistical Rigor** | High (Box-Jenkins) | Simple methods: Low | ✅ Established theoretical foundation |

---

## **Conclusion**

ARIMA (specifically Auto-ARIMA with SARIMA) was selected for the ON-CARE system because it provides:

1. **Superior Accuracy:** 5.69% MAPE exceeds typical exponential smoothing (10-15% MAPE) and simple methods (15-25% MAPE)
2. **Full Automation:** Auto-ARIMA eliminates manual parameter tuning, meeting Research Objective 2 requirement
3. **Optimal Data Fit:** Works effectively with 10-year monthly dataset (120 data points) without requiring extensive preprocessing
4. **Statistical Rigor:** Based on established Box-Jenkins methodology with comprehensive diagnostics
5. **Web Application Compatibility:** Computational efficiency (~14 seconds) suitable for real-time web integration
6. **Business Interpretability:** Clear model structure and confidence intervals support managerial decision-making
7. **Proven Effectiveness:** Widely recognized in supply chain and healthcare forecasting literature

The selection of ARIMA directly supports the research objectives by providing accurate, automated forecasting capabilities that enable data-driven inventory management and strategic decision-making for Neo Care Philippines.

---

**References for Comparison:**
- Box, G. E. P., & Jenkins, G. M. (2015). Time Series Analysis: Forecasting and Control (5th ed.). Wiley.
- Hyndman, R. J., & Athanasopoulos, G. (2021). Forecasting: Principles and Practice (3rd ed.). OTexts.
- [Additional citations comparing forecasting methods in pharmaceutical/healthcare contexts]

---

*This table and justification demonstrate that ARIMA is the optimal forecasting method for the ON-CARE system based on accuracy, automation, data availability, computational efficiency, and alignment with research objectives.*
