# Использовать black/flake8/isort на каждом файле, интегрировать в CI
# чтобы работало перед каждым коммитом
# добавить pyproject.toml
'''
[tool.black]
line-length = 88
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 88
'''
'''
- name: Lint with flake8
  run: python -m flake8 .
- name: Check formatting with black
  run: python -m black --check .
- name: Check import sorting with isort
  run: python -m isort --check-only .
'''