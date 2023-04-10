import sys
import os
import openai
import yaml
import argparse

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.refactoring_tool.code_analysis import CodeAnalysis
from src.refactoring_tool.ai_functions import call_ai_function

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

parser = argparse.ArgumentParser(description="Refactoring Tool")
parser.add_argument("-c", "--config", required=True, help="Path to the refactoring configuration file")
args = parser.parse_args()

def main():
    config_path = args.config

    # Load configuration
    config = load_config(config_path)
    openai.api_key = config["openai"]["api_key"]

    # Example Python code to analyze
    code_to_analyze = """
    import time

    def slow_function(n):
        result = 0
        for i in range(n):
            result += i
            time.sleep(0.1)
        return result

    print(slow_function(10))
    """

    # Print the original code
    print("Original code:")
    print(code_to_analyze)
    print()

    # Analyze different aspects of the code
    performance_suggestions = CodeAnalysis.analyze_code_performance(code_to_analyze)
    readability_suggestions = CodeAnalysis.analyze_code_readability(code_to_analyze)
    modularity_suggestions = CodeAnalysis.analyze_code_modularity(code_to_analyze)

    # Combine suggestions
    all_suggestions = {
        "Performance": performance_suggestions,
        "Readability": readability_suggestions,
        "Modularity": modularity_suggestions,
    }

    # Print suggestions
    for category, suggestions in all_suggestions.items():
        print(f"{category} suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion.strip()}")
        print()

    # Apply suggestions one by one
    modified_code = code_to_analyze
    for category, suggestions in all_suggestions.items():
        modified_code = CodeAnalysis.apply_suggestions(modified_code, {category: suggestions})

    # Print the modified code
    print("\nModified code:")
    print(modified_code)

if __name__ == "__main__":
    main()
