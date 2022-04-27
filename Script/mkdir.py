import os
i = 1
file = "SalesManagementTest"
while i <= 10:
    if i < 10:
        path = 'C:/Users/msi/Pictures/Saved Pictures/%s/test_0%i' % (file, i)
    else:
        path = 'C:/Users/msi/Pictures/Saved Pictures/%s/test_%i' % (file, i)
    if not os.path.isdir(path):  # 如果 test_data1 该文件不存在，就创建该文件
        os.mkdir(path)
    i += 1