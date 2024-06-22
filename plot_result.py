import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
# plt.rcParams['font.sans-serif'] = 'simhei'
# plt.rcParams['axes.unicode_minus']=False
 
def zoom_enlarge_1(axes, enlarge_position, x1, x2, y1, y2):
    xmin, xmax = x1, x2  # define the coordinates of the magnification section
    ymin, ymax = y1, y2  
 
    ax_zoom = plt.axes(enlarge_position)  # enlarge position means the subfigure position in the figure
    plt.plot(d2[:,0],d2[:,2], color='tomato', linewidth =2)
    plt.plot(d2[:,0],d3[:,2], color='deepskyblue', linewidth =2)
    plt.plot(d2[:,0],d4[:,2], color='springgreen', linewidth =2)
    plt.plot(d2[:,0],d5[:,2], color='deeppink', linewidth =2) # above plot the selected curves
    ax_zoom.set_xlim([xmin, xmax])  
    ax_zoom.set_ylim([ymin, ymax])  # above set the subfigure axis
    # ax_zoom.set_xlabel('X')  
    # ax_zoom.set_ylabel('Y')  
    # ax_zoom.set_title('Zoomed In')  
 
    rect = plt.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, fill=False, edgecolor='r', linewidth=2)  
    axes.add_patch(rect)  # show the selected part of the figure with highted line in red color
    
    
def zoom_enlarge_2(axes, enlarge_position, x1, x2, y1, y2):
    xmin, xmax = x1, x2  
    ymin, ymax = y1, y2  
 
    ax_zoom = plt.axes(enlarge_position)  
    plt.plot(d2[:,0],d2[:,1], color='tomato', linewidth =2)
    plt.plot(d2[:,0],d3[:,1], color='deepskyblue', linewidth =2)
    plt.plot(d2[:,0],d4[:,1], color='springgreen', linewidth =2)
    plt.plot(d2[:,0],d5[:,1], color='deeppink', linewidth =2)
    ax_zoom.set_xlim([xmin, xmax])  
    ax_zoom.set_ylim([ymin, ymax])  
    # ax_zoom.set_xlabel('X')  
    # ax_zoom.set_ylabel('Y')  
    # ax_zoom.set_title('Zoomed In')  
 
    rect = plt.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, fill=False, edgecolor='r', linewidth=2)  
    axes.add_patch(rect)  

 
d2 = pd.read_csv("/demo/ARN-LSM/runs/models/UT-1/ARN_no_rel_att_after_s1/summary.csv")
d2 = np.array(d2)
print(d2.shape)
 
d3 = pd.read_csv("/demo/ARN-LSM/runs/models/UT-1/ARN_no_rel_att_before_s1/summary.csv")
d3 = np.array(d3)
print(d3.shape)
 
d4 = pd.read_csv("/demo/ARN-LSM/runs/models/UT-1/ARN_no_rel_ave_after_s1/summary.csv")
d4 = np.array(d4)
print(d4.shape)
 
d5 = pd.read_csv("/demo/ARN-LSM/runs/models/UT-1/ARN_no_rel_ave_before_s1/summary.csv")
d5 = np.array(d5)
print(d5.shape) # above load curves with pandas and convert data to numpy format
 
 
config = {
    "font.family":'serif',
    "font.size": 18,
    "mathtext.fontset":'stix',
    "font.serif": ['Times new roman'],
}
rcParams.update(config) # set the text style
 
 
 
plt.figure(figsize=(14,6))
ax1 = plt.subplot(121)
plt.plot(d2[:,0],d2[:,2], color='tomato', linewidth =2)
plt.plot(d2[:,0],d3[:,2], color='deepskyblue', linewidth =2)
plt.plot(d2[:,0],d4[:,2], color='springgreen', linewidth =2)
plt.plot(d2[:,0],d5[:,2], color='deeppink', linewidth =2)# above show curves
plt.title('Train loss',fontsize=20, fontweight='bold')
plt.ylabel('Loss',fontsize=18)
plt.xlabel('Epoch',fontsize=18)
plt.legend(['block = 2', 'block = 3', 'block = 4', 'block = 5'], loc='upper right',fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.yticks(fontproperties='Times New Roman', size=18)
plt.xticks(fontproperties='Times New Roman', size=18)
zoom_enlarge_1(ax1, (0.25, 0.3, 0.2, 0.2), 3, 20, 0.00, 0.015) # use the enlarge function
 
bwith = 1.5 # define the with of the figure borders
TK = plt.gca()
TK.spines['bottom'].set_linewidth(bwith)
TK.spines['left'].set_linewidth(bwith)
TK.spines['top'].set_linewidth(bwith)
TK.spines['right'].set_linewidth(bwith)
 
# summarize history for loss
# plt.figure(figsize=(7,6))
ax2 = plt.subplot(122)
plt.plot(d2[:,0],d2[:,1], color='tomato', linewidth =2)
plt.plot(d2[:,0],d3[:,1], color='deepskyblue', linewidth =2)
plt.plot(d2[:,0],d4[:,1], color='springgreen', linewidth =2)
plt.plot(d2[:,0],d5[:,1], color='deeppink', linewidth =2)
plt.title('Train acc',fontsize=20, fontweight='bold')
plt.ylabel('Acc',fontsize=18)
plt.xlabel('Epoch',fontsize=18)
plt.legend(['block = 2', 'block = 3', 'block = 4', 'block = 5'], loc='lower right',fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.yticks(fontproperties='Times New Roman', size=18)
plt.xticks(fontproperties='Times New Roman', size=18)
zoom_enlarge_2(ax2, (0.65, 0.5, 0.2, 0.2), 3, 20, 0.95, 1.00)
 
 
bwith = 1.5 
TK = plt.gca()
TK.spines['bottom'].set_linewidth(bwith)
TK.spines['left'].set_linewidth(bwith)
TK.spines['top'].set_linewidth(bwith)
TK.spines['right'].set_linewidth(bwith)
 
plt.savefig('loss_different_block.png', dpi=600, bbox_inches='tight')# save figure
plt.savefig('loss_different_block.eps', dpi=600, bbox_inches='tight')
plt.show()
 