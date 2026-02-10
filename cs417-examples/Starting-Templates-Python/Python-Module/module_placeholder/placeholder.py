from datetime import datetime

def demo_function(name: str) -> str:

    return f"Hello {name:}. It is {datetime.now():%A}"
