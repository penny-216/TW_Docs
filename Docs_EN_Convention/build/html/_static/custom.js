
// 在自定义 JavaScript 文件中添加以下代码
document.addEventListener('DOMContentLoaded', function() {
    // 获取侧边栏中的所有标题
    var sidebarHeaders = document.querySelectorAll('.sphinxsidebar h3, .sphinxsidebar h4');
    
    // 遍历所有标题
    for (var i = 0; i < sidebarHeaders.length; i++) {
        // 检查标题文本是否为 "This Page"
        if (sidebarHeaders[i].textContent.trim() === 'This Page') {
            // 隐藏该标题
            sidebarHeaders[i].style.display = 'none';
            break; // 找到后退出循环
        }
    }
});
