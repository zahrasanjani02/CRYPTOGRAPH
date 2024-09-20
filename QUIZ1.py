import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Vigenere cipher
def vigenere_encrypt(text, key):
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    return result

# Playfair cipher
def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used_chars = set()
    
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_in_matrix(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return -1, -1

def prepare_text(text):
    text = text.upper().replace("J", "I")
    prepared = ""
    
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        
        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2
    
    if len(prepared) % 2 != 0:
        prepared += 'X'
    
    return prepared

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = prepare_text(text)
    
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_in_matrix(matrix, a)
        row2, col2 = find_in_matrix(matrix, b)
        
        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    
    return result

def playfair_decrypt(text, key):
    if len(text) % 2 != 0:
        text += 'X'
    
    matrix = generate_playfair_matrix(key)
    
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_in_matrix(matrix, a)
        row2, col2 = find_in_matrix(matrix, b)
        
        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    
    return result

# Hill cipher functions
def matrix_vector_multiply(matrix, vector, mod):
    return [(sum(matrix[i][j] * vector[j] for j in range(3)) % mod) for i in range(3)]

def matrix_multiply(a, b, mod):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) % mod for j in range(3)] for i in range(3)]

def matrix_inverse(matrix, mod):
    det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
           - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
           + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])) % mod
    
    det_inv = pow(det, -1, mod)
    
    adj = [
        [(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) % mod,
         (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) % mod,
         (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) % mod],
        [(matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) % mod,
         (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) % mod,
         (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) % mod],
        [(matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) % mod,
         (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) % mod,
         (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod]
    ]
    
    return [[((det_inv * adj[i][j]) % mod) for j in range(3)] for i in range(3)]

def hill_encrypt(text, key):
    while len(text) % 3 != 0:
        text += 'x'

    key_matrix = [[ord(key[i*3+j]) - ord('a') for j in range(3)] for i in range(3)]
    
    ciphertext = ""
    for i in range(0, len(text), 3):
        block = [ord(c) - ord('a') for c in text[i:i+3]]
        encrypted = matrix_vector_multiply(key_matrix, block, 26)
        ciphertext += ''.join([chr(c % 26 + ord('A')) for c in encrypted])
    
    return ciphertext

def hill_decrypt(text, key):
    key_matrix = [[ord(key[i*3+j]) - ord('a') for j in range(3)] for i in range(3)]
    
    try:
        key_inverse = matrix_inverse(key_matrix, 26)
    except Exception as e:
        messagebox.showerror("Error", "Kunci tidak valid untuk dekripsi Hill Cipher (tidak memiliki invers matriks).")
        return ""
    
    block_size = 3
    if len(text) % block_size != 0:
        text += 'X' * (block_size - (len(text) % block_size))
    
    plaintext = ""
    for i in range(0, len(text), block_size):
        block = [ord(c) - ord('A') for c in text[i:i+block_size]]
        decrypted = matrix_vector_multiply(key_inverse, block, 26)
        plaintext += ''.join([chr(c % 26 + ord('a')) for c in decrypted])
 
    return plaintext

class CipherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Cipher")
        master.geometry("800x700")
        master.configure(bg="#eaeaea")

        # Frame untuk pemilihan cipher
        self.cipher_frame = ttk.LabelFrame(master, text="Pilih Metode Cipher", padding=(10, 10))
        self.cipher_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.cipher_method = ttk.Combobox(self.cipher_frame, values=["Vigenere", "Playfair", "Hill"], state="readonly")
        self.cipher_method.set("Vigenere")
        self.cipher_method.grid(row=0, column=0, padx=5, pady=5)

        # Frame untuk input sumber
        self.input_frame = ttk.LabelFrame(master, text="Sumber Input", padding=(10, 10))
        self.input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.input_source = ttk.Combobox(self.input_frame, values=["Teks", "File"], state="readonly")
        self.input_source.set("Teks")
        self.input_source.grid(row=0, column=0, padx=5, pady=5)
        self.input_source.bind("<<ComboboxSelected>>", self.toggle_input_method)

        self.text_input = ttk.Entry(self.input_frame, width=60)
        self.text_input.grid(row=1, column=0, padx=5, pady=5)

        self.file_path = tk.StringVar()
        self.file_input = ttk.Entry(self.input_frame, textvariable=self.file_path, state="disabled", width=40)
        self.file_input.grid(row=2, column=0, padx=5, pady=5)
        
        self.file_button = ttk.Button(self.input_frame, text="Pilih File", command=self.choose_file, state="disabled")
        self.file_button.grid(row=2, column=1, padx=5, pady=5)

        # Frame untuk key dan operasi
        self.key_frame = ttk.LabelFrame(master, text="Kunci dan Operasi", padding=(10, 10))
        self.key_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.key_input = ttk.Entry(self.key_frame, width=60)
        self.key_input.grid(row=0, column=0, padx=5, pady=5)

        self.operation = ttk.Combobox(self.key_frame, values=["Enkripsi", "Dekripsi"], state="readonly")
        self.operation.set("Enkripsi")
        self.operation.grid(row=1, column=0, padx=5, pady=5)

        # Tombol proses
        self.process_button = ttk.Button(master, text="Proses", command=self.process_cipher)
        self.process_button.grid(row=3, column=0, pady=10)

        # Frame untuk hasil
        self.result_frame = ttk.LabelFrame(master, text="Hasil", padding=(10, 10))
        self.result_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.result_display = tk.Text(self.result_frame, height=10, width=70, wrap=tk.WORD)
        self.result_display.pack(expand=True, fill=tk.BOTH)

        # Mengatur grid
        master.grid_columnconfigure(0, weight=1)

    def toggle_input_method(self, event=None):
        if self.input_source.get() == "Teks":
            self.text_input.config(state="normal")
            self.file_input.config(state="disabled")
            self.file_button.config(state="disabled")
        else:
            self.text_input.config(state="disabled")
            self.file_input.config(state="normal")
            self.file_button.config(state="normal")

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_path.set(file_path)

    def process_cipher(self):
        method = self.cipher_method.get()
        operation = self.operation.get()
        key = self.key_input.get()
        input_text = self.text_input.get() if self.input_source.get() == "Teks" else self.load_file_content()
        
        if not key or not input_text:
            messagebox.showerror("Error", "Masukkan kunci dan teks.")
            return

        try:
            if method == "Vigenere":
                result = (vigenere_encrypt(input_text, key) if operation == "Enkripsi" 
                          else vigenere_decrypt(input_text, key))
            elif method == "Playfair":
                result = (playfair_encrypt(input_text, key) if operation == "Enkripsi" 
                          else playfair_decrypt(input_text, key))
            elif method == "Hill":
                result = (hill_encrypt(input_text, key) if operation == "Enkripsi" 
                          else hill_decrypt(input_text, key))

            self.result_display.delete(1.0, tk.END)
            self.result_display.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def load_file_content(self):
        file_path = self.file_path.get()
        with open(file_path, 'r') as file:
            return file.read()

if __name__ == "__main__":
    root = tk.Tk()
    gui = CipherGUI(root)
    root.mainloop()
