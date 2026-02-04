import tkinter as tk
from tkinter import ttk, messagebox
import string
import random
import math
from collections import Counter

class ModernPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("800x700")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # Colors
        self.bg_color = '#000000'
        self.neon_green = '#39FF14'
        self.white = '#FFFFFF'
        self.dark_gray = '#1E1E1E'
        self.light_gray = '#2A2A2A'
        
        self.current_password = ""
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container with padding
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill='both', padx=40, pady=30)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🔐PASSWORD GENERATOR",
            font=('Helvetica', 28, 'bold'),
            fg=self.neon_green,
            bg=self.bg_color
        )
        title_label.pack(pady=(0, 5))
        
        # Catchy caption
        caption_label = tk.Label(
            main_frame,
            text=" Your Security Companion",
            font=('Helvetica', 12, 'italic'),
            fg=self.white,
            bg=self.bg_color
        )
        caption_label.pack(pady=(0, 35))
        
        # Password Length Section
        length_frame = tk.Frame(main_frame, bg=self.bg_color)
        length_frame.pack(pady=15)
        
        length_label = tk.Label(
            length_frame,
            text="Password Length:",
            font=('Helvetica', 16, 'bold'),
            fg=self.white,
            bg=self.bg_color
        )
        length_label.pack(side='left', padx=(0, 15))
        
        self.length_var = tk.StringVar(value='13')
        self.length_entry = tk.Entry(
            length_frame,
            textvariable=self.length_var,
            font=('Helvetica', 14),
            fg=self.white,
            bg=self.dark_gray,
            width=10,
            insertbackground=self.white,
            relief='flat',
            bd=0
        )
        self.length_entry.pack(side='left', ipady=8, ipadx=10)
        
        # Generate Button
        self.generate_btn = tk.Button(
            main_frame,
            text="GENERATE PASSWORD",
            font=('Helvetica', 14, 'bold'),
            fg='#000000',
            bg=self.white,
            activebackground='#CCCCCC',
            activeforeground='#000000',
            relief='flat',
            cursor='hand2',
            command=self.generate_password,
            bd=0,
            padx=30,
            pady=15
        )
        self.generate_btn.pack(pady=25)
        
        # Generated Password Section
        pwd_label = tk.Label(
            main_frame,
            text="Generated Password:",
            font=('Helvetica', 16, 'bold'),
            fg=self.white,
            bg=self.bg_color,
            anchor='w'
        )
        pwd_label.pack(fill='x', pady=(10, 5))
        
        # Password display with frame
        pwd_frame = tk.Frame(main_frame, bg=self.light_gray, relief='flat', bd=2)
        pwd_frame.pack(fill='x', pady=(0, 10))
        
        self.password_text = tk.Text(
            pwd_frame,
            font=('Courier New', 13),
            fg=self.white,
            bg=self.dark_gray,
            height=2,
            wrap='word',
            relief='flat',
            bd=0,
            padx=15,
            pady=15
        )
        self.password_text.pack(fill='both', expand=True, padx=2, pady=2)
        self.password_text.config(state='disabled')
        
        # Copy Button
        self.copy_btn = tk.Button(
            main_frame,
            text="📋 COPY TO CLIPBOARD",
            font=('Helvetica', 12, 'bold'),
            fg='#000000',
            bg=self.white,
            activebackground='#CCCCCC',
            activeforeground='#000000',
            relief='flat',
            cursor='hand2',
            command=self.copy_password,
            bd=0,
            padx=25,
            pady=10,
            state='disabled'
        )
        self.copy_btn.pack(pady=10)
        
        # Shannon Entropy Section
        entropy_label = tk.Label(
            main_frame,
            text="Shannon Entropy:",
            font=('Helvetica', 16, 'bold'),
            fg=self.white,
            bg=self.bg_color,
            anchor='w'
        )
        entropy_label.pack(fill='x', pady=(20, 5))
        
        # Entropy display with frame
        entropy_frame = tk.Frame(main_frame, bg=self.light_gray, relief='flat', bd=2)
        entropy_frame.pack(fill='x')
        
        self.entropy_text = tk.Text(
            entropy_frame,
            font=('Helvetica', 12),
            fg=self.white,
            bg=self.dark_gray,
            height=4,
            wrap='word',
            relief='flat',
            bd=0,
            padx=15,
            pady=15
        )
        self.entropy_text.pack(fill='both', expand=True, padx=2, pady=2)
        self.entropy_text.config(state='disabled')
        
    def calculate_shannon_entropy(self, password):
        """Calculate Shannon entropy of the password for character distribution"""
        if not password:
            return 0.0
        
        counter = Counter(password)
        length = len(password)
        
        entropy_per_char = 0.0
        for count in counter.values():
            probability = count / length
            entropy_per_char -= probability * math.log2(probability)
        
        return entropy_per_char
    
    def calculate_password_entropy(self, length, pool_size):
        """Calculate password entropy based on pool size and length"""
        return length * math.log2(pool_size)
    
    def generate_password(self):
        """Generate password when button is clicked"""
        try:
            n = int(self.length_var.get())
            if n < 8:
                messagebox.showwarning('Invalid Length', 'Password length must be at least 8 characters for security')
                return
            if n > 100:
                messagebox.showwarning('Invalid Length', 'Password length cannot exceed 100 characters')
                return
        except ValueError:
            messagebox.showwarning('Invalid Input', 'Please enter a valid number')
            return
        
        # Create character pool
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        
        s = []
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        s.extend(s4)
        
        random.shuffle(s)
        
        # Generate password
        password = ''.join(s[0:n])
        self.current_password = password
        
        # Calculate character pool size
        charset_size = len(string.ascii_lowercase + string.ascii_uppercase + 
                          string.digits + string.punctuation)
        
        # Calculate Shannon entropy
        shannon_entropy = self.calculate_shannon_entropy(password)
        
        # Calculate password entropy
        password_entropy = self.calculate_password_entropy(n, charset_size)
        
        # Display password
        self.password_text.config(state='normal')
        self.password_text.delete('1.0', 'end')
        self.password_text.insert('1.0', password)
        self.password_text.config(state='disabled')
        
        # Display entropy info
        entropy_info = f"Password Entropy: {password_entropy:.2f} bits\n"
        entropy_info += f"Character Distribution Entropy: {shannon_entropy:.4f} bits/char\n"
        entropy_info += f"Crack Time (1B guesses/sec): {2**(password_entropy-1) / 1e9:.2e} seconds"
        
        self.entropy_text.config(state='normal')
        self.entropy_text.delete('1.0', 'end')
        self.entropy_text.insert('1.0', entropy_info)
        self.entropy_text.config(state='disabled')
        
        # Enable copy button
        self.copy_btn.config(state='normal')
    
    def copy_password(self):
        """Copy password to clipboard"""
        if self.current_password:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.current_password)
            
            # Change button text temporarily to show feedback
            original_text = self.copy_btn.cget('text')
            self.copy_btn.config(text='✓ COPIED!')
            self.root.after(2000, lambda: self.copy_btn.config(text=original_text))

if __name__ == '__main__':
    root = tk.Tk()
    app = ModernPasswordGenerator(root)
    root.mainloop()
