def call_llm(runtime, decision_id, agent_id, prompt, real_llm_call):

    # REPLAY MODE
    if runtime.mode == "replay":
        return runtime.get_replay_output(decision_id)

    # RECORD MODE
    output = real_llm_call(prompt)

    event = {
        "decision_id": decision_id,
        "agent_id": agent_id,
        "input": prompt,
        "output": output,
        "parent_id": None,
    }

    from flowing.observability.tracer import tracer
    tracer.record(event)

    return output
