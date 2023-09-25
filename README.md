# Python-Study
Python日常工作 demo测试



# 虚拟环境

```markdown
# 安装
pip show virtualenv
pip install virtualenv
# 新建
virtualenv <venv_name>
# 激活 命令结束会发现命令行提示符前缀发生变更 后面就是pip之类的使用了
.\<venv_name>\Scripts\activate
source /<venv_name>/bin/activate
# 退出虚拟环境
deactivate
# 删除
rmdir /s /q <venv_name>
rm -rf xxx
```

虚拟环境新建结束，编译器配置一些项目的python解释器，选择新建的那个虚拟环境就可以切换了