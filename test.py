#import modul Tkinter
from tkinter import *

# Fungsi menampilkan jendela utama
def kalkulator(lihat, side):
    mycalc = Frame(lihat, borderwidth=4, bd=4, bg="powder blue")
    mycalc.pack(side=side, expand=YES, fill=BOTH)
    return mycalc

def tombol(lihat, side, text, command=None, bg='grey'):
    mycalc = Button(lihat, text=text, command=command, bg=bg)
    mycalc.pack(side=side, expand=YES, fill=BOTH)
    return mycalc

class aplikasi(Frame):
    # Fungsi untuk penerapan tombol yang ada
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'sans-serif')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Kalkulator')
        
        display = StringVar()
        Entry(self, relief=FLAT, textvariable=display, bd=30, bg='light green').pack(side=TOP, expand=YES, fill=BOTH)
        
        for TombolAngka in ('123', '456', '789', '.0+', '/*-'):
            nomor = kalkulator(self, TOP)
            for a in TombolAngka:
                tombol(nomor, LEFT, a, lambda mycalc=display, q=a: mycalc.set(mycalc.get() + q))
                
        for Tombol_C in (['C']):
            hapus = kalkulator(self, RIGHT)
            for c in Tombol_C:
                tombol(hapus, RIGHT, c, lambda mycalc=display, q=c: mycalc.set(''), bg='green')
                
        SamaDengan = kalkulator(self,LEFT)
        for samadengan in '=':
            if samadengan == '=':
                TombolSama = tombol(SamaDengan, LEFT, samadengan)
                TombolSama.bind('<ButtonRelease-1>', lambda e,s=self, mycalc=display: s.hitung(mycalc), '+')
            else:
                TombolSama = tombol(SamaDengan, LEFT, samadengan, lambda mycalc=display, s=' %s ' % samadengan: mycalc.set(mycalc.get()+s))
    # Fungsi Perhitungan
    def hitung(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set('ERROR')
            
if __name__ == ' __main__ ':
    Tk.mainloop(aplikasi())
    