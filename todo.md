# TODO

- [ ] 调整成可配置版本
- [x] 完成 HTML 处理类(20240218)
- [ ] 汇总README.md
- [ ] 爬虫部分
- [ ] 增加本地sqlite存储


# bug-fix
- [x] 同一片文章多张图片会有问题(20240220)

```python
urllib3.exceptions.SSLError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1002)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/requests/adapters.py", line 486, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 847, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/retry.py", line 515, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='blog.sina.com.cn', port=443): Max retries exceeded with url: /s/blog_497675f20100c6rt.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1002)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/runpy.py", line 198, in _run_module_as_main
    return _run_code(code, main_globals, None,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/runpy.py", line 88, in _run_code
    exec(code, run_globals)
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/__main__.py", line 39, in <module>
    cli.main()
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 430, in main
    run()
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 284, in run_file
    runpy.run_path(target, run_name="__main__")
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 321, in run_path
    return _run_module_code(code, init_globals, run_name,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 135, in _run_module_code
    _run_code(code, mod_globals, init_globals,
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 124, in _run_code
    exec(code, run_globals)
  File "/Users/narglc/Code/Workplace/sina.blog.bak/script/main.py", line 34, in <module>
    articleAna.handle()
  File "/Users/narglc/Code/Workplace/sina.blog.bak/script/article_ana.py", line 32, in handle
    self.getAtcPage()
  File "/Users/narglc/Code/Workplace/sina.blog.bak/script/article_ana.py", line 40, in getAtcPage
    pageContent = getBlogPage(self.articleUrl, self.cookies, self.header)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/narglc/Code/Workplace/sina.blog.bak/script/download.py", line 5, in getBlogPage
    response = requests.get(url, cookies=cookies, headers=headers)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/adapters.py", line 517, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='blog.sina.com.cn', port=443): Max retries exceeded with url: /s/blog_497675f20100c6rt.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1002)')))


----
urllib3.exceptions.SSLError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1002)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/requests/adapters.py", line 486, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 847, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/retry.py", line 515, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='blog.sina.com.cn', port=443): Max retries exceeded with url: /s/blog_497675f20100bjaz.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1002)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/runpy.py", line 198, in _run_module_as_main
    return _run_code(code, main_globals, None,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/runpy.py", line 88, in _run_code
    exec(code, run_globals)
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/__main__.py", line 39, in <module>
    cli.main()
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 430, in main
    run()
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 284, in run_file
    runpy.run_path(target, run_name="__main__")
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 321, in run_path
    return _run_module_code(code, init_globals, run_name,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 135, in _run_module_code
    _run_code(code, mod_globals, init_globals,
  File "/Users/narglc/.vscode/extensions/ms-python.debugpy-2024.0.0-darwin-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 124, in _run_code
    exec(code, run_globals)
  File "/Users/narglc/Code/Workplace/sina.blog.bak/script/main.py", line 34, in <module>
    articleAna.handle()
  File "/Users/narglc/Code/Workplace/sina.blog.bak/script/article_ana.py", line 32, in handle
    self.getAtcPage()
  File "/Users/narglc/Code/Workplace/sina.blog.bak/script/article_ana.py", line 40, in getAtcPage
    pageContent = getBlogPage(self.articleUrl, self.cookies, self.header)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/narglc/Code/Workplace/sina.blog.bak/script/download.py", line 5, in getBlogPage
    response = requests.get(url, cookies=cookies, headers=headers)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/requests/adapters.py", line 517, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='blog.sina.com.cn', port=443): Max retries exceeded with url: /s/blog_497675f20100bjaz.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1002)')))
```

### 未完成文章
```
ArticleAna://blog.sina.com.cn/s/blog_497675f20100auxm.html fail, err:HTTPSConnectionPool(host='blog.sina.com.cn', port=443): Max retries exceeded with url: /s/blog_497675f20100auxm.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1002)')))

ArticleAna://blog.sina.com.cn/s/blog_497675f2010006z9.html fail, err:HTTPSConnectionPool(host='blog.sina.com.cn', port=443): Max retries exceeded with url: /s/blog_497675f2010006z9.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1002)')))
```