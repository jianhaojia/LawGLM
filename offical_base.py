import requests
from urllib.parse import urljoin, urlencode
import json
team_token='3A0FF2F050B5CD21E10254935AB79768D737BF1015890A0B'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 3A0FF2F050B5CD21E10254935AB79768D737BF1015890A0B'
}


url = "https://comm.chatglm.cn/law_api/"
def search_company_name_by_info(key: str, value: str):
    finallurl=urljoin(url,'search_company_name_by_info')
    data = {
        "key": key,
        'value': value
    }
    max_retries=3
    for attempt in range(max_retries):
        try:
            rsp = requests.post(finallurl, json=data, headers=headers)
            return rsp.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 1 * (2 ** attempt)  # 指数退避策略
            else:
                print("已达到最大重试次数，放弃请求。")
                raise

def get_company_info(company_name: str):
    finallurl=urljoin(url,'get_company_info')
    data = {
        "company_name": company_name
    }
    max_retries=3
    for attempt in range(max_retries):
        try:
            rsp = requests.post(finallurl, json=data, headers=headers)
            return rsp.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 1 * (2 ** attempt)  # 指数退避策略
            else:
                print("已达到最大重试次数，放弃请求。")
                raise

def getcompanyinfo(key: str, value: str):
    """"公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期",
    "法人代表", "总经理","董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱",
    "入选指数", "主营业务", "经营范围","机构简介", "每股面值", "首发价格", "首发募资净额", '首发主承销商']"""
    result = []
    count=0
    if key=="公司名称":
        result.append(get_company_info(value))
    else:
        names=search_company_name_by_info(key,value)
        print(names)
        if names is None or "查询失败" not in names:
            if len(names) == 1:
                result.append(get_company_info(str(names['公司名称'])))
            else:
                for name in names:
                    result.append(get_company_info(str(name['公司名称'])))
    if result is None and (key!="曾用简称" or key!="公司简称"):
        result=getcompanyregisterinfo("曾用简称",value)
        if result is None and key!="公司简称":
            result = getcompanysubinfo("公司简称", value)
    print("基本信息")
    return result

def search_company_name_by_register(key: str, value: str):
    finallurl=urljoin(url,'search_company_name_by_register')
    data = {
        "key": key,
        'value': value
    }
    max_retries=3
    for attempt in range(max_retries):
        try:
            rsp = requests.post(finallurl, json=data, headers=headers)
            return rsp.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 1 * (2 ** attempt)  # 指数退避策略
            else:
                print("已达到最大重试次数，放弃请求。")
                raise

def get_company_register(company_name: str):
    finallurl=urljoin(url,'get_company_register')
    data = {
        "company_name": company_name
    }
    max_retries=3
    for attempt in range(max_retries):
        try:
            rsp = requests.post(finallurl, json=data, headers=headers)
            return rsp.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 1 * (2 ** attempt)  # 指数退避策略
            else:
                print("已达到最大重试次数，放弃请求。")
                raise

def getcompanyregisterinfo(key: str, value: str):
    """"公司名称", "登记状态", "统一社会信用代码", "注册资本", "成立日期",
    "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名"""
    result = []

    if key=="公司名称":
        result.append(get_company_register(value))
    else:
        names=search_company_name_by_register(key,value)
        print(names)
        if names is None or "查询失败" not in names:
            if len(names) == 1:
                result.append(get_company_register(str(names['公司名称'])))
            else:
                for name in names:
                    result.append(get_company_register(str(name['公司名称'])))
    print("注册信息")
    print(result)
    if is_valid_list(result)and key !="曾用名":
        getcompanyregisterinfo("曾用名", value)
    return result

def search_company_name_by_sub_info(key: str, value: str):
    finallurl=urljoin(url,'search_company_name_by_sub_info')
    data = {
        "key": key,
        'value': value
    }
    max_retries=3
    for attempt in range(max_retries):
        try:
            rsp = requests.post(finallurl, json=data, headers=headers)
            return rsp.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 1 * (2 ** attempt)  # 指数退避策略
            else:
                print("已达到最大重试次数，放弃请求。")
                raise

