import zalgo

encoded = zalgo.process('Test text')
print(encoded)
decoded = zalgo.strip(encoded)
print(decoded)
