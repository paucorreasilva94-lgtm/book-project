# book-project
Book project
# Book Recommendation Engine

A content-based recommendation system that leverages Machine Learning, NLP, and clustering techniques to provide personalized book suggestions.

## 🎯 Mission and Objectives
**Mission:** To democratize literary discovery by connecting readers with books that authentically resonate with their interests through accessible, data-driven technology.

**Objective:** To build an interactive, AI-powered web tool that uses semantic analysis and clustering to provide personalized, relevant book recommendations in real-time.

## 🚀 Key Features
* **Data Sanitization:** Automated NLP pipeline to clean raw web-scraped data (removing HTML tags, special characters, and standardizing text).
* **TF-IDF Vectorization:** Converts book descriptions into mathematical vectors to capture semantic context.
* **K-Means Clustering:** Segments the catalog into 10 thematic clusters to improve recommendation precision and search efficiency.
* **Similarity Engine:** Uses Cosine Similarity to identify thematic matches within clusters.
* **Interactive Interface:** Deployed as a web application using **Streamlit** for a seamless user experience.



## 🛠 Tech Stack
* **Language:** Python 3.x
* **Machine Learning:** `scikit-learn` (KMeans, TfidfVectorizer, Cosine Similarity)
* **Web Framework:** `Streamlit`
* **Data Handling:** `pandas`, `joblib`
* **Environment:** Anaconda / Conda

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