def get_sub_company_info(company_name: str):
    finallurl=urljoin(url,'get_sub_company_info')
    data = {
        "company_name": company_name
    }
    max_retries=3
    for attempt in range(max_retries):
        try:
            rsp = requests.post(finallurl, json=data, headers=headers)
            return rsp.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 1 * (2 ** attempt)  # 指数退避策略
            else:
                print("已达到最大重试次数，放弃请求。")
                raise

def getcompanysubinfo(key: str, value: str):
    """关联上市公司股票代码", "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额", "公司名称"""
    result = []

    if key=="公司名称" and len(key)!=4 :
        result.append(get_sub_company_info(value))
    else:
        newkey=key
        if len(key)==4:
            newkey="关联上市公司股票简称"
        print(newkey+":"+value)
        names=search_company_name_by_sub_info(newkey,value)
        print(names)
        if names is None or "查询失败" not in names:
            if len(names) == 1:
                result.append(get_sub_company_info(str(names['公司名称'])))
            else:
                for name in names:
                    result.append(get_sub_company_info(str(name['公司名称'])))
    print("关联信息")
    print(result)
    if result ==[] and  key!="关联上市公司全称":
        result=getcompanysubinfo("关联上市公司全称", value)

    return result



def getSpecialinfo(key: str, value: str,need:str):
    baseinfo=""""公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期",
    "法人代表", "总经理","董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱",
    "入选指数", "主营业务", "经营范围","机构简介", "每股面值", "首发价格", "首发募资净额", "首发主承销商" """
    reinfo="""["公司名称", "登记状态", "统一社会信用代码", "注册资本", "成立日期",
 "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名"]"""
    suinfo="""关联上市公司股票代码", "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额", "公司名称"""

    output = []
    if key=="公司名称":
        if need in baseinfo:
            results=getcompanyinfo(key,value)
            for result in results:
                return {key: value, need: result[need]}
        elif need in reinfo:
            results=getcompanyregisterinfo(key,value)
            for result in results:

                return {key: value, need: result[need]}
        elif need in suinfo:
            results=get_sub_company_info(key,value)
            for result in results:
                return {key: value, need: result[need]}
    else:
        if key in baseinfo:
            results=getcompanyinfo(key,value)
            for result in results:
                name=result['公司名称']
                output.append(getSpecialinfo('公司名称' ,name, need))
        elif key in reinfo:
            results=getcompanyregisterinfo(key,value)
            for result in results:
                name=result['公司名称']
                output.append(getSpecialinfo('公司名称' ,name, need))
        elif key in suinfo:
            print("suinfo")
            results=getcompanysubinfo(key,value)
            for result in results:
                name=result['公司名称']
                output.append(getSpecialinfo('公司名称' ,name, need))
        return output

def merge_dicts_sorted(dict1, dict2, dict3):

    merged_dict = {}
    merged_dict.update(dict1)
    merged_dict.update(dict2)
    merged_dict.update(dict3)

    # 按照字典序排序并返回结果
    sorted_dict = {k: merged_dict[k] for k in sorted(merged_dict.keys())}
    return sorted_dict

#通过公司名称获取所有信息
def getCompanyInfoByCompanyName(company_name:str):
    baseinfo=""""公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期",
    "法人代表", "总经理","董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱",
    "入选指数", "主营业务", "经营范围","机构简介", "每股面值", "首发价格", "首发募资净额", "首发主承销商" """
    reinfo="""["公司名称", "登记状态", "统一社会信用代码", "注册资本", "成立日期",
 "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名"]"""
    suinfo="""关联上市公司股票代码", "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额", "公司名称"""

    companyinfo=get_company_info(company_name)

    registerinfo=get_company_register(company_name)

    subinfo=get_sub_company_info(company_name)


    result = merge_dicts_sorted(companyinfo, registerinfo, subinfo)
    return result

def merge_dicts(*args):
    merged_list = []

    seen = set()  # 用于记录已经添加过的字典项

    for data in args:
        if isinstance(data, dict):
            # 将字典项转换为元组，并使用集合进行去重
            item = tuple(data.items())
            if item not in seen:
                seen.add(item)
                merged_list.append(data)
        elif isinstance(data, list):
            for d in data:
                if isinstance(d, dict):
                    # 将字典项转换为元组，并使用集合进行去重
                    item = tuple(d.items())
                    if item not in seen:
                        seen.add(item)
                        merged_list.append(d)

    return merged_list

