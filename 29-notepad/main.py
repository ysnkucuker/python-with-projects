import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QAction,
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QWidget, QPlainTextEdit, QTextEdit, QFontDialog, QColorDialog
)
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QTextFormat




class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = CodeEditor()
        self.setCentralWidget(self.editor)
        self.current_file = None

        self.create_actions()
        self.create_menu()
        self.create_toolbar()

        self.setWindowTitle("NotePad")
        self.resize(900, 600)
        self.show()

    def create_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction(self.find_action)

        format_menu = menubar.addMenu("Format")
        format_menu.addAction(self.bold_action)
        format_menu.addAction(self.italic_action)
        format_menu.addAction(self.underline_action)
        format_menu.addSeparator()
        format_menu.addAction(self.font_action)
        format_menu.addAction(self.color_action)

    def create_actions(self):
        # ---- File actions ----
        self.new_action = QAction("New", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(self.new_file)

        self.open_action = QAction("Open", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.save_file)

        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close)

        # ---- Edit ----
        self.find_action = QAction("Find & Replace", self)
        self.find_action.setShortcut("Ctrl+F")
        self.find_action.triggered.connect(self.open_find_replace)

        # ---- Format ----
        self.bold_action = QAction("Bold", self)
        self.bold_action.setShortcut("Ctrl+B")
        self.bold_action.triggered.connect(self.make_bold)

        self.italic_action = QAction("Italic", self)
        self.italic_action.setShortcut("Ctrl+I")
        self.italic_action.triggered.connect(self.make_italic)

        self.underline_action = QAction("Underline", self)
        self.underline_action.setShortcut("Ctrl+U")
        self.underline_action.triggered.connect(self.make_underline)

        self.font_action = QAction("Font", self)
        self.font_action.triggered.connect(self.choose_font)

        self.color_action = QAction("Text Color", self)
        self.color_action.triggered.connect(self.choose_color)

    def create_toolbar(self):
        toolbar = self.addToolBar("Toolbar")

        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addSeparator()

        toolbar.addAction(self.bold_action)
        toolbar.addAction(self.italic_action)
        toolbar.addAction(self.underline_action)
        toolbar.addAction(self.font_action)
        toolbar.addAction(self.color_action)

    # ---------- Text Formatting ----------
    def make_bold(self):
        cursor = self.editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontWeight(QFont.Bold if fmt.fontWeight() != QFont.Bold else QFont.Normal)
        cursor.mergeCharFormat(fmt)

    def make_italic(self):
        cursor = self.editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        cursor.mergeCharFormat(fmt)

    def make_underline(self):
        cursor = self.editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        cursor.mergeCharFormat(fmt)

    def choose_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            cursor = self.editor.textCursor()
            fmt = cursor.charFormat()
            fmt.setFont(font)
            cursor.mergeCharFormat(fmt)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor = self.editor.textCursor()
            fmt = cursor.charFormat()
            fmt.setForeground(color)
            cursor.mergeCharFormat(fmt)

    def new_file(self):
        self.editor.clear()
        self.current_file = None

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt)"
        )
        if file_name:
            with open(file_name, "r", encoding="utf-8") as f:
                self.editor.setPlainText(f.read())
            self.current_file = file_name

    def save_file(self):
        if not self.current_file:
            self.current_file, _ = QFileDialog.getSaveFileName(
                self, "Save File", "", "Text Files (*.txt)"
            )
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.editor.toPlainText())

    def open_find_replace(self):
        FindReplaceDialog(self.editor).exec_()

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.editor.line_number_area_paint_event(event)

class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.line_number_area = LineNumberArea(self)

        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        self.update_line_number_area_width(0)
        self.highlight_current_line()

    def line_number_area_width(self):
        digits = len(str(self.blockCount()))
        return 10 + self.fontMetrics().horizontalAdvance("9") * digits

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(
                0, rect.y(),
                self.line_number_area.width(),
                rect.height()
            )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(
            QRect(cr.left(), cr.top(),
                  self.line_number_area_width(),
                  cr.height())
        )

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QColor(240, 240, 240))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = int(self.blockBoundingGeometry(block)
                  .translated(self.contentOffset()).top())

        while block.isValid() and top <= event.rect().bottom():
            painter.drawText(
                0, top,
                self.line_number_area.width() - 5,
                self.fontMetrics().height(),
                Qt.AlignRight,
                str(block_number + 1)
            )

            top += int(self.blockBoundingRect(block).height())
            block = block.next()
            block_number += 1

    def highlight_current_line(self):
        selection = QTextEdit.ExtraSelection()
        selection.cursor = self.textCursor()
        selection.format.setBackground(QColor(232, 242, 254))
        selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        self.setExtraSelections([selection])

class FindReplaceDialog(QDialog):
    def __init__(self, editor):
        super().__init__()
        self.editor = editor
        self.setWindowTitle("Find & Replace")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout(self)

        self.find_input = QLineEdit()
        self.replace_input = QLineEdit()

        layout.addWidget(QLabel("Find"))
        layout.addWidget(self.find_input)

        layout.addWidget(QLabel("Replace with"))
        layout.addWidget(self.replace_input)

        buttons = QHBoxLayout()
        find_btn = QPushButton("Find")
        replace_btn = QPushButton("Replace All")

        find_btn.clicked.connect(self.find_text)
        replace_btn.clicked.connect(self.replace_all)

        buttons.addWidget(find_btn)
        buttons.addWidget(replace_btn)
        layout.addLayout(buttons)

    def find_text(self):
        self.editor.find(self.find_input.text())

    def replace_all(self):
        text = self.editor.toPlainText()
        self.editor.setPlainText(
            text.replace(
                self.find_input.text(),
                self.replace_input.text()
            )
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())
