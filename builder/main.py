def main():
	b = []

	print(b)

	for i in range(len(b)):
		m = i

		for j in range(i + 1, len(b)):
			if b[j] < b[m]:
				m = j

		c = b[i]
		b[i] = b[m]
		b[m] = c

	print(b)

if __name__ == '__main__':
	main()