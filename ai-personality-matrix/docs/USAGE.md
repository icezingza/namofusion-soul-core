# USAGE.md

## Running main.py
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the module:
   ```bash
   python main.py
   ```

## Docker Example
```bash
docker run -it --rm -v $(pwd):/app -w /app python:3.10 bash -c "pip install -r requirements.txt && python main.py"
```

## Deployment Tips
- **Local:** Use a virtual environment for isolation.
- **Cloud:** Deploy as a container or serverless function. Ensure API ports are open and secure.
- **Scaling:** Use load balancers for high availability.
