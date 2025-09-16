plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置支持中文
center = (5, 5) #圆心
radius = 3  #圆半径
width = 5   #椭圆宽度
height = 3  #椭圆高度
angle = 0  #旋转角度

figure, ax = plt.subplots(3, 3)

#标注
for i in range(3):
    for j in range(3):
        ellipse = patches.Ellipse(center, width=width, height=height, angle=angle * 45)	#创建ellipse实例
        ax[i, j].add_patch(ellipse)		#添加实例

        dx = 4 * round(np.cos(np.pi / 4 * angle), 2)	#计算箭头X增量
        dy = 4 * round(np.sin(np.pi / 4 * angle), 2)	#计算箭头Y增量

        ax[i, j].arrow(center[0], center[1], dx=dx, dy=dy, width=0.08)	#画箭头
        ax[i, j].plot(center[0], center[1], marker='o', markersize=5 , markerfacecolor='#000000')	#画中心
        ax[i, j].set_xlim([0, 10])  #设置轴范围
        ax[i, j].set_ylim([0, 10])  #设置轴范围
        ax[i, j].text(center[0], center[1], '中心', fontsize=15)  #标注中心点
        ax[i, j].set_title(str(angle * 45) + '°')	#设置标题
        angle += 1

plt.show()
