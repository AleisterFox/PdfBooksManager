from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.edit_book_window import EditBookForm
from db.books import select_Book_By_Id, update_Book
import re
import os
import shutil

class EditBookWindow(QWidget,EditBookForm):
    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.selectFileButton.clicked.connect(self.select_File)
        self.editButton.clicked.connect(self.edit_Book)
        self.cancelButton.clicked.connect(self.close)
        self.populate_Inputs()
        

    def populate_Inputs(self):
        data = select_Book_By_Id(self._id)
        
        self.titleLineEdit.setText(data[1])
        self.categoryLineEdit.setText(data[2])
        self.pageQtySpinBox.setValue(data[3])
        self.pageQtyReadSpinBox_2.setValue(data[4])
        self.filePathLineEdit.setText(data[5])
        self.descriptionTextEdit.setText(data[6])

    def select_File(self):
        self.old_path = self.filePathLineEdit.text()

        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)

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

    def edit_Book(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pageQtySpinBox.value()
        page_qty_read = self.pageQtyReadSpinBox_2.text()
        path = self.filePathLineEdit.text()
        description = self.descriptionTextEdit.toPlainText()

        data = [title, category, page_qty, page_qty_read, path, description]

        if self.check_Inputs():
            path_to_check = 'book_files\\' + re.split("/|\\\\", path)[-1]
            result = os.path.exists(path_to_check)

    
            if result == False:
                data[4] = shutil.copy(path, "book_files")
                os.remove(self.old_path)
            
            if update_Book(self._id, data):
                self.close()