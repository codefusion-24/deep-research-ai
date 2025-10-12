# 🤝 Contributing to Deep Research AI

First off, thank you for considering contributing to Deep Research AI! It's people like you that make this project better for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Expected Behavior

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers and help them get started
- ✅ Give and gracefully accept constructive feedback
- ✅ Focus on what is best for the community

### Unacceptable Behavior

- ❌ Harassment or discriminatory language
- ❌ Trolling or insulting comments
- ❌ Personal or political attacks
- ❌ Publishing others' private information

---

## 💡 How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Screenshots** (if applicable)
- **Environment details** (OS, Python version, etc.)

**Template**:
```markdown
**Bug Description**
A clear description of the bug.

**To Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment**
- OS: [e.g., Windows 10]
- Python: [e.g., 3.9.0]
- Browser: [e.g., Chrome 96]
```

### Suggesting Features

Feature requests are welcome! Please provide:

- **Clear description** of the feature
- **Use case**: Why is this needed?
- **Proposed solution**: How should it work?
- **Alternatives**: Other solutions you've considered

### Code Contributions

1. **Start Small**: Begin with small PRs (bug fixes, typos)
2. **Discuss First**: For major changes, open an issue first
3. **Follow Standards**: Adhere to our coding guidelines
4. **Write Tests**: Add tests for new features
5. **Update Docs**: Keep documentation current

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- Git
- Code editor (VS Code recommended)

### Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR-USERNAME/deep-research-ai.git
cd deep-research-ai

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL-OWNER/deep-research-ai.git
```

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Add your API keys to .env

# Run tests
python test_system.py

# Start development server
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend

# No build required! Just open in browser
python -m http.server 8080
```

### Running Tests

```bash
# Backend tests
cd backend
python test_system.py

# Check code style
flake8 .

# Type checking
mypy .
```

---

## 📝 Coding Standards

### Python (Backend)

**Style Guide**: PEP 8

```python
# Good
def calculate_confidence_score(sources: List[Dict]) -> float:
    """Calculate confidence score based on source frequency.
    
    Args:
        sources: List of source dictionaries
        
    Returns:
        Confidence score between 0 and 1
    """
    return sum(s.get('count', 0) for s in sources) / len(sources)

# Bad
def calcScore(s):
    return sum([x['count'] for x in s])/len(s)
```

**Key Rules**:
- ✅ Use type hints
- ✅ Write docstrings for functions
- ✅ Use meaningful variable names
- ✅ Keep functions small (< 50 lines)
- ✅ Use f-strings for formatting
- ✅ Add comments for complex logic

### JavaScript (Frontend)

**Style Guide**: Airbnb JavaScript Style Guide

```javascript
// Good
const handleResearch = async (query) => {
    if (!query.trim()) {
        setError('Please enter a query');
        return;
    }
    
    try {
        const result = await apiClient.post('/run', { query });
        setResult(result);
    } catch (error) {
        setError(error.message);
    }
};

// Bad
function handle(q){
    if(!q)return
    apiClient.post('/run',{query:q}).then(r=>setResult(r))
}
```

**Key Rules**:
- ✅ Use `const` and `let`, not `var`
- ✅ Use arrow functions
- ✅ Use async/await over promises
- ✅ Add PropTypes for components
- ✅ Use meaningful names
- ✅ Keep components small

### File Organization

```
backend/
├── main.py              # API routes
├── research_agent.py    # Core logic
├── query_decomposer.py  # Single responsibility
└── tests/              # Mirror structure
    └── test_agent.py

frontend/
├── js/
│   ├── app.js          # Main app
│   ├── components.js   # UI components
│   └── utils.js        # Helpers
```

---

## 🔄 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance

**Examples**:

```bash
# Good commits
git commit -m "feat(backend): add caching for search results"
git commit -m "fix(frontend): resolve progress bar animation issue"
git commit -m "docs(readme): update installation instructions"

# Bad commits
git commit -m "fixed stuff"
git commit -m "update"
git commit -m "asdfasdf"
```

