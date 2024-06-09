import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

import mysql.connector

# Kết nối tới cơ sở dữ liệu MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Clbtoanhoc11!",
    database="librarymanagement"
)
cursor = db.cursor()

# Các lớp để lưu trữ thông tin sách và biên mục sách
class BookMarc:
    def __init__(self, book_id, title, author, publisher, year, isbn):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.isbn = isbn

class Book:
    def __init__(self, inventory_number, book_id, status):
        self.inventory_number = inventory_number
        self.book_id = book_id
        self.status = status

# Các hàm để tương tác với cơ sở dữ liệu
def add_book_marc(book_marc):
    cursor.execute("SELECT * FROM bookMarc WHERE book_id = %s", (book_marc.book_id,))
    if cursor.fetchone():
        raise Exception("Mã sách đã tồn tại")
    
    cursor.execute("SELECT * FROM bookMarc WHERE isbn = %s", (book_marc.isbn,))
    if cursor.fetchone():
        raise Exception("Số ISBN đã tồn tại")
    
    cursor.execute("INSERT INTO bookMarc (book_id, title, author, publisher, year, isbn) VALUES (%s, %s, %s, %s, %s, %s)", 
                   (book_marc.book_id, book_marc.title, book_marc.author, book_marc.publisher, book_marc.year, book_marc.isbn))
    db.commit()

def update_book_marc(book_marc):
    cursor.execute("SELECT * FROM bookMarc WHERE book_id = %s", (book_marc.book_id,))
    if not cursor.fetchone():
        raise Exception("Mã sách không tồn tại")
    
    cursor.execute("UPDATE bookMarc SET title = %s, author = %s, publisher = %s, year = %s, isbn = %s WHERE book_id = %s", 
                   (book_marc.title, book_marc.author, book_marc.publisher, book_marc.year, book_marc.isbn, book_marc.book_id))
    db.commit()

def delete_book_marc(book_id):
    cursor.execute("DELETE FROM bookMarc WHERE book_id = %s", (book_id,))
    db.commit()

def search_book_marc_by_id(book_id):
    cursor.execute("SELECT * FROM bookMarc WHERE book_id = %s", (book_id,))
    return cursor.fetchone()

def search_book_marc_by_title(title):
    cursor.execute("SELECT * FROM bookMarc WHERE title LIKE %s", ('%' + title + '%',))
    return cursor.fetchall()

def search_book_marc_by_isbn(isbn):
    cursor.execute("SELECT * FROM bookMarc WHERE isbn = %s", (isbn,))
    return cursor.fetchone()

def add_book(book):
    cursor.execute("SELECT * FROM book WHERE inventory_number = %s", (book.inventory_number,))
    if cursor.fetchone():
        raise Exception("Số nhập kho đã tồn tại")
    
    cursor.execute("INSERT INTO book (inventory_number, book_id, status) VALUES (%s, %s, %s)", 
                   (book.inventory_number, book.book_id, book.status))
    db.commit()

def update_book(book):
    cursor.execute("SELECT * FROM book WHERE inventory_number = %s", (book.inventory_number,))
    if not cursor.fetchone():
        raise Exception("Số nhập kho không tồn tại")
    
    cursor.execute("UPDATE book SET book_id = %s, status = %s WHERE inventory_number = %s", 
                   (book.book_id, book.status, book.inventory_number))
    db.commit()

def delete_book(inventory_number):
    cursor.execute("DELETE FROM book WHERE inventory_number = %s", (inventory_number,))
    db.commit()

def search_books_by_book_id(book_id):
    cursor.execute("SELECT * FROM book WHERE book_id = %s", (book_id,))
    return cursor.fetchall()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Library Management System")

# # Thêm logo
# logo = tk.PhotoImage(file="path/to/your/logo.png")
# logo_label = tk.Label(root, image=logo)
# logo_label.grid(row=0, column=0, pady=10)

# Tải ảnh
image_path = "D:\\Python\\Library Management\\report\\image\\logo.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Hiển thị ảnh bằng widget Label
# Hiển thị ảnh bằng widget Label
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=0, pady=10)



# Sử dụng ttk để có giao diện đẹp hơn
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

book_marc_frame = ttk.Frame(root, padding="10 10 10 10")
book_frame = ttk.Frame(root, padding="10 10 10 10")

# Hàm để hiển thị frame
def show_frame(frame):
    frame.tkraise()

for frame in (main_frame, book_marc_frame, book_frame):
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Cửa sổ chính
ttk.Label(main_frame, text="Library Management System", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)
ttk.Button(main_frame, text="Quản lý biên mục sách", command=lambda: show_frame(book_marc_frame)).grid(row=1, column=0, pady=5)
ttk.Button(main_frame, text="Quản lý sách", command=lambda: show_frame(book_frame)).grid(row=2, column=0, pady=5)

# Cửa sổ quản lý biên mục sách
ttk.Label(book_marc_frame, text="Quản lý biên mục sách", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)

marc_frame = ttk.LabelFrame(book_marc_frame, text="Thông tin biên mục sách")
marc_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

ttk.Label(marc_frame, text="Mã sách:").grid(row=0, column=0, sticky=tk.W, pady=2)
entry_book_id = ttk.Entry(marc_frame)
entry_book_id.grid(row=0, column=1, pady=2)

ttk.Label(marc_frame, text="Tên sách:").grid(row=1, column=0, sticky=tk.W, pady=2)
entry_title = ttk.Entry(marc_frame)
entry_title.grid(row=1, column=1, pady=2)

ttk.Label(marc_frame, text="Tên tác giả:").grid(row=2, column=0, sticky=tk.W, pady=2)
entry_author = ttk.Entry(marc_frame)
entry_author.grid(row=2, column=1, pady=2)

