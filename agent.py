"""
Self-Correcting Code & SQL Agent State Machine
"""
from typing import TypedDict, List
import ast

class AgentState(TypedDict):
    task: str
    code: str
    error_trace: str
    iteration: int
    is_valid: bool

def validate_python_ast(code: str) -> tuple[bool, str]:
    try:
        ast.parse(code)
        return True, ""
    except SyntaxError as e:
        return False, f"SyntaxError: {e.msg} at line {e.lineno}"

def generate_and_repair_pipeline(task: str) -> AgentState:
    state: AgentState = {
        "task": task,
        "code": "def compute_exposure(nav, leverage): return nav * leverage",
        "error_trace": "",
        "iteration": 1,
        "is_valid": False
    }
    valid, err = validate_python_ast(state["code"])
    state["is_valid"] = valid
    state["error_trace"] = err
    return state

if __name__ == "__main__":
    task = "Write a function to calculate capital adequacy ratio under Basel III"
    res = generate_and_repair_pipeline(task)
    print(f"Agent state result: {res}")
