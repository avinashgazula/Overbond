FROM python:3
WORKDIR /submission
COPY . .
CMD python3 BenchmarkTest.py sample_input.json sample_output.json ; python3 Benchmark.py sample_input.json sample_output.json