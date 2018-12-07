#!/usr/bin/env python3

# 可变参数


def dynamic_params(*nums):
    result = 0
    for number in nums:
        result += number
    print(result)


dynamic_params(1, 2, 3, 4)
dynamic_params(*[1, 2, 3, 4])
dynamic_params(*(1, 2, 3, 4))

# 关键字参数


def keywords_params(name, **kw):
    print('name is %s, kw is %s' % (name, kw))


keywords_params('gt')
keywords_params('gt', city='Beijing')
keywords_params('gt', **{'city': 'Beijing', 'job': 'Engineer'})


def limit_keywords_params(name, *, city):
    print('name is %s, city is %s' % (name, city))


limit_keywords_params('gt', city='Beijing')


def limit_keywords_params2(name, *ext, city):
    print('name is %s, extInfo is %s, city is %s', % (name, ext, city))
