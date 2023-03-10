import time
import sys
import asyncio
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from http_client_discord import HTTP_CLIENT_DISCORD

client = HTTP_CLIENT_DISCORD('TOKEN')

def input_window(inputs: list):
    # Erstellen des Dialogfensters für die Eingabefelder
    input_dialog = QDialog()
    input_dialog.setWindowTitle("Eingabefelder")
    input_dialog.setStyleSheet("QDialog { background-color: #333; min-width: 240px; min-height: 140px; max-width: 240px; max-height: 180px; } QLabel { color: #FFFFFF; font-size: 15px;}")
    input_dialog.setWindowIcon(QIcon('img/logo.ico'))
    input_dialog.setWindowTitle("Trolly Discord")
    input_dialog_layout = QVBoxLayout()
    input_dialog.setLayout(input_dialog_layout)
    input_dialog.setModal(True)  # Das Dialogfenster blockiert die Hauptanwendung, bis es geschlossen wird
    # Erstellen des Anforderungs Dialog
    input_layout = QHBoxLayout()
    input_layout.addWidget(QLabel("𝗣𝗹𝘀, 𝘄𝗿𝗶𝘁𝗲 𝗮𝗹𝗹 𝗶𝗻𝗽𝘂𝘁𝘀 :)"))
    input_dialog_layout.addLayout(input_layout)
    # Erstellen der Eingabefelder im Dialogfenster
    input_labels = inputs
    input_fields = []

    for label in input_labels:
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel(label))
        input_layout.addWidget(QLineEdit())
        input_fields.append(input_layout)
        input_dialog_layout.addLayout(input_layout)
    
    # Erstellen der Schaltflächen im Dialogfenster
    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.accepted.connect(input_dialog.accept)
    button_box.rejected.connect(input_dialog.reject)
    input_dialog_layout.addWidget(button_box)
    return input_dialog, input_fields
        
