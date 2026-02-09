class AutonomousController:
    def run_cycle(self):
        tasks = self.generate_tasks()
        assignments = self.assign(tasks)
        results = self.execute(assignments)
        self.evaluate(results)
        self.update_economy(results)
