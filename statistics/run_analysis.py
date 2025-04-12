import argparse
from iris_analysis.io import load, save
from iris_analysis import calculate as cal



def parser_for_stats():
    parser = argparse.ArgumentParser(prog='stats', description="Computing stats for iris dataset")
    parser.add_argument('input', help='input file with iris')
    parser.add_argument('output', help='output file with results')
    return parser


if __name__ == '__main__':
    args = parser_for_stats().parse_args()
    data = load.load_data(dataset_path=args.input)
    result = cal.stats_for_all(data)
    save.save_to_csv(stats=result, output_path=args.output)

