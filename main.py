from fastmcp import FastMCP
import random


mcp = FastMCP(name="Simple Remote Server.")

@mcp.tool
def add(a: int,b: int)->int:
    """Adds two given numbers a and b and returns its sum."""
    return a+b


@mcp.tool
def generate_random_number(start_range: int,stop_range: int)->int:
    """Generate a random number between the given start_range and stop_range."""
    return random.randint(start_range,stop_range)


if __name__=="__main__":
    mcp.run()