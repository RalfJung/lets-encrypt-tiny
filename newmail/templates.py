# -*- coding: utf-8 -*-
SUBJECT = "Deine E-Mail-Adresse {user}"
TEMPLATE = """Hallo,

du hast jetzt einen E-Mail-Account "{user}" mit Passwort "{password}".
Bevor du dich einloggen kannst, musst du das Passwort unter <https://{host}/changepw> ändern.

{incoming}

Versenden kannst du Mails via SMTP:
  Server: {host}
  Port:   587
  Verschlüsselung: STARTTLS
  Benutzername: {user}

Bitte prüfe, ob das alles funktioniert. Bei Problemen kannst du dich gerne an mich wenden.

Viele Grüße,
Ralf"""
INCOMING_FORWARD = "Eingehende Mails werden an deine Adresse {forward} weitergeleitet."
INCOMING_IMAP    = '''Der Zugriff auf das Postfach erfolgt via IMAP:
  Server: {host}
  Port:   143
  Verschlüsselung: STARTTLS
  Benutzername: {user}'''

