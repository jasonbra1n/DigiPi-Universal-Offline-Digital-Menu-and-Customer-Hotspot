# 🤝 Contributing to DigiPi

We're excited you're interested in contributing to the DigiPi project! This guide will help you get started.

## Code of Conduct

By participating in this project, you are expected to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

### 🐛 Reporting Bugs

If you find an issue, please submit a bug report on our GitHub Issues page. Before submitting, please:
1.  **Check existing issues** to see if the bug has already been reported.
2.  Provide a **clear and descriptive title**.
3.  Include **steps to reproduce** the bug.
4.  Specify the **environment** (e.g., Raspberry Pi 4, OS version, browser used).

### ✨ Suggesting Features

We welcome new feature ideas! Please open a discussion or an issue with the label `enhancement` and describe:
1.  **The goal** of the new feature.
2.  **Why it is needed** (e.g., "It will improve provisioning reliability").
3.  Any **design considerations** (e.g., "This must be done without an internet connection").

## Development Setup

1.  **Fork the Repository:** Click the 'Fork' button at the top right of this repository.
2.  **Clone your Fork:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/DigiPi](https://github.com/YOUR_USERNAME/DigiPi)
    cd DigiPi
    ```
3.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏗️ Making Changes

1.  **Create a Branch:** Create a branch for your feature or bug fix.
    ```bash
    git checkout -b feature/my-awesome-feature
    ```
2.  **Code:** Make your changes in the `src/` directory.
3.  **Test:** Ensure your code works as expected and doesn't introduce regressions.
4.  **Commit:** Write clear, concise commit messages.
    ```bash
    git commit -m "feat: Add new multi-display config tab to admin panel"
    ```
5.  **Push:** Push your changes to your fork.
    ```bash
    git push origin feature/my-awesome-feature
    ```
6.  **Pull Request (PR):** Open a Pull Request from your fork to the `main` branch of the original repository. Please reference any related issues in your PR description.

Thank you for contributing to the future of DigiPi!
