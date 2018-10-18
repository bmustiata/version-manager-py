FROM python:3.6

RUN pip install vm

# it's not directly version-manager to wait for child processes
# that die unexpectedly.
ENTRYPOINT vm
