from flowing import trace_agent
from reviewer_agent import reviewer_agent

@trace_agent
def coder_agent(plan):
    code = f"Code based on {plan}"
    return reviewer_agent(code)
