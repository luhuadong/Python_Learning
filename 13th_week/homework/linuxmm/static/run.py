python3 <<EOF
import psutil as pu
import json
info = {}
mem = pu.virtual_memory()
info['mem_total'] = mem.total
info['mem_available'] = mem.available
info['mem_percent'] = mem.percent
info['mem_used'] = mem.used
info['mem_free'] = mem.free
print(info)
EOF