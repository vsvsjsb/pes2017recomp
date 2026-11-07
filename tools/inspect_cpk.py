from pathlib import Path

p = Path("dt10_x36.cpk")
data = p.read_bytes()

print("File:", p.name)
print("Size:", len(data), "bytes")
print("Header:", data[:64].hex(" "))

for sig in (b"CPK ", b"@UTF", b"TOC ", b"ETOC", b"GTOC", b"ITOC"):
    pos = data.find(sig)
    print(sig.decode(), "offset:", pos)

Path("cpk-inspection.txt").write_text(
    f"File: {p.name}\nSize: {len(data)} bytes\nHeader: {data[:64].hex(' ')}\n",
    encoding="utf-8"
)