### Branch Naming

```bash
# Feature
git checkout -b feature/add-caching

# Bug fix
git checkout -b fix/progress-bar-bug

# Documentation
git checkout -b docs/update-readme
```

---

## 🔀 Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation is updated
- [ ] Commits are clean and descriptive
- [ ] Branch is up-to-date with main

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Screenshots
If applicable, add screenshots

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No breaking changes
```

### Submitting PR

```bash
# 1. Commit your changes
git add .
git commit -m "feat: add amazing feature"

# 2. Push to your fork
git push origin feature/amazing-feature

# 3. Create PR on GitHub
# Go to GitHub and click "New Pull Request"
```

### Review Process

1. **Automated Checks**: CI/CD runs tests
2. **Code Review**: Maintainer reviews code
3. **Feedback**: Address review comments
4. **Approval**: Get approval from maintainer
5. **Merge**: PR is merged to main

**Response Time**: We aim to review PRs within 3-5 days.

---

## 🐛 Issue Guidelines

### Creating Issues

**Good Issue**:
```markdown
**Title**: Add export to PDF feature

**Description**: 
Users want to download research reports as PDF in addition to Markdown/JSON.

**Expected Behavior**:
Button to download PDF report with proper formatting.

**Proposed Solution**:
Use a library like ReportLab or WeasyPrint to generate PDFs.

**Additional Context**:
Similar to Markdown export but with better formatting for printing.
```

**Bad Issue**:
```markdown
Title: "bug"
Description: "doesn't work"
```

### Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature
- `documentation`: Documentation improvements
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `question`: Questions about the project

---

## 🧪 Testing Guidelines

### Writing Tests

```python
# backend/tests/test_decomposer.py

def test_query_decomposition():
    """Test that queries are properly decomposed"""
    decomposer = QueryDecomposer()
    result = decomposer.decompose("AI trends 2024")
    
    assert len(result['dimensions']) == 3
    assert all('queries' in d for d in result['dimensions'])
    assert result['total_searches'] == 9
```

### Test Coverage

- Aim for 70%+ coverage
- Test critical paths
- Include edge cases
- Test error handling

---

## 📚 Documentation

### Code Documentation

```python
def aggregate_results(self, results: List[Dict]) -> List[Dict]:
    """Aggregate and deduplicate search results.
    
    Uses Self-Consistency validation to identify high-confidence sources
    by checking if information appears multiple times across searches.
    
    Args:
        results: List of search results from multiple agents
        
    Returns:
        List of deduplicated results with confidence scores
        
    Example:
        >>> results = [{'url': 'example.com'}, {'url': 'example.com'}]
        >>> aggregated = self.aggregate_results(results)
        >>> aggregated[0]['confidence']
        2
    """
    # Implementation
```

### README Updates

When adding features, update:
- Features section
- Usage examples
- API documentation
- Configuration options

---

## 🎓 Learning Resources

### Python/FastAPI
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Asyncio](https://docs.python.org/3/library/asyncio.html)
- [Real Python Tutorials](https://realpython.com/)

### React
- [React Documentation](https://react.dev/)
- [JavaScript.info](https://javascript.info/)

### Git
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [GitHub Guides](https://guides.github.com/)

---

## 🏆 Recognition

Contributors will be:
- Listed in `CONTRIBUTORS.md`
- Mentioned in release notes
- Given credit in documentation

---

## ❓ Questions?

- **General Questions**: Open a [Discussion](https://github.com/AdiityaRaj/deep-research-ai/discussions)
- **Bug Reports**: Open an [Issue](https://github.com/AdiityaRaj/deep-research-ai/issues)
- **Direct Contact**: [rajaditya2424@gmail.com]

---

## 🎉 Thank You!

Every contribution makes a difference. Whether it's code, documentation, bug reports, or feature suggestions - we appreciate your help!

**Happy Contributing! 🚀**

---

*This contributing guide is adapted from open source best practices and will evolve as the project grows.*