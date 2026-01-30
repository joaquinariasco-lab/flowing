def run_task(publisher, worker, task):
    print(f"\n{publisher.name} publishes task:")
    print(f" - {task.description}")
    print(f" - Price: {task.price}")

    if not worker.can_accept_task(task.price):
        print(f"{worker.name} rejects task (not worth it)")
        return

    print(f"{worker.name} accepts task")

    # Simulation of work
    result = "done"

    success = task.criteria(result)

    if success:
        worker.earn(task.price)
        publisher.lose(task.price)
        print(f"{worker.name} SUCCESS → earns {task.price}")
    else:
        print(f"{worker.name} FAILS → earns nothing")

    print(f"Balances:")
    print(f" - {publisher.name}: {publisher.balance}")
    print(f" - {worker.name}: {worker.balance}")
