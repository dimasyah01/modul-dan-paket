import rumus as rms

def main():
	p = int(input("Masukkan Panjang\t: "))
	l = int(input("Masukkan Lebar\t\t: "))
	t = int(input("Masukkan Tinggi\t\t: "))
	s = int(input("Masukkan Sisi\t\t: "))
	r = int(input("Masukkan Jari-Jari\t: "))

	luasBalok = rms.luasBalok(p,l,t)
	luasKubus = rms.luasKubus(s)
	luasBola = rms.luasBola(r)

	print("BALOK")
	print("Panjang\t: ",p)
	print("Lebar\t: ",l)
	print("Tinggi\t: ",t)
	print("Luas\t= ",luasBalok)

	print("\nKUBUS")
	print("Sisi\t: ",s)
	print("Luas\t= ",luasKubus)

	print("\nBola")
	print("Jari-Jari\t: ",r)
	print("Luas\t\t= ",luasBola)

if __name__ == "__main__":
	main()