class Worker(QThread):
    output = pyqtSignal(str)
    event_on = False
    selection = -1
    loop_interval = 3
    input_fields = ""

    def __init__(self):
        super().__init__()

    def run(self):
        match self.selection:
            case 0: # RING_USER
                while self.event_on:
                    text = client.RING_USER(self.input_fields[0],self.input_fields[1])
                    self.output.emit(str(text))
                    time.sleep(self.loop_interval)
            case 1: # DISCONECT_USER
                while self.event_on:
                    text = client.DISCONECT_USER(self.input_fields[0],self.input_fields[1])
                    self.output.emit(str(text))
                    time.sleep(self.loop_interval)
            case 2: # CHANGE_VOICE_STATE
                while self.event_on:
                    text = client.CHANGE_VOICE_STATE(self.input_fields[0])
                    self.output.emit(str(text))
                    time.sleep(self.loop_interval)
            case 3: # FULL_MUTE
                while self.event_on:
                    text = client.FULL_MUTE(self.input_fields[0],self.input_fields[1],self.input_fields[2])
                    self.output.emit(str(text))
                    time.sleep(self.loop_interval)
            case 4: # HTTP_CLIENT_HEADSET
                while self.event_on:
                    text = client.HTTP_CLIENT_HEADSET(self.input_fields[0],self.input_fields[1],self.input_fields[2])
                    self.output.emit(str(text))
                    time.sleep(self.loop_interval)
            case 5: # HTTP_CLIENT_MICRO
                while self.event_on:
                    text = client.HTTP_CLIENT_MICRO(self.input_fields[0],self.input_fields[1],self.input_fields[2])
                    self.output.emit(str(text))
                    time.sleep(self.loop_interval)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tool-Liste
        self.tool_list = ["𝗥𝗜𝗡𝗚_𝗨𝗦𝗘𝗥","𝗗𝗜𝗦𝗖𝗢𝗡𝗘𝗖𝗧_𝗨𝗦𝗘𝗥","𝗖𝗛𝗔𝗡𝗚𝗘_𝗩𝗢𝗜𝗖𝗘_𝗦𝗧𝗔𝗧𝗘","𝗙𝗨𝗟𝗟_𝗠𝗨𝗧𝗘","𝗛𝗧𝗧𝗣_𝗖𝗟𝗜𝗘𝗡𝗧_𝗛𝗘𝗔𝗗𝗦𝗘𝗧","𝗛𝗧𝗧𝗣_𝗖𝗟𝗜𝗘𝗡𝗧_𝗠𝗜𝗖𝗥𝗢"]

        # Hauptfenster
        self.setGeometry(20, 40, 650, 480)
        self.setStyleSheet("background-color: #333;")  # Hintergrundfarbe des Hauptfensters
        self.setWindowIcon(QIcon('img/logo.ico'))
        self.setWindowTitle("Trolly Discord")

        # Zentrales Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout des zentralen Widgets
        central_widget_layout = QVBoxLayout()
        central_widget.setLayout(central_widget_layout)

        # Auswahlliste
        self.combo_box = QComboBox()
        self.combo_box.setStyleSheet("background-color: #222; color: #ddd; height: 32; font-size: 15px;")
        self.combo_box.addItems(self.tool_list)
        central_widget_layout.addWidget(self.combo_box)

        # Ausführen-Knopf
        execute_button = QPushButton("Ausführen")
        execute_button.setStyleSheet("background-color: #555; color: #ddd; font-size: 15px;")
        execute_button.setFixedHeight(30)
        central_widget_layout.addWidget(execute_button)

        # Abbrechen-Knopf
        break_button = QPushButton("Abbrechen")
        break_button.setStyleSheet("background-color: #555; color: #ddd; font-size: 15px;")
        break_button.setFixedHeight(30)
        central_widget_layout.addWidget(break_button)

        # Textausgabe
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("background-color: #222; color: #ddd; font-size: 15px;")
        central_widget_layout.addWidget(self.list_widget)

        # Verbindung der Knöpfe mit Signalen
        execute_button.clicked.connect(self.execute_task)
        break_button.clicked.connect(self.task_finished)

        # Worker-Instanz erstellen
        self.worker = Worker()
        self.worker.output.connect(self.list_widget.addItem)

    def execute_task(self):        
        input_dialog, input_fields = None, None
        selection = -1
        for i in range(len(self.tool_list)):
            if self.combo_box.currentText() == self.tool_list[i]:
                selection = i
                self.list_widget.addItem("test1")
                try:
                    match selection:
                        case 0:
                            input_dialog, input_fields = input_window(["channel_id","user_id","Loop Interval"]) # RING_USER
                        case 1:
                            input_dialog, input_fields = input_window(["guild_id","user_id","Loop Interval"]) # DISCONECT_USER
                        case 2:
                            input_dialog, input_fields = input_window(["voice_id","Loop Interval"]) # CHANGE_VOICE_STATE
                        case 3:
                            input_dialog, input_fields = input_window(["guild_id","user_id","bool","Loop Interval"]) # FULL_MUTE
                        case 4:
                            input_dialog, input_fields = input_window(["guild_id","user_id","bool","Loop Interval"]) # HTTP_CLIENT_HEADSET
                        case 5:
                            input_dialog, input_fields = input_window(["guild_id","user_id","bool","Loop Interval"]) # HTTP_CLIENT_MICRO
                    
                    
                    result = input_dialog.exec_()
    
                    if result == QDialog.Accepted:
                        self.list_widget.addItem("test3")
                        self.list_widget.addItem("Tool: "+self.combo_box.currentText()+" | "+input_fields[0].itemAt(0).widget().text()+": "+input_fields[0].itemAt(1).widget().text()+" | "+input_fields[1].itemAt(0).widget().text()+": "+input_fields[1].itemAt(1).widget().text()+" | "+input_fields[2].itemAt(0).widget().text()+": "+input_fields[2].itemAt(1).widget().text())
                        self.list_widget.addItem(" ")
                        if (self.worker.event_on):
                             self.list_widget.addItem("Pls stop the Tool that is runing.")
                        elif (self.worker.event_on == False):
                            fields = []
                            for i in range(len(input_fields)):
                                fields.append(input_fields[i].itemAt(1).widget().text())

                            try:
                                self.worker.event_on = True
                                self.worker.selection = selection
                                self.worker.loop_interval = int(input_fields[len(input_fields)].itemAt(1).widget().text())
                                self.worker.input_fields = fields
                                self.worker.start()
                            except:
                                self.list_widget.addItem("An Error Input, check all inputs. Pls :)")
                except: None

    def task_finished(self):
        if (self.worker.event_on == True):
            self.worker.event_on = False
            self.worker.quit()
            self.list_widget.addItem("Tool stoped")
        elif (self.worker.event_on == False):
            self.list_widget.addItem("No Tool is runing to stop.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow() 
    main.show()
    sys.exit(app.exec_())