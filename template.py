import asyncio
from datetime import datetime
from logger import logger

###
### PASTE ALL THE CODE COPIED FROM AGENT BUILDER
###


if __name__ == "__main__":
    try:
        # We assume the presence of WorkflowInput
        workflow_input = WorkflowInput(input_as_text="Scarpe da running")

        # Execute the Workflow with asyncio (the method run_workflow is async)
        result = asyncio.run(run_workflow(workflow_input))

        # change this with the correct output key
        output_text = result.get("output_text", "")

        # Stampa il risultato in console
        logger.debug("=== Print Output ===")
        logger.debug(output_text)

        # Salva il risultato su file txt
        output_filename = (
            f"workflow_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        )
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(output_text)

        logger.info(f"\n✓ File saved in: {output_filename}")
    except Exception as err:
        logger.error(f"Error during workflow execution: {err}")
