# Prefect Experimentation

This project is an exploration of [Prefect](https://www.prefect.io/) for workflow orchestration and task automation. Aim to experiment with Prefect's features and integrations, including its Snowflake module, using Python.

## Project Details

- **Objective**: Experiment with Prefect to understand its capabilities and evaluate its suitability for our workflows.
- **Prefect Version**: `3.1.4`
- **Python Version**: `3.12`
- **Key Integration**: Prefect's Snowflake module (`Prefect[Snowflake]`)

## Features Explored
- Flow and task creation using Prefect
- Scheduling workflows
- Monitoring and orchestration through Prefect
- Integrating with Snowflake for data operations

## Installation

### Prerequisites
1. **Python 3.12**: Make sure you have Python 3.12 installed on your machine.
2. **Prefect CLI**: Install the Prefect CLI for managing and running flows.

1. dependencies:
   ```bash
   poetry add prefect
   poetry add prefect[Snowflake]
   ```

## Usage

### Running a Flow
1. Define a Prefect flow in Python.
2. Use the Prefect CLI or Prefect UI to schedule or run the flow:
   ```bash
   prefect server start
   ```

3. Execute the flow:
   ```bash
   poetry run python flow_script.py
   ```

### Integrating with Snowflake
- Prefect's Snowflake module simplifies executing queries and loading data into Snowflake. Ensure Snowflake credentials are configured in your environment or stored securely in Prefect's block storage.

## Resources

- [Prefect Documentation](https://docs.prefect.io/)
- [Prefect Snowflake Integration](https://docs.prefect.io/integrations/snowflake/)