ttk.Label(marc_frame, text="Nhà xuất bản:").grid(row=3, column=0, sticky=tk.W, pady=2)
entry_publisher = ttk.Entry(marc_frame)
entry_publisher.grid(row=3, column=1, pady=2)

ttk.Label(marc_frame, text="Năm xuất bản:").grid(row=4, column=0, sticky=tk.W, pady=2)
entry_year = ttk.Entry(marc_frame)
entry_year.grid(row=4, column=1, pady=2)

ttk.Label(marc_frame, text="Số ISBN:").grid(row=5, column=0, sticky=tk.W, pady=2)
entry_isbn = ttk.Entry(marc_frame)
entry_isbn.grid(row=5, column=1, pady=2)

def add_book_marc_event():
    try:
        book_marc = BookMarc(
            int(entry_book_id.get()),
            entry_title.get(),
            entry_author.get(),
            entry_publisher.get(),
            int(entry_year.get()),
            entry_isbn.get()
        )
        add_book_marc(book_marc)
        messagebox.showinfo("Success", "Biên mục sách đã được thêm thành công")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_book_marc_event():
    try:
        book_marc = BookMarc(
            int(entry_book_id.get()),
            entry_title.get(),
            entry_author.get(),
            entry_publisher.get(),
            int(entry_year.get()),
            entry_isbn.get()
        )
        update_book_marc(book_marc)
        messagebox.showinfo("Success", "Biên mục sách đã được cập nhật thành công")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_book_marc_event():
    try:
        book_id = int(entry_book_id.get())
        delete_book_marc(book_id)
        messagebox.showinfo("Success", "Biên mục sách đã được xóa thành công")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_book_marc_event():
    try:
        book_id = int(entry_book_id.get())
        result = search_book_marc_by_id(book_id)
        if result:
                    messagebox.showinfo("Search Result", f"Mã sách: {result[0]}\nTên sách: {result[1]}\nTác giả: {result[2]}\nNhà xuất bản: {result[3]}\nNăm xuất bản: {result[4]}\nISBN: {result[5]}")
        else:
            messagebox.showinfo("Search Result", "Không tìm thấy biên mục sách")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ttk.Button(book_marc_frame, text="Thêm", command=add_book_marc_event).grid(row=2, column=0, pady=5)
ttk.Button(book_marc_frame, text="Cập nhật", command=update_book_marc_event).grid(row=3, column=0, pady=5)
ttk.Button(book_marc_frame, text="Xóa", command=delete_book_marc_event).grid(row=4, column=0, pady=5)
ttk.Button(book_marc_frame, text="Tìm kiếm", command=search_book_marc_event).grid(row=5, column=0, pady=5)
ttk.Button(book_marc_frame, text="Quay lại", command=lambda: show_frame(main_frame)).grid(row=6, column=0, pady=5)

# Cửa sổ quản lý sách
ttk.Label(book_frame, text="Quản lý sách", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)

book_info_frame = ttk.LabelFrame(book_frame, text="Thông tin sách")
book_info_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

ttk.Label(book_info_frame, text="Số nhập kho:").grid(row=0, column=0, sticky=tk.W, pady=2)
entry_inventory_number = ttk.Entry(book_info_frame)
entry_inventory_number.grid(row=0, column=1, pady=2)

ttk.Label(book_info_frame, text="Mã sách:").grid(row=1, column=0, sticky=tk.W, pady=2)
entry_book_id_for_book = ttk.Entry(book_info_frame)
entry_book_id_for_book.grid(row=1, column=1, pady=2)

ttk.Label(book_info_frame, text="Tình trạng:").grid(row=2, column=0, sticky=tk.W, pady=2)
status_var = tk.StringVar(value="trong kho")
ttk.Radiobutton(book_info_frame, text="Đang cho mượn", variable=status_var, value="đang cho mượn").grid(row=2, column=1, sticky=tk.W, pady=2)
ttk.Radiobutton(book_info_frame, text="Trong kho", variable=status_var, value="trong kho").grid(row=2, column=2, sticky=tk.W, pady=2)

def add_book_event():
    try:
        book = Book(
            int(entry_inventory_number.get()),
            int(entry_book_id_for_book.get()),
            status_var.get()
        )
        add_book(book)
        messagebox.showinfo("Success", "Sách đã được thêm thành công")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_book_event():
    try:
        book = Book(
            int(entry_inventory_number.get()),
            int(entry_book_id_for_book.get()),
            status_var.get()
        )
        update_book(book)
        messagebox.showinfo("Success", "Sách đã được cập nhật thành công")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_book_event():
    try:
        inventory_number = int(entry_inventory_number.get())
        delete_book(inventory_number)
        messagebox.showinfo("Success", "Sách đã được xóa thành công")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_books_by_book_id_event():
    try:
        book_id = int(entry_book_id_for_book.get())
        results = search_books_by_book_id(book_id)
        if results:
            messagebox.showinfo("Search Result", "\n".join([f"Số nhập kho: {result[0]}, Tình trạng: {result[2]}" for result in results]))
        else:
            messagebox.showinfo("Search Result", "Không tìm thấy sách")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ttk.Button(book_frame, text="Thêm", command=add_book_event).grid(row=2, column=0, pady=5)
ttk.Button(book_frame, text="Cập nhật", command=update_book_event).grid(row=3, column=0, pady=5)
ttk.Button(book_frame, text="Xóa", command=delete_book_event).grid(row=4, column=0, pady=5)
ttk.Button(book_frame, text="Tìm kiếm", command=search_books_by_book_id_event).grid(row=5, column=0, pady=5)
ttk.Button(book_frame, text="Quay lại", command=lambda: show_frame(main_frame)).grid(row=6, column=0, pady=5)

# Hiển thị frame chính
show_frame(main_frame)
root.mainloop()

