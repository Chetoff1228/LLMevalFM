<div align="center">
  <a href="https://github.com/Chetoff1228/LLMevalFM/blob/hw_4">
    <img src="https://github.com/Chetoff1228/LLMevalFM/blob/hw_4/extensions/views/logo_eng.png" alt="LLMevalFM">
  </a>
</div>

# LLMevalFM: Framework for Evaluating Large Language Models

[LLMevalFM](https://github.com/Chetoff1228/LLMevalFM) is a framework designed to assess the factual accuracy of large language models (LLMs) within the Russian context.

## Description

LLMevalFM evaluates LLMs by measuring their performance on Russian-centric datasets, including culturally, geographically, and politically sensitive topics. The goal is to provide researchers and developers with tools for benchmarking and improving model accuracy in real-world scenarios.

### Key Features

- **SLAVA Dataset**: A comprehensive collection of Russian sociopolitical questions. [Dataset Link](https://huggingface.co/datasets/RANEPA-ai/SLAVA-OpenData-2800-v1)
- **Accuracy Metrics**: Includes multiple tools to measure and analyze the factuality of LLM-generated answers.
- **Leaderboard**: Allows easy comparison of model performances to identify top-performing solutions.

---

## Installation

### Prerequisites
- Python 3.10+
- Poetry for dependency management

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Chetoff1228/LLMevalFM.git
   cd LLMevalFM
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. Explore the functionality through notebooks in the `notebooks` folder.


---

## Repository Structure

```plaintext
LLMevalFM/
├── README.md                      # Project description
├── LICENSE                        # License file
├── pyproject.toml                 # Poetry configuration
├── poetry.lock                    # Dependency lock file
├── slava/
│   ├── __init__.py
│   ├── config.py                  # Configuration settings
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── data_loader.py         # Data loading utilities
│   │   ├── compute_metrics.py     # Accuracy metric calculations
│   │   ├── evaluate.py            # Evaluation logic
│   │   ├── leaderboard.py         # Leaderboard generation
│   │   └── utils/
│   │       ├── class_metrics.py   # Metrics logic
│   │       └── metrics_utils.py   # Helper functions
│   ├── notebooks/
│       ├── __init__.py
│       ├── data_loader.ipynb      # Example for loading datasets
│       ├── metrics.ipynb          # Accuracy metrics demonstration
│       └── evaluation.ipynb       # Evaluation examples
└── tests/                         # Test scripts
```

---

## Contribution

We welcome contributions to LLMevalFM! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/<feature_name>
   ```
3. Submit a pull request with your changes.

---

## Contact

📧 For inquiries or suggestions: **chetvergov-as@ranepa.ru**

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
```

**Что изменено:**
1. **Адаптирован текст описания** для краткости и удобочитаемости.
2. Добавлена структура фреймворка, включая ключевые файлы и функции.
3. Упрощен процесс установки и использования.
4. Указаны базовые шаги для выполнения оценки и генерации метрик.