#通过KV获取公司名字
def getCompanyNameByKeyValue(key,value):

    companyinfo=search_company_name_by_info(key,value)
    registerinfo=search_company_name_by_register(key,value)
    subinfo=search_company_name_by_sub_info(key,value)
    result=merge_dicts(companyinfo,registerinfo,subinfo)
    print(result)
    return result



def searchInto(key,value):
    companyinfo = search_company_name_by_info(key, value)
    # print("base查询：" + str(companyinfo))
    registerinfo = search_company_name_by_register(key, value)
    # print("register查询：" + str(registerinfo))
    subinfo = search_company_name_by_sub_info(key, value)
    # print("subinfo查询：" + str(subinfo))
    result = merge_dicts(companyinfo, registerinfo, subinfo)
    print(result)
    return result
# def appendAllInfo(key,value)

def process_data(data_list, keys ,default_key='公司名称'):
    all_keys = [default_key] + keys  # 包含默认键和额外指定的键的列表
    result = []  # 用于存储最终结果的列表
    seen = set()  # 用于跟踪已处理的公司名称

    for data in data_list:
        # 确保 data 是字典
        if isinstance(data, dict):
            # 获取默认键的值
            key_value = data.get(default_key, None)
            # 如果公司名称未见过，则处理该项
            if key_value and key_value not in seen:
                # 将公司名称添加到已见集合中
                seen.add(key_value)
                # 过滤出所有需要的键，并且缺少的键设为 None
                filtered_data = {k: data.get(k, None) for k in all_keys}
                result.append(filtered_data)

    return result  # 返回处理后的结果列表


def mergeAndDeduplicateCompanyLists(keyValueList):
    # 使用集合来去重
    seen = set()
    merged_list = []

    for item in keyValueList:
        company_name = item.get('公司名称')
        if company_name and company_name not in seen:
            seen.add(company_name)
            merged_list.append({'公司名称': company_name})

    return merged_list
def getNumOfCompanyBykeyValue(key,value):
    all_companies=set()
    company_list =getCompanyNameByKeyValue(key,value)
    for company in company_list:
        company_name = company['公司名称']
        all_companies.add(company_name)
    formatted_list = [{'公司名称': company_name} for company_name in all_companies]
    num_elements = len(formatted_list)
    print(num_elements)
    print(all_companies)
    return f"""有相关信息{str(formatted_list)}，通过计算,已经确定我们想知道的公司数量是{num_elements},"""

# getNumOfCompanyBykeyValue('所属行业','通用设备制造业')
def getCompanyInfoByCompanyNameList(company_names, require):
    data_list = []
    for company_name in company_names:
        temp=getCompanyInfoByCompanyName(company_name)
        data_list.append(temp)  # 获取每个公司名称对应的数据字典

    result = process_data(data_list, keys=require)  # 使用 process_data 处理数据列表

    return result

def getComanyInfoByKeyValue(key,value,requirements):
    a=[]
    companys=getCompanyNameByKeyValue(key,value)
    for item in companys:
        company_name = item['公司名称']
        a.append(company_name)
    result=getCompanyInfoByCompanyNameList(a,requirements)
    return result

""""公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期",
    "法人代表", "总经理","董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱",
    "入选指数", "主营业务", "经营范围","机构简介", "每股面值", "首发价格", "首发募资净额", "首发主承销商" """


"""["公司名称", "登记状态", "统一社会信用代码", "注册资本", "成立日期",
 "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名"]"""

"""关联上市公司股票代码", "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额", "公司名称"""


def is_valid_list(lst):
    # 检查列表是否为空
    if not lst:
        return False

    # 检查是否是 [[], [], ...] 的格式
    if all(isinstance(i, list) and not i for i in lst):
        return False

    return True

def is_english_string(s):
    allowed_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,!?;:'\"-()[]{}0123456789")
    return all(c in allowed_chars for c in s)


def is_invalid_return(result, requirement):
    # 判断是否为空列表或者嵌套空列表
    if result == [] or result == [[]]:
        return True

    # 判断特定结构的无效返回
    if isinstance(result, list) and len(result) >= 2:
        # 第一个元素是公司名称和参股比例
        first_element_valid = isinstance(result[0], dict) and '公司名称' in result[0] and '上市公司参股比例' in result[0]

        # 后续元素是requirement的值和None
        remaining_elements_valid = all(
            isinstance(element, tuple) and len(element) == 2 and element[1] is None for element in result[1:])

        # 从requirement的第二个元素开始检查
        requirement_match = all(element[0] == req for element, req in zip(result[1:], requirement[1:]))

        if first_element_valid and remaining_elements_valid and requirement_match:
            return True

    # 如果不满足无效返回的任何一种情况，则认为是有效返回
    return False



""""公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期",
    "法人代表", "总经理","董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱",
    "入选指数", "主营业务", "经营范围","机构简介", "每股面值", "首发价格", "首发募资净额", "首发主承销商" """


"""["公司名称", "登记状态", "统一社会信用代码", "注册资本", "成立日期",
 "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名"]"""

"""关联上市公司股票代码", "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额", "公司名称"""

"标题,案号,文书类型,原告,被告,原告律师,被告律师,案由,审理法条依据,涉案金额,判决结果,胜诉方,文件名"

def getComanyListInfoByKeyValueList(keyValueList,requirements):
    a=set()
    tempresult=''
    for key,value in keyValueList:
        temp = getComanyInfoByKeyValue(key, value, requirements)
        if (key=='公司名称' or  key == '关联上市公司全称') and len(value)<=4:
            b=['关联上市公司股票简称','公司简称','曾用简称','曾用名']
            c = set()
            for case in b:
                temp = getComanyInfoByKeyValue(case,value, requirements)
                if(is_invalid_return(temp,requirements)):
                    c = merge_dicts(c, temp)


        if key=='公司名称' and is_invalid_return(key, requirements):
                temp = getComanyInfoByKeyValue('关联上市公司全称', value, requirements)

        if is_english_string(value) :
            temp2 = getComanyInfoByKeyValue('英文名称', value, requirements)
            temp=merge_dicts(temp2)

        a = merge_dicts(a,temp)

    print("接口返回")
    print(a)
    return a
# a=getComanyInfoByKeyValue('英文名称', "Tianyang New Materials (Shanghai) Technology Co., Ltd.", ["公司名称","上市公司参股比例"])
# print(a)
print(str(is_invalid_return(a,["公司名称","上市公司参股比例"])))
a=getComanyListInfoByKeyValueList([["英文名称","Tianyang New Materials (Shanghai) Technology Co., Ltd."]],["关联上市公司股票代码","关联上市公司股票简称","关联上市公司全称","上市公司关系","上市公司参股比例"])
print(a)
print(str(is_invalid_return(a,["公司名称","上市公司参股比例"])))
# getComanyListInfoByKeyValueList([["关联上市公司全称","Tianyang New Materials (Shanghai) Technology Co., Ltd."]],["关联上市公司股票代码","关联上市公司股票简称","关联上市公司全称","上市公司关系","上市公司参股比例"])
# a=get_sub_company_info("安睿智达（成都）科技有限公司")
# a= getComanyInfoByKeyValue('公司名称', "安睿智达（成都）科技有限公司", ["关联上市公司全称"])
# print(a)
def search_case_num_by_legal_document(key: str, value: str):
    finallurl=urljoin(url,'search_case_num_by_legal_document')
    data = {
        "key": key,
        'value': value
    }
    max_retries=3
    for attempt in range(max_retries):
        try:
            rsp = requests.post(finallurl, json=data, headers=headers)
            return rsp.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 1 * (2 ** attempt)  # 指数退避策略
            else:
                print("已达到最大重试次数，放弃请求。")
                raise

def get_legal_document(case_num: str):
    finallurl=urljoin(url,'get_legal_document')
    data = {
        "case_num": case_num
    }
    max_retries=3
    for attempt in range(max_retries):
        try:
            rsp = requests.post(finallurl, json=data, headers=headers)
            return rsp.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 1 * (2 ** attempt)  # 指数退避策略
            else:
                print("已达到最大重试次数，放弃请求。")
                raise

