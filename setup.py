import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyverify-xnz233",  # Replace with your own username
    version="1.0.0",
    author="xnz233",
    author_email="jl3362518@163.com",
    description="A small verify project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xnz233/pyverify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
