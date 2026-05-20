from rich.console import Console
from rich.panel import Panel

from app.chatbot import AIChatbot
from app.utils import save_chat_history

console = Console()


def main():
    """
    Main function for AI-CLI chatbot.
    :return:
    """
    chatbot = AIChatbot()

    console.print(
        Panel.fit(
            "🤖 AI CLI Chatbot Started\nType 'exit' to quit.",
            title="Generative AI Project",
        )
    )

    while True:
        user_input = console.input("\n[bold cyan]You:[/bold cyan] ")
        if user_input.lower() in ["exit", "quit"]:
            save_chat_history(chatbot.messages)

            console.print("\n👋 Goodbye!")
            break

        try:
            response = chatbot.chat(user_input)

            console.print(f"\n[bold green]AI:[/bold green] {response}")

        except Exception as error:
            console.print(f"\n[bold red]Error:[/bold red] {error}")


if __name__ == "__main__":
    main()
