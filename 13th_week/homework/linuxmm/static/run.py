python3 <<EOF
import psutil as pu
import json
info = {}
info['cpu_count'] = pu.cpu_count()
info['cpu_percent'] = pu.cpu_percent()
mem = pu.virtual_memory()
info['mem_total'] = mem.total
info['mem_available'] = mem.available
info['mem_percent'] = mem.percent
info['mem_used'] = mem.used
info['mem_free'] = mem.free
data = json.dumps(info)
print(data)
EOF