def getlegaldocument(key: str, value: str):
    result = []
    if key=="案号":
        result.append(get_legal_document(value))
    else:
        names=search_case_num_by_legal_document(key,value)
        if names is None or "查询失败" not in names:
            if len(names) == 1:
                result.append(get_legal_document(str(names['案号'])))
            else:
                for name in names:
                    result.append(get_legal_document(str(name['案号'])))
    print(result)
    return result

"标题,案号,文书类型,原告,被告,原告律师,被告律师,案由,审理法条依据,涉案金额,判决结果,胜诉方,文件名"
def getCaseListInfoByKeyValueList(keyValueList,requirements):
    a=set()
    for key,value in keyValueList:
        cases = search_case_num_by_legal_document(key, value)
        temp=merge_dicts(cases)
        a=merge_dicts(temp)
    data_list = []
    print(a)
    for item in a:
        for key, value in item.items():
            temp = get_legal_document(value)
            data_list.append(temp)  # 获取每个公司名称对应的数据字典
            result=process_data(data_list, keys=requirements,default_key='案号')
    print("接口返回")
    print(result)
    return result

# getCaseListInfoByKeyValueList([["被告","九牧王股份有限公司"]],["原告律师","案号"])
def getNumOfCaseByKeyValue(key,value):

    cases = search_case_num_by_legal_document(key, value)
    data_list = []
    if len(cases)!=1:
        for item in cases:
            for key, value in item.items():
                temp = get_legal_document(value)
                data_list.append(temp)  # 获取每个公司名称对应的数据字典
    else:
        data_list=cases
    num_elements = len(data_list)
    print(num_elements)
    return f"""有相关信息{str(data_list)}，通过计算,已经确定我们想知道的案件数量是{num_elements},"""

# getNumOfCaseByKeyValue("案号","(2020)苏0412民初6970号")
# getComanyListInfoByKeyValueList([("公司名称", "瑞丰光电")],['法定代表人','注册地址','电子邮箱'])
# # searchInto()
# # getNumOfCompanyByKeyValue('所属行业','专用设备制造业')
# a=getComanyInfoByKeyValue('公司名称','瑞丰光电',['法定代表人','注册地址','电子邮箱'])
# print(a)
# getCompanyNameByKeyValue('公司名称','劲拓股份')
# a=getCompanyInfoByCompanyNameList(["药店龙头公司","益丰药房"],['注册资本'])

# a=search_company_name_by_info('英文名称','Beijing Comens New Materials Co., Ltd.')
""""公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期",
    "法人代表", "总经理","董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱",
    "入选指数", "主营业务", "经营范围","机构简介", "每股面值", "首发价格", "首发募资净额", "首发主承销商" """


"""["公司名称", "登记状态", "统一社会信用代码", "注册资本", "成立日期",
 "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名"]"""

"""关联上市公司股票代码", "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额", "公司名称"""

"标题,案号,文书类型,原告,被告,原告律师,被告律师,案由,审理法条依据,涉案金额,判决结果,胜诉方,文件名"


    # a=get_company_info("劲拓股份")
    # print(a)
    # search_company_name_by_info("公司名称","广州发展集团股份有限公司")
# a=get_company_info("香料江苏怡达化学股份有限公司")
    # a=search_company_name_by_register("注册号","320512400000458")
    #get_sub_company_info("正海磁材")
# a=getCompanyInfoByCompanyName("香料江苏怡达化学股份有限公司")
# print(a)
    # get_legal_document("(2020)桂0103民初6133号")
    # search_case_num_by_legal_document("标题","徐某某、李某某等合同纠纷民事一审民事判决书")
    # a=getcompanyinfo("所属行业", "批发业")
    # a=getcompanyinfo("公司名称", "浙江时立态合科技有限公司")
    # getlegaldocument("标题","徐某某、李某某等合同纠纷民事一审民事判决书")

    # a=getSpecialinfo("企业类型","股份有限公司（上市、国有控股）","注册资本")
    # a=getcompanysubinfo("公司名称","劲拓股份")
    # print(a)

    #
    #





