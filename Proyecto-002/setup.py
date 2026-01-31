"""Setup configuration for Task Manager."""

from setuptools import setup, find_packages
import os

# Intentar leer README.md si existe
long_description = "Sistema de Gestión de Tareas - Proyecto CI/CD"
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="task-manager",
    version="1.0.0",
    author="Erick Medardo Alpusig",
    description="Sistema de Gestión de Tareas - Proyecto CI/CD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],
)
