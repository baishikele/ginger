
# 解决两个问题：1，url冗余过长，采用prefex  2，blueprint是用在分流模块而不是用来分视图函数的
class RedPrint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefex=None):
        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefex+rule, endpoint, f, **options)
