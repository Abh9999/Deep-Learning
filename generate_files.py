# Adding necessary project files for your Colab project.

# LICENSE File (MIT License)
LICENSE = """MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# README.md
README = """# Colab Project

## Description
This project contains code designed to run in Google Colab for [specific purpose].

## Features
- Feature 1: [Explain feature]
- Feature 2: [Explain feature]
- Feature 3: [Explain feature]

## Installation
Run the following commands in your terminal to set up:
```bash
# Clone the repository
git clone <repository-url>

# Install dependencies
pip install -r requirements.txt
```

## Usage
1. Open the Colab notebook.
2. Follow the provided instructions in the notebook cells.
3. Input your data or configurations as required.

## Contributing
Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License
This project is licensed under the [MIT License](LICENSE).
"""

# .gitignore
GITIGNORE = """# Byte-compiled files
*.pyc
*.pyo
__pycache__/

# Virtual environments
venv/
.env/

# Logs
*.log

# IDE files
.vscode/
.idea/

# Colab-specific files
.ipynb_checkpoints/
"""

# CONTRIBUTING.md
CONTRIBUTING = """# Contributing to Colab Project

We welcome contributions to improve this project. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add a meaningful commit message"
   ```
4. Push your changes:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request and describe your changes.

Thank you for contributing!
"""

# CODE_OF_CONDUCT.md
CODE_OF_CONDUCT = """# Code of Conduct

## Our Pledge
We are committed to fostering an open and welcoming environment. All contributors and participants are expected to maintain a respectful and inclusive attitude.

## Guidelines
- Be respectful to others.
- No harassment or discriminatory language.
- Report unacceptable behavior to [email@example.com].

## Enforcement
Instances of unacceptable behavior may be reported to the project maintainers for review and appropriate action.
"""

# CHANGELOG.md
CHANGELOG = """# Changelog

## [1.0.0] - 2025-01-26
- Initial release of the Colab project files.
"""

# Save files to the project folder
def save_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

save_file("LICENSE", LICENSE)
save_file("README.md", README)
save_file(".gitignore", GITIGNORE)
save_file("CONTRIBUTING.md", CONTRIBUTING)
save_file("CODE_OF_CONDUCT.md", CODE_OF_CONDUCT)
save_file("CHANGELOG.md", CHANGELOG)
