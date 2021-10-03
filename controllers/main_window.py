from PySide2.QtWidgets import QWidget, QTableWidgetItem,QAbstractItemView
from views.main_window import ListBookForm
from db.books import select_All_Books, select_Book_By_Title, select_Book_By_Category, delete_Book
import os

class ListBookWindow(QWidget, ListBookForm):

    def  __init__(self):
        super().__init__()

        self.setupUi(self)
        
        self.table_Config()
        self.populate_Table(select_All_Books())
        self.populate_ComboBox()
        self.records_Qty()

        self.openBookButton_2.clicked.connect(self.open_NewBookWindow)
        self.openEditButton.clicked.connect(self. open_EditBookWindow)
        self.refreshButton.clicked.connect(self.refresh)
        self.openBookButton.clicked.connect(self.open_Book)
        self.searchButton.clicked.connect(self.search)
        self.deleteBookButton.clicked.connect(self.remove_Book)

        
    def open_NewBookWindow(self):
        from controllers.new_book_window import NewBookWindow
        window = NewBookWindow(self)
        window.show()


    def open_EditBookWindow(self):
        from controllers.edit_book_window import EditBookWindow
        selected_row = self.listBooksTable.selectedItems()

        if selected_row:
            book_id = int(selected_row[0].text())
            window = EditBookWindow(self, book_id)
            window.show()

        self.listBooksTable.clearSelection()
        

    def open_Book(self):
        selected_row = self.listBooksTable.selectedItems()

        if selected_row:
            path = selected_row[5].text()
            os.startfile(path)
        
        self.listBooksTable.clearSelection()


    def remove_Book(self):
        selected_row = self.listBooksTable.selectedItems()
        if selected_row:
            book_id = int(selected_row[0].text())
            row = selected_row[0].row()
            if delete_Book(book_id):
                file_path = selected_row[5].text()
                self.listBooksTable.removeRow(row)
                os.remove(file_path)

        self.records_Qty()


    def table_Config(self):
        column_headers = ('Book ID', 'Title', 'Category', 'Pages', 'Pages Read', 'Path', 'Description')
        self.listBooksTable.setColumnCount(len(column_headers))
        self.listBooksTable.setHorizontalHeaderLabels(column_headers)
        self.listBooksTable.setSelectionBehavior(QAbstractItemView.SelectRows)

    def populate_Table(self, data):
        self.listBooksTable.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.listBooksTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell))) 

        self.records_Qty()

    def refresh(self):
        data = select_All_Books()
        self.listBooksTable.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.listBooksTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        self.records_Qty()

    def populate_ComboBox(self):
        cb_options = ("", "Title", "Category")
        self.searchByComboBox.addItems(cb_options)

    def search_BookByTitle(self, title):
        data = select_Book_By_Title(title)
        self.populate_Table(data)

    def search_BookByCategory(self, category):
        data = select_Book_By_Category(category)
        self.populate_Table(data)

    def search(self):
        option_selected = self.searchByComboBox.currentText()
        parameter = self.parameterLineEdit.text()

        if option_selected == "":
            print("Please Select an Option")
        else:
            if parameter == "":
                print("You must write what you want to consult")
            else:
                if option_selected == "Title":
                    self.search_BookByTitle(parameter)
                elif option_selected == "Category":
                    self.search_BookByCategory(parameter)

    def records_Qty(self):
        qty_rows = str(self.listBooksTable.rowCount())
        self.booksQtyLabel.setText(qty_rows)

    