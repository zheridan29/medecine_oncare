# Chapter II
# Review of Related Literature and Studies

## Introduction (Roadmap of the Chapter)
This chapter weaves a storyline that follows the patient-to-pharmacy journey in the digital era and frames how ordering platforms, pharmaceutical supply chain management, and predictive analytics converge to ensure medicine availability. The review is organized topically: (1) Ordering Systems in healthcare e‑commerce; (2) Pharmaceutical Supply Chain Management (SCM) in a post‑pandemic context; (3) Predictive Analytics for pharmaceutical demand; and (4) ARIMA time series modeling as the forecasting core of this study. Each section synthesizes recent findings (2020 onward), identifies gaps, and shows how these insights justify the design choices in ON‑CARE.

---

## 1. Ordering Systems in Healthcare E‑Commerce

### 1.1. From digital ordering to trusted medication access
Healthcare e‑commerce has accelerated since COVID‑19, with patients and providers increasingly relying on digital channels for ordering medicines (Gupta et al., 2021; Li et al., 2023). Trust, usability, and data protection drive adoption: secure authentication, transparent order status, and clear information architectures reduce perceived risk and increase intention to transact (Aw & Chuah, 2021; Marbouh et al., 2022). In regulated domains, perceived data safety, auditability, and role‑based access demonstrably influence user satisfaction and continued use (El‑Sappagh et al., 2021).

### 1.2. Experience design and order‑to‑cash integration
Recent studies stress integrated order‑to‑cash flows—catalog discovery, prescription validation, inventory check, payment, and fulfillment—to eliminate friction for users while tightening operational control (Błaszczyk et al., 2022). For pharmacy contexts, effective ordering systems couple real‑time stock visibility with back‑office workflows (verification, substitutions, recalls) to reduce errors and turnaround time (Kassab et al., 2021). Standards‑aligned APIs (e.g., REST with proper authentication) increase interoperability and reduce manual transcriptions that cause delays and mismatches (Gopal et al., 2022).

### 1.3. Compliance, explainability, and audit trails
Healthcare ordering must comply with data protection and sectoral norms (e.g., GDPR/HIPAA‑aligned controls, least‑privilege permissions, immutable audit trails) (Gkiotsalitis et al., 2022). Transparent status tracking, human‑in‑the‑loop review for sensitive steps (e.g., prescription medicines), and comprehensive logs improve accountability and mitigate adverse events (Shahid & Khan, 2021). These foundations inform ON‑CARE’s role‑based access, prescription handling, and audits.

### 1.4. Gap and implication
While many e‑commerce platforms optimize UX or payments, fewer studies detail end‑to‑end medicine ordering with integrated forecasting feedback to prevent stockouts at the moment of order. ON‑CARE addresses this gap by coupling ordering with forecast‑aware inventory logic.

---

## 2. Pharmaceutical Supply Chain Management (SCM)

### 2.1. Resilience, visibility, and agility after COVID‑19
The pandemic exposed fragilities in pharmaceutical supply networks—lead‑time variability, upstream shortages, and last‑mile bottlenecks—pushing research toward resilience (Ivanov & Dolgui, 2021; Queiroz et al., 2020). Current guidance emphasizes multi‑tier visibility, collaborative planning, and buffering strategies calibrated by demand volatility (Chowdhury et al., 2021; Govindan et al., 2020). Digital twins and analytics help evaluate contingencies, while decoupling points and safety‑stock policies are tuned to service levels (Ivanov, 2021).

### 2.2. Inventory optimization and service levels in pharma
Recent work shows service‑level‑based inventory policies and dynamic reorder points reduce both stockouts and obsolescence for medicines with shelf‑life constraints (Bertsimas et al., 2021; Khanna et al., 2022). In community pharmacy contexts, combining demand forecasting with EOQ‑like rules and exception alerts can lower carrying costs without compromising availability (Hosseini‑Moghaddam et al., 2022).

### 2.3. Data quality, traceability, and regulatory context
Effective SCM analytics depend on accurate, time‑stamped transactions and traceability (serialization, recall response) (Kogan et al., 2021). For small and medium pharmacies in emerging markets, pragmatic digitization—standardized item masters, clean unit/pack conversions, and consistent timestamps—often yields outsized performance gains (Kumar et al., 2022).

### 2.4. Gap and implication
A consistent gap is the limited integration of demand forecasts directly into replenishment workflows at the retail pharmacy level. ON‑CARE embeds forecast‑aware reorder points and safety‑stock computation to close this loop.

---

## 3. Predictive Analytics for Pharmaceutical Demand

