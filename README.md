# Overbond Dev Assessment

* Date Created: 11 06 2021

## Author

* Avinash Gazula, avinashgazula@gmail.com

## Prerequisites

* Install python 3
* Install Docker

## Run Instructions

* Clone the GitHub repository
* To run the script with python, run the command "python3 Benchmark.py sample_input.json sample_output.json" where sample_input.json is the relative path to the input file and sample_output.json is the relative path to the output file
* To run the test script with python, run the command "python3 BenchmarkTest.py sample_input.json sample_output.json" where sample_input.json is the relative path to the input file and sample_output.json is the relative path to the output file
* Build a docker image with "docker build -t docker-image ." where docker-image is the name of the docker image
* To run the docker, run it with "docker run -v ${PWD}:/submission docker-image". Mount the host path with the container path

## Built with

* [Python](https://www.python.org/): Python is an interpreted high-level general-purpose programming language

* [Visual Studio code](): Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications.

* [Docker](https://www.docker.com/): Docker is a tool designed to make it easier to create, deploy, and run applications by using containers

## Business Logic

The best government bond benchmark is calculated for every corporate bond and then spread is calculated from the yield. if the yield is similar for two different bonds, the bond with the higher amount outstanding is considered