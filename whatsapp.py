from mcp.server.fastmcp import FastMCP

import requests

mcp = FastMCP("whatsapp")

url = "http://localhost:3000/api/sendText"


@mcp.resource("resource://contact-list")
def get_contact_list() -> dict:
    """Returns a dictionary of contacts for WhatsApp. Each contact name is paired with it's respective phone number.
    """
    return {"Vivo": "+5511999151515",
            "Claro": "+5511999910621",
            "Oi": "+553131313131"}

@mcp.tool()
def send_message(chatId: str, text: str) -> str:
    """Send WhatsApp message to a specified contact.


    Args:
        chatId: The contact's phone number written in the international format (e.g. +5561987654321)
        text: The contents of the message (Text only)
    """

    headers = { "Accept": "application/json", "Content-Type": "application/json" }
    number = chatId[chatId.find("+")+1:] + "@c.us"
    data = { "chatId": number, "text": text, "session": "default" }
    response = requests.post(url, json=data, headers=headers)

    return response.text


if __name__ == "__main__":
    mcp.run(transport='stdio')