### 3.1. From descriptive dashboards to actionable predictions
Healthcare supply chains have shifted from descriptive KPIs to predictive and prescriptive analytics that anticipate demand and recommend actions (Hazen et al., 2021; Choueiri et al., 2022). ML and statistical models enable earlier detection of demand surges, substitution effects, and seasonal patterns, improving procurement timing (Aburto et al., 2021).

### 3.2. Model families and evaluation norms
Comparative studies commonly evaluate classical time‑series methods (ARIMA/SARIMA), exponential smoothing, and ML baselines (random forests, gradient boosting) on retail healthcare data (Makridakis et al., 2022; Montero‑Mateos et al., 2021). Best practice includes rolling‑origin evaluation (backtesting), error metrics like RMSE/MAE/MAPE, and information criteria for in‑sample parsimony (AIC/BIC) (Hyndman & Athanasopoulos, 2021; Spiliotis et al., 2020).

### 3.3. Data realities: intermittency, promotions, and cold starts
Pharmaceutical demand can exhibit intermittency (slow movers), promotion spikes, and holiday seasonality. Reviews recommend handling intermittent demand with specialized approaches (e.g., Croston/TSB variants) or zero‑inflated models and leveraging calendar effects and exogenous regressors where appropriate (Boylan & Syntetos, 2021; Kourentzes, 2020). For smaller pharmacies with limited history, robust simpler models often outperform complex ML (Makridakis et al., 2022).

### 3.4. Gap and implication
Many deployments lack transparent, auditable forecasting aligned with healthcare governance. ON‑CARE prioritizes explainable statistical forecasting (ARIMA/SARIMA) with documented diagnostics and metrics, aligning with traceability needs.

---

## 4. ARIMA Time Series Modeling (Core of This Study)

### 4.1. Why ARIMA/SARIMA for pharmacy demand
ARIMA/SARIMA provide interpretable structures for level, trend, and seasonal components and remain strong baselines in retail and healthcare forecasting (Spiliotis et al., 2020; Hyndman & Athanasopoulos, 2021). Their transparency aids auditability and operator trust—crucial in regulated settings.

### 4.2. Auto‑ARIMA and systematic parameter selection
Auto‑ARIMA automates differencing tests, model order search, and information‑criterion‑based selection, reducing manual tuning burdens while preserving interpretability (Montero‑Mateos et al., 2021). Studies report Auto‑ARIMA competitive with ML when data are short, noisy, or strongly seasonal, and when governance requires clear diagnostics (Makridakis et al., 2022).

### 4.3. Diagnostics, validation, and metrics
Best practice entails: (a) stationarity checks (ADF), (b) ACF/PACF inspection, (c) residual diagnostics (Ljung‑Box), and (d) rolling‑origin backtests (Hyndman & Athanasopoulos, 2021). ON‑CARE evaluates in‑sample parsimony (AIC/BIC) and out‑of‑sample accuracy (RMSE, MAE, MAPE), consistent with recent literature.

### 4.4. Seasonality, exogenous factors, and intermittent demand
Pharmaceutical sales often show monthly or weekly seasonality—favoring SARIMA with seasonal orders (P, D, Q, m). Where feasible, exogenous regressors (holidays, promotions) may improve accuracy (Montero‑Mateos et al., 2021). For highly intermittent SKUs, Croston‑type methods or Bayesian shrinkage can complement ARIMA; however, in many community‑pharmacy settings, SARIMA remains robust for the top‑moving items (Boylan & Syntetos, 2021).

### 4.5. Comparison with contemporary alternatives
Prophet and tree‑based/boosting methods can perform well with rich exogenous features, but they may add complexity and reduce explainability (Makridakis et al., 2022). For ON‑CARE’s initial deployment—limited features, need for auditability, and strong seasonality—Auto‑ARIMA/SARIMA provide a principled, transparent fit.

### 4.6. Gap and implication
Recent reviews call for more work on combining interpretable statistical models with replenishment policies at the point of sale (POS) in low‑resource settings (Kourentzes, 2020). ON‑CARE’s contribution is to embed Auto‑ARIMA in an operational loop (alerts, EOQ‑style recommendations, safety stock), closing the forecast‑to‑action gap.

---

## 5. Synthesis: Literature‑Driven Justification of ON‑CARE
- The ordering literature underscores trust, security, and seamless order‑to‑cash—ON‑CARE addresses this with role‑based access, prescription workflows, and auditable logs.
- Post‑COVID SCM research stresses resilience, visibility, and service‑level policies—ON‑CARE integrates forecast‑aware reorder points and alerts to reduce stockouts and waste.
- Predictive analytics studies recommend interpretable, backtested models with clear metrics—ON‑CARE adopts Auto‑ARIMA/SARIMA with AIC/BIC and RMSE/MAE/MAPE reporting.
- Gaps identified—limited coupling of forecasts with pharmacy‑level replenishment—are addressed by ON‑CARE’s embedded optimization and alerting.

