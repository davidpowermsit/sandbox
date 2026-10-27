# sandbox

A place to write and test snippets of code

## Projects

The sandbox contains three independent projects, each in its own subpackage with a matching test folder:

| Project      | Source                     | Tests               | Run with                  |
| ------------ | -------------------------- | ------------------- | ------------------------- |
| Anagram finder | `src/sandbox/anagram/`   | `tests/anagram/`    | `uv run anagrams`         |
| Calculator   | `src/sandbox/calculator/`  | `tests/calculator/` | `uv run calculator`       |
| Scrapbook    | `src/sandbox/scrapbook/`   | `tests/scrapbook/`  | (snippets, tests only)    |

```text
src/sandbox/
├── anagram/
├── calculator/
└── scrapbook/
tests/
├── anagram/
├── calculator/
└── scrapbook/
```

To add a new project, create `src/sandbox/<name>/` (with an `__init__.py`) and `tests/<name>/`.
Test file names must be unique across projects (e.g. `test_<name>.py`).

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:davidpowermsit/sandbox.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.
