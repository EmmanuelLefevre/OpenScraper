from src.application.services.message_printer import MessagePrinter


class DisplayBackupAborted:
  @staticmethod
  def execute() -> None:
    MessagePrinter.print_backup_aborted("Sauvegarde annulée par l'utilisateur...")
