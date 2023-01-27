import subprocess

def run_bash_command(command_as_list, print_returns=False):
    returns = subprocess.run(command_as_list, capture_output=True)
    has_failed = returns.returncode
    output = returns.stdout
    error = returns.stderr
    if print_returns:
        print_command_returns(command_as_list, output, has_failed, error)
    return output, has_failed, error
    

def submit_job(name_jobscript, additional_commands=None, print_returns=True):
    if additional_commands is None:
        additional_commands = []
    output, has_failed, error = run_bash_command(["sbatch"] + additional_commands + [name_jobscript], print_returns=print_returns)
    return output, has_failed, error


def print_command_returns(command, output, has_failed, error):
    if not has_failed:
        print(output)
    else:
        print(f"Error executing {command=}; {output=}, {error=}")
    
    
    
# submit training run

name_training_script = "submit_train.sh"
output_train, _, _ = submit_job(name_training_script)

# submit evaluation to be dependent on training

name_evaluation_script = "submit_evaluate.sh"
_, _, _ = submit_job(name_evaluation_script, additional_commands=[f"--depend=afterany:{output_train}"])

print("\nCurrent status:\n")
#show the current status with 'sjobs'
run_bash_command(["ej"], print_returns=True)
