Thank you for your interest in contributing to this project!

Guidelines
- Please open an issue before starting work on a non-trivial change so we can discuss the approach.
- Keep changes small and focused. One feature / fix per pull request.
- Write clear commit messages and include a short description in the PR.

Development workflow
1. Fork the repository and create a feature branch from `main`:

```bash
git checkout -b feature/my-change
```

2. Run the dev server and verify changes locally:

```powershell
.\.venv\Scripts\Activate.ps1
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py runserver
```

3. Run checks (the CI also runs these):

```powershell
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python manage.py check
```

4. Push your branch to your fork and open a pull request against `lekalderonicky/portfolio:main`.

Code style
- Keep code readable. Prefer small functions and clear variable names.
- Add tests for non-trivial logic. This project uses Django's standard test runner.

Thank you — maintainers will review PRs and provide feedback.
