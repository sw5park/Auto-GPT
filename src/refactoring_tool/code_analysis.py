from typing import List
import json
from typing import List, Dict
from src.refactoring_tool.ai_functions import call_ai_function


class CodeAnalysis:
  
    @staticmethod
    def analyze_code_readability(code: str) -> List[str]:
        """
        Analyze the readability of the given code and return a list of suggestions for improving readability.
        
        :param code: The source code to analyze as a string.
        :return: A list of strings containing suggestions for improving readability.
        """
        function_string = "def analyze_code_readability(code: str) -> List[str]:"
        args = [code]
        description_string = "Analyze the readability of the given code and return a list of suggestions for improving readability."

        result_string = call_ai_function(
            function_string, tuple(args), description_string)
        try:
            return json.loads(result_string)
        except json.JSONDecodeError:
            # If the output is not a valid JSON, return the output as a single-item list.
            return [result_string]

    @staticmethod
    def analyze_code_performance(code: str) -> List[str]:
        """
        Analyze the given code and return a list of suggestions for optimizing performance.
        
        :param code: The source code to analyze as a string.
        :return: A list of strings containing suggestions for optimizing performance.
        """
        function_string = "def analyze_code_performance(code: str) -> List[str]:"
        args = [code]
        description_string = "Analyzes the given code and returns a list of suggestions for optimizing performance."

        result_string = call_ai_function(
            function_string, tuple(args), description_string)
        try:
            return json.loads(result_string)
        except json.JSONDecodeError:
            # If the output is not a valid JSON, return the output as a single-item list.
            return [result_string]

    @staticmethod
    def analyze_code_security(code: str) -> List[str]:
        """
        Analyze the given code and return a list of suggestions for improving security.
        
        :param code: The source code to analyze as a string.
        :return: A list of strings containing suggestions for improving security.
        """
        function_string = "def analyze_code_security(code: str) -> List[str]:"
        args = [code]
        description_string = "Analyzes the given code and returns a list of suggestions for improving security."

        result_string = call_ai_function(
            function_string, tuple(args), description_string)
        try:
            return json.loads(result_string)
        except json.JSONDecodeError:
            # If the output is not a valid JSON, return the output as a single-item list.
            return [result_string]

    @staticmethod
    def analyze_code_modularity(code: str) -> List[str]:
        """
        Analyze the given code and return a list of suggestions for improving modularity.
        
        :param code: The source code to analyze as a string.
        :return: A list of strings containing suggestions for improving modularity.
        """
        function_string = "def analyze_code_modularity(code: str) -> List[str]:"
        args = [code]
        description_string = "Analyzes the given code and returns a list of suggestions for improving modularity."

        result_string = call_ai_function(
            function_string, tuple(args), description_string)
        try:
            return json.loads(result_string)
        except json.JSONDecodeError:
            # If the output is not a valid JSON, return the output as a single-item list.
            return [result_string]
    

    @staticmethod
    def apply_suggestions(code: str, categorized_suggestions: Dict[str, List[str]]) -> str:
        """
        Apply the suggestions to the given code and return the modified code.

        :param code: The source code to modify as a string.
        :param categorized_suggestions: A dictionary containing categories and their respective lists of suggestions.
        :return: A modified version of the code with the suggestions applied.
        """
        if not categorized_suggestions:
            return code

        modified_code = code
        for category, suggestions in categorized_suggestions.items():
            for suggestion in suggestions:
                function_string = "def apply_suggestion(code: str, suggestion: str) -> str:"
                args = [modified_code, suggestion]
                description_string = "Apply a suggestion to the given code and return the modified code. Ensure the outputs of source code and modified code are the same."
                modified_code = call_ai_function(function_string, tuple(args), description_string)

        return modified_code