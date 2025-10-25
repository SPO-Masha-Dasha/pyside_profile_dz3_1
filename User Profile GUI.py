import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont, QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(300, 550)
        self.setWindowTitle("Профиль Джедая - Оби-Ван Кеноби")
        self.setUpMainWindow()
        self.show()

    def createRoundPixmap(self, size=120):
        try:
            pixmap = QPixmap()
            if pixmap.isNull():
                raise FileNotFoundError

            pixmap = pixmap.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)

            rounded = QPixmap(size, size)
            rounded.fill(Qt.GlobalColor.transparent)

            painter = QPainter(rounded)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            path = QPainterPath()
            path.addEllipse(0, 0, size, size)
            painter.setClipPath(path)

            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            return rounded

        except Exception as e:
            print(f"Error loading image: {e}")
            return QPixmap(size, size)

    def createImageLabels(self):
        try:
            bg_label = QLabel(self)
            bg_pixmap = QPixmap("")
            bg_pixmap = bg_pixmap.scaled(300, 180, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
            bg_label.setPixmap(bg_pixmap)
            bg_label.move(0, 0)
        except FileNotFoundError as error:
            print(f"Background image not found. Error: {error}")

        try:
            profile_pixmap = self.createRoundPixmap("", 120)
            profile_label = QLabel(self)
            profile_label.setPixmap(profile_pixmap)
            profile_label.move(90, 30)
        except Exception as error:
            print(f"Profile image error: {error}")

    def setUpMainWindow(self):
        self.createImageLabels()

        name_label = QLabel(self)
        name_label.setText("Оби-Ван Кеноби")
        name_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        name_label.move(50, 190)

        bio_title_label = QLabel(self)
        bio_title_label.setText("Биография")
        bio_title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        bio_title_label.move(20, 230)

        bio_text_label = QLabel(self)
        bio_text_label.setText("Мастер-Джедай, наставник Энакина и Люка Скайуокеров. Хранитель мира в галактике.")
        bio_text_label.setWordWrap(True)
        bio_text_label.setFixedWidth(260)
        bio_text_label.move(20, 255)

        abilities_title_label = QLabel(self)
        abilities_title_label.setText("Способности")
        abilities_title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        abilities_title_label.move(20, 320)

        abilities_text_label = QLabel(self)
        abilities_text_label.setText("Сила Джедаев | Форма III | Философия | Наставничество")
        abilities_text_label.setWordWrap(True)
        abilities_text_label.setFixedWidth(260)
        abilities_text_label.move(20, 345)

        experience_title_label = QLabel(self)
        experience_title_label.setText("Опыт")
        experience_title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        experience_title_label.move(20, 410)

        position1_label = QLabel(self)
        position1_label.setText("Мастер-Джедай Совета")
        position1_label.setFont(QFont("Arial", 11))
        position1_label.move(20, 435)

        dates1_label = QLabel(self)
        dates1_label.setText("32 ДБЯ - 19 ДБЯ")
        dates1_label.setFont(QFont("Arial", 9))
        dates1_label.move(20, 455)

        position2_label = QLabel(self)
        position2_label.setText("Падаван Квай-Гона Джинна")
        position2_label.setFont(QFont("Arial", 11))
        position2_label.move(20, 480)

        dates2_label = QLabel(self)
        dates2_label.setText("44 ДБЯ - 32 ДБЯ")
        dates2_label.setFont(QFont("Arial", 9))
        dates2_label.move(20, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())