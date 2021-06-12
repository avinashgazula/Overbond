import json
import sys

if(len(sys.argv) < 3):
    raise Exception(
        "Please make sure input and output files are mentioned in the command")
else:
    input_path = sys.argv[-2]
    output_path = sys.argv[-1]


class Benchmark:
    def __init__(self, input_path):
        self.corporate_bonds = []
        self.government_bonds = []
        self.input_path = input_path
        self.json_data = None
        self.read_from_json()

    def read_from_json(self):
        with open(input_path, encoding='utf-8') as fh:
            fdata = json.load(fh)
            self.json_data = fdata["data"]
            for bond in self.json_data:
                if(bond['tenor'] is not None and bond['yield'] is not None and bond['amount_outstanding'] is not None):
                    if bond['type'] == 'corporate':
                        self.corporate_bonds.append(bond)
                    elif bond['type'] == 'government':
                        self.government_bonds.append(bond)

    def best_benchmark_index(self, corporate_index):
        min_benchmark = sys.maxsize
        best_benchmark_index = -1
        for government_index in range(len(self.government_bonds)):
            benchmark = abs(float(self.corporate_bonds[corporate_index]['tenor'].split()[
                            0]) - float(self.government_bonds[government_index]['tenor'].split()[0]))
            if benchmark < min_benchmark or (benchmark == min_benchmark and float(self.government_bonds[government_index]['amount_outstanding']) > float(self.government_bonds[best_benchmark_index]['amount_outstanding'])):
                min_benchmark = benchmark
                best_benchmark_index = government_index
        return best_benchmark_index

    def spread(self):
        result = []
        for corporate_index in range(len(self.corporate_bonds)):
            best_benchmark_index = self.best_benchmark_index(corporate_index)
            spread = 100 * abs(float(self.corporate_bonds[corporate_index]["yield"].strip(
                '%'))-float(self.government_bonds[best_benchmark_index]['yield'].strip('%')))
            data_object = {}
            data_object['corporate_bond_id'] = self.corporate_bonds[corporate_index]['id']
            data_object['government_bond_id'] = self.government_bonds[best_benchmark_index]['id']
            data_object['spread'] = str(round(spread)) + ' bps'
            result.append(data_object)
        return result

    def write_output(self, result):
        print(result)
        with open(output_path, 'w') as f:
            data = {}
            data["data"] = result
            json.dump(data, f)


if __name__ == "__main__":
    benchmark = Benchmark(input_path)
    spread_result = benchmark.spread()
    benchmark.write_output(spread_result)