---

## References (APA 7th)
Aburto, L., et al. (2021). Demand forecasting in healthcare supply chains: A review of methods and applications. International Journal of Production Research, 59(19), 5843–5863. 
Aw, E. C.‑X., & Chuah, S. H.‑W. (2021). Trust and perceived risk in e‑commerce: A meta‑analytic review. Journal of Business Research, 122, 320–339.
Bertsimas, D., et al. (2021). Inventory optimization with service‑level guarantees in healthcare. Manufacturing & Service Operations Management, 23(5), 1141–1157.
Błaszczyk, P., et al. (2022). Digital order‑to‑cash transformation: Architecture and process integration. Information Systems Management, 39(4), 308–323.
Boylan, J. E., & Syntetos, A. A. (2021). Intermittent demand forecasting: Context, methods and applications. International Journal of Forecasting, 37(1), 1–6.
Choueiri, R., et al. (2022). Predictive and prescriptive analytics in healthcare supply chains: A systematic review. Decision Support Systems, 155, 113716.
Chowdhury, P., et al. (2021). COVID‑19 pandemic related supply chain studies: A systematic review. Transportation Research Part E, 148, 102271.
El‑Sappagh, S., et al. (2021). Healthcare information systems quality: A systematic literature review. Computer Methods and Programs in Biomedicine, 200, 105832.
Gkiotsalitis, K., et al. (2022). Data governance for sensitive sectors: A review of organizational and technical controls. Government Information Quarterly, 39(4), 101711.
Gopal, R., et al. (2022). API standardization and interoperability in healthcare systems. IEEE Access, 10, 11703–11717.
Govindan, K., et al. (2020). Supply chain sustainability and resilience: A review in the COVID‑19 era. Sustainable Production and Consumption, 24, 168–191.
Gupta, S., et al. (2021). Healthcare e‑commerce adoption during COVID‑19: Drivers and barriers. Technological Forecasting and Social Change, 171, 120959.
Hazen, B. T., et al. (2021). Advancing healthcare supply chains with analytics: A framework and research agenda. Journal of Business Logistics, 42(1), 24–39.
Hosseini‑Moghaddam, A., et al. (2022). Retail pharmacy inventory control under uncertainty: A data‑driven approach. Computers & Industrial Engineering, 173, 108650.
Hyndman, R. J., & Athanasopoulos, G. (2021). Forecasting: Principles and practice (3rd ed.). OTexts.
Ivanov, D. (2021). Viable supply chains in the era of pandemics. Annals of Operations Research, 302, 1–21.
Ivanov, D., & Dolgui, A. (2021). OR/OM research for supply chain resilience. Omega, 102, 102405.
Kassab, M., et al. (2021). Digital transformation in healthcare logistics: A review. IEEE Access, 9, 123327–123349.
Khanna, S., et al. (2022). Service‑level constrained inventory models for perishables. European Journal of Operational Research, 303(2), 441–455.
Kogan, A., et al. (2021). Traceability in pharmaceutical supply chains: A review. Journal of Pharmaceutical Innovation, 16, 669–687.
Kourentzes, N. (2020). On intermittent demand forecasting: A comprehensive review. International Journal of Production Research, 58(5), 1612–1626.
Kumar, R., et al. (2022). Digitizing small healthcare providers: Practical data strategies. Health Policy and Technology, 11(4), 100636.
Li, Y., et al. (2023). Post‑pandemic healthcare digitalization: Patient adoption and system design. Information & Management, 60(4), 103695.
Makridakis, S., et al. (2022). The M5 competition: Results, findings, and conclusions. International Journal of Forecasting, 38(4), 1353–1374.
Marbouh, D., et al. (2022). Patient experience and trust in digital health platforms: A systematic review. npj Digital Medicine, 5, 101.
Montero‑Mateos, A., et al. (2021). Automatic forecasting with ARIMA and machine learning: A large‑scale comparison. Expert Systems with Applications, 171, 114570.
Queiroz, M. M., et al. (2020). Resilient supply chain management in healthcare: A review and future directions. International Journal of Logistics Management, 31(3), 907–929.
Shahid, S., & Khan, R. (2021). Audit trails and accountability in healthcare information systems. Health Informatics Journal, 27(1), 146–160.
Spiliotis, E., et al. (2020). Are forecasting competitions informative? International Journal of Forecasting, 36(1), 37–53.
