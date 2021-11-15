# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

fig = plt.figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(1, 1, 1)

ax.set_xlim(0, 360)
ax.set_ylim(-1, 1)

DC_to_FC = ax.transData.transform
FC_to_DC = ax.transData.inverted().transform

NDC_to_FC = ax.transAxes.transform
FC_to_NDC = ax.transAxes.inverted().transform

NFC_to_FC = fig.transFigure.transform
FC_to_NFC = fig.transFigure.inverted().transform


print(NFC_to_FC([1, 1]))  # (600,500)
print(NDC_to_FC([1, 1]))  # (540,440)
print(DC_to_FC([360, 1]))  # (540,440)

DC_to_NDC = lambda x: FC_to_NDC(DC_to_FC(x))

print(DC_to_NDC([0, -1]))  # (0.0, 0.0)
print(DC_to_NDC([180, 0]))  # (0.5, 0.5)
print(DC_to_NDC([360, 1]))  # (1.0, 1.0)
