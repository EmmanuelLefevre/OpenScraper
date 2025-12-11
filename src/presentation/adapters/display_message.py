from colorama import Fore, Style
from src.domain.ports.message_display_port import MessageDisplayPort

class ConsoleMessageDisplayAdapter(MessageDisplayPort):
  def display(self, message: str, message_type: str) -> None:
    formats = {
      "error": (Style.BRIGHT, Fore.RED, "💥"),
      "exception": (Style.NORMAL, Fore.RED, "💣"),
      "info": (Style.BRIGHT, Fore.CYAN, "ℹ"),
      "message": (Style.NORMAL, Fore.BLUE, ""),
      "saved_file": (Style.BRIGHT, Fore.GREEN, "📄"),
      "success": (Style.BRIGHT, Fore.GREEN, "✅"),
      "warning": (Style.BRIGHT, Fore.MAGENTA, "⚠️"),
      "backup_aborted": (Style.BRIGHT, Fore.RED, "❌"),
    }

    style, color, icon = formats.get(message_type, (Style.NORMAL, Fore.WHITE, ""))

    print(f"{style}{color}{icon} {message}{Style.RESET_ALL}")
