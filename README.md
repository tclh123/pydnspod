# pydnspod

![](https://img.shields.io/pypi/pyversions/sa-tools-core)

pydnspod 是一个 DNSPod 国内版 API 的 Python SDK.

[DNSPod API Docs](https://github.com/DNSPod/dnspod-api-doc/)

# Installation

```
pip install pydnspod2
```

# 特性

- 支持自定义User-Agent
- 支持D令牌
- 发送请求前检查是否遗漏参数，避免无效请求
- 使用命名参数，可以单独指定特定api的返回结果的format、lang

# 使用方法

```python
from pydnspod import pydnspod

if __name__ == "__main__":
    login_email = ''
    login_password = ''
    api = pydnspod.Api(login_email, login_password)
    print api.version()

    user_manager=pydnspod.User(login_email, login_password)
    print user_manager.detail()

    domain_manager = pydnspod.Domain(login_email, login_password)
    print domain_manager.create(domain="domain.name")
    print domain_manager.info(domain="domain.name")
```
