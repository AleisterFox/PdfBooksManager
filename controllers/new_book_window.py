from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.new_book_window import NewBookForm 
from db.books import insert_Book
import shutil
import os


class NewBookWindow(QWidget,NewBookForm):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.addButton.clicked.connect(self.add_Book)
        self.selectFileButton.clicked.connect(self.select_File)
        self.cancelButton.clicked.connect(self.close)

    def check_Inputs(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pageQtySpinBox.value()
        path = self.filePathLineEdit.text()

        error_count = 0

        if title == "":
            print('TITLE field is empty')
            error_count += 1
        if category == "":
            print('CATEGORY field is empty')
            error_count += 1
        if path == "":
            print('You MUST select a book')
            error_count += 1
        
        if error_count == 0:
            return True

    def add_Book(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pageQtySpinBox.value()
        path = self.filePathLineEdit.text()
        description = self.descriptionTextEdit.toPlainText()

        if self.check_Inputs():
            new_path = shutil.copy(path, "book_files") #Almacena la nueva ruta del archivo despues de copiarla a la nueva carpeta
            data = (title, category, page_qty, new_path, description)

            if insert_Book(data):
                self.clean_Inputs()
            else:
                self.filePathLineEdit.setText(new_path)
                self.undo()

    def clean_Inputs(self):
        self.titleLineEdit.clear()
        self.categoryLineEdit.clear()
        self.pageQtySpinBox.setValue(0)
        self.filePathLineEdit.clear()
        self.descriptionTextEdit.clear()


    def select_File(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)


    def undo(self):
        file_path = self.filePathLineEdit.text()

        if file_path != "":
            os.remove(file_path)

