from fastmcp import FastMCP
import random
import json


mcp = FastMCP(name="Simple Remote Server.")

@mcp.tool
def add(a: int,b: int)->int:
    """Adds two given numbers a and b and returns its sum."""
    return a+b


@mcp.tool
def generate_random_number(start_range: int,stop_range: int)->int:
    """Generate a random number between the given start_range and stop_range."""
    return random.randint(start_range,stop_range)

@mcp.resource("info://server")
def server_info()->str:
    """Get information about this server"""
    info={
        "name":"Simple Calculator Server",
        "version":"1.0.0",
        "description":"A basic MCP server with math tools.",
        "tools":["add","random_number"],
        "author":"Veeru"
    }
    return json.dumps(info,indent=2)


if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)