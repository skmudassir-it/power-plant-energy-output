# ⚡ Power Plant Energy Output Prediction

> Machine Learning model to predict net hourly electrical energy output of a Combined Cycle Power Plant.

**🎉 New modern frontend available:**

### 👉 [power-plant-frontend-ten.vercel.app](https://power-plant-frontend-ten.vercel.app)

The new version features:
- 🎨 Beautiful dark-themed UI with animated energy gauge
- 🧠 ML model runs directly in the browser (no backend needed!)
- 📊 Decision Tree Regressor with 127 nodes, max depth 6
- ⚡ Instant predictions — no API calls, no latency
- 📱 Fully responsive design
- Built with Next.js 16 + Framer Motion + Tailwind CSS

**Source:** [github.com/skmudassir-it/power-plant-frontend](https://github.com/skmudassir-it/power-plant-frontend)

---

## Dataset

The dataset contains **9,568 data points** collected from a Combined Cycle Power Plant over 6 years (2006-2011).

**Features:**
| Feature | Range |
|---|---|
| Temperature (T) | 0°C – 40°C |
| Exhaust Vacuum (V) | 20 – 85 cm Hg |
| Ambient Pressure (AP) | 900 – 1100 milibar |
| Relative Humidity (RH) | 0 – 100% |

**Target:** Net hourly electrical energy output (EP) in MW

---

## Old Version (Flask)

```bash
pip install -r requirements.txt
python app.py
```

---

*Developed by Mudassir Shaik*
