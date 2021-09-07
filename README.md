# CI-and-unit-test-on-python  

Is my teach project, oriented on learning GitHub Actions and work with CI in GitHub.
  
## Simple math programm on Python  
Running the programm with the following command:  

```python3 main.py```  

main.py contains the ```class Calculator```, which can do simple ariphmectics operations, and the ```def array_sum```, which finds the sum of the numbers in an array. ```class Circle``` contains simple ariphmetic operation with circle.

## Unit Testing with Python

Running the unit tests with the following command:

```python3 test.py```

test.py imports the generated calculator and unittest module needed to set up and run tests, as well as the array_sum function.

## Parametrized tests show in pytest dir
To run the tests, first start the web server, this can be done through the IDE or using the command line 

```flask run```   [docs](https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing)

Next, install deps and run the tests

```
pip -r install requirements.txt
python3 pytest/tests/test_math.py -m pytest
```
