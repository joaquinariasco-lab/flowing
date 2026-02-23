# Flowing
### A minimal layer letting AI agents from different frameworks communicate and delegate tasks.

Make a LangChain agent talk to a CrewAI agent in minutes.

---

## Why this exists

Today, AI agents built with:
- LangChain
- CrewAI
- AutoGPT-style systems

And cannot communicate natively.

Each team rebuilds:
- Message passing
- Task delegation
- Context exchange
- Execution boundaries

Flowing defines a minimal shared protocol so agents can interoperate without sharing a framework.

---

## ⚡What you can do with it
- Run two independent agents on different ports
- Send structured tasks between them
- Delegate execution safely
- Maintain execution boundaries
- Build framework adapters

---

## 🚀 5-Minute Demo

First:

git clone ...
cd flowing
python agent_server.py
python my_agent_server.py

Then:
curl -X POST http://localhost:5001/run_task ...

Now modify one server to wrap a LangChain agent.
They can now talk.

---

## 🔍 Why not just use X?
Tool	Limitation
LangChain	No cross-framework protocol
CrewAI	Tight ecosystem coupling
AutoGPT	Monolithic execution model

Flowing focuses only on interoperability.
Not orchestration.
Not LLMs.
Not SaaS.
Just the protocol.

---

## 🧠 Core Design Principles

- Agents are networked actors
- Execution is isolated
- Coordination primitives are minimal
- No vendor lock-in

---

## 📦 Current State

Experimental.
Interface definitions evolving.

Includes:
- BaseAgent interface
- Draft protocol
- Two reference agent servers
- Message + task examples

---

## 🛣 Roadmap
- Adapter for LangChain
- Adapter for CrewAI
- Standardized task schema
- Permission system
- Discovery mechanism

--- 
## 🤝 Contributing

If you're building agents and re-implementing glue code,
this repo is for you.
