# How to install robotstxtpy. run: 
pip install --extra-index-url https://test.pypi.org/simple/ robotstxt==0.0.3
run robotstxt to generate robots.txt in the current directory
run crawler to to generate robots.txt with Disallow for all endpoints 

### Install pre-commit

We use `pre-commit` to run linters and formatters before each commit. To setup `pre-commit`, please follow these steps:

```bash
$ pip install pre-commit
$ pre-commit install
```

### Install CLIs

To interact with the library functions directly, there are CLI's for this.
```bash
pip install -e .
```

The two CLI's available so far are `robotstxt` and `crawler`
