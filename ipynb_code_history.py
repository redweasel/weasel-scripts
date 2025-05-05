# As it turns out, VSCode is saving an extensive history of
# which Jupyter Notebooks you have opened over the entire time you have used it.
# Along with that, it also saves the actual Notebooks, which can grow quite large.
# Here is a tool to visualize your usage of VSCode for Jupyter.

import os
import json
from datetime import datetime
from matplotlib import pyplot as plt

times = []
times_per_type = {}
path = os.path.expanduser("~/.config/Code/User/History")
for folder in os.listdir(path):
    # each folder is a notebook? anyway, there is many.
    with open(os.path.join(path, folder, "entries.json"), "r") as f:
        content = json.load(f)
        assert content["version"] == 1, "this script was written for version 1, not sure what happens with other versions. You can try to remove this assert."
        file = content["resource"]
        ext = file.split(".")[-1]
        for entry in content["entries"]:
            timestamp = entry["timestamp"]
            dt = datetime.fromtimestamp(timestamp / 1000) # why???
            times.append(dt)
            times_per_type[ext] = times_per_type.get(ext, []) + [dt]

plt.hist(times, bins=100)
plt.show()
times_per_type = list(times_per_type.items())
plt.hist([v for k, v in times_per_type], bins=100, label=[k for k, v in times_per_type], stacked=True)
plt.legend()
plt.show()
