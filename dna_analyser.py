dna = input("Enter DNA sequence: ")

dna = dna.upper()

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

total = len(dna)

gc_content = ((g + c) / total) * 100

print("A count:", a)
print("T count:", t)
print("G count:", g)
print("C count:", c)

print("Total length:", total)
print("GC Content:", gc_content, "%")
