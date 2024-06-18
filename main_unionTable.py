from zhipuai import ZhipuAI
import json
from baseUrl.offical_base import getCaseListInfoByKeyValueList, getNumOfCaseByKeyValue, getNumOfCompanyBykeyValue,getComanyListInfoByKeyValueList
from baseUrl.enhandtool import enhandceAndCall
from openai import OpenAI
import asyncio

import logging

# 设置日志记录器
# 设置日志记录器
logging.basicConfig(filename='log1.log', level=logging.INFO,
                    format='%(message)s')

# 创建一个日志记录器对象
logger = logging.getLogger(__name__)

# 写入一些日志信息
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
#属性名和只，
tools = [
    { "type": "function",
    "function": {
    "name": "getComanyListInfoByKeyValueList",
    "description": "根据关键字值对列表获取需要的公司信息列表。不能用来做计算公司数量",
    "parameters": {
        "type": "object",
        "properties": {
            "keyValueList": {
                "description": """关键字值对列表,注意，格式是 ：[(key,value),(key2,value2)]。例如[("公司名称","北京华清瑞达科技有限公司"),("公司名称","博晖生物制药（内蒙古）有限公司"),("公司名称","浙江迪安健检医疗管理有限公司")]""",
                "type": "array",
                "items": {
                    "type": "array",
                    "items": (
                        {
                            "description": "关键字,不能为空",
                            "type": "string"
                        },
                        {
                            "description": "值,不能为空",
                            "type": "any"
                        }
                    )
                }
            },
            "requirements": {
                "description": "需要的信息列表，不能为空,格式:['属性1','属性2'....] 例如 ['公司简称','英文名称']",
                "type": "list",
                "requirement": {
                    "type": "string",

                    "enum": ["公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期", "法人代表",
                             "总经理", "董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱", "入选指数", "主营业务",
                             "经营范围", "机构简介", "每股面值", "首发价格", "首发募资净额", '首发主承销商', "登记状态", "统一社会信用代码", "注册资本",
                             "成立日期", "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名", "关联上市公司股票代码",
                             "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额"]
                }
            }
        },
        "required": ["keyValueList", "requirements"]
    }
}
},
    {
        "type": "function",
        "function": {
            "name": "getNumOfCompanyByKeyValue",
            "description": "根据属性名和属性名的值来查询相关公司的数量",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "属性名的名,不能为空",
                        "type": "string",
                        "enum": ["公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期", "法人代表", "总经理",
                                 "董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱", "入选指数", "主营业务", "经营范围",
                                 "机构简介", "每股面值", "首发价格", "首发募资净额", '首发主承销商', "登记状态", "统一社会信用代码", "注册资本", "成立日期", "省份",
                                 "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名", "关联上市公司股票代码", "关联上市公司股票简称",
                                 "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额"]
                    },
                    "value": {
                        "description": "属性名的值,不能为空",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            },
        }
    },
{ "type": "function",
    "function": {
    "name": "getCaseListInfoByKeyValueList",
    "description": "根据关键字值对列表获取需要的案件信息列表。不能用来做案件数量计算",
    "parameters": {
        "type": "object",
        "properties": {
            "keyValueList": {
                "description": """关键字值对列表,注意，格式是 ：[(key,value),(key2,value2)]。例如[("案号","(2020)苏0412民初6970号"),("案号","(2020)鄂0606民初2733号")]""",
                "type": "array",
                "items": {
                    "type": "array",
                    "items": (
                        {
                            "description": "关键字,不能为空",
                            "type": "string"
                        },
                        {
                            "description": "值,不能为空",
                            "type": "any"
                        }
                    )
                }
            },
            "requirements": {
                "description": "需要的信息列表，不能为空,格式:['属性1','属性2'....] 例如 ['标题','案号']",
                "type": "list",
                "requirement": {
                    "type": "string",
                    "enum": ["标题", "案号", "文书类型", "原告", "被告", "原告律师", "被告律师", "案由", "审理法条依据", "涉案金额", "判决结果", "胜诉方","文件名"]

                }
            }
        },
        "required": ["keyValueList", "requirements"]
    }
}
},
    {
        "type": "function",
        "function": {
            "name": "getNumOfCaseByKeyValue",
            "description": "根据关键字值进行筛选，并统计出需要的统计案件数量或合作次数",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "属性名的名,不能为空",
                        "type": "string",
                        "enum": ["标题", "案号", "文书类型", "原告", "被告", "原告律师", "被告律师", "案由", "审理法条依据", "涉案金额", "判决结果", "胜诉方",
                                 "文件名"]
                    },
                    "value": {
                        "description": "属性名的值,不能为空",
                        "type": "string"
                    }
                },
                "required": ["key","value"]
            },
        }
    }

]
def get_completion_with_tools(messages, tools_inside):
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools_inside
    )
    return response



def get_completion_with_tools_content(messages, tools_inside):
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools_inside,
    )
    return response.choices[0].message.content

def get_completion_array(messages,function=''):
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages

    )
    return response

def get_completion_content(prompt):
    messages = [{"role": "user", "content": prompt}]  # 将 prompt 作为用户输入
    response = client.chat.completions.create(
        model="glm-4",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def get_completion(input,role='请回答用户问题'):
    messages = []
    messages.append({"role": "system", "content": role})
    messages.append({"role": "user", "content": input}) # 将 prompt 作为用户输入
    response = client.chat.completions.create(
        model="glm-4",
        messages=messages,
        temperature=0
    )
    return response

def print_json(data):
    """
    打印参数。如果参数是有结构的（如字典或列表），则以格式化的 JSON 形式打印；
    否则，直接打印该值。
    """
    if hasattr(data, 'model_dump_json'):
        data = json.loads(data.model_dump_json())

    if (isinstance(data, (list))):
        for item in data:
            print_json(item)
    elif (isinstance(data, (dict))):
        print(json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ))
    else:
        print(data)


def parseKeyValueList(key_value_list):
    """
    解析并统一不同格式的 keyValueList。

    参数:
    key_value_list (dict or list): 原始的键值对列表，可能有不同的嵌套格式。

    返回:
    list: 标准化后的键值对列表。
    """
    if isinstance(key_value_list, dict):
        # 处理可能的字典格式
        if "Items" in key_value_list:
            items = key_value_list["Items"]
            if isinstance(items, list):
                if all(isinstance(item, dict) and "Items" in item for item in items):
                    # 处理 {"Items": [{"Items": [...]}, ...]}
                    return [item["Items"] for item in items]
                elif all(isinstance(item, list) for item in items):
                    # 处理 {"Items": [[...], ...]}
                    return items
        elif isinstance(key_value_list, list):
            # 处理 {"keyValueList": [...]}
            return key_value_list
    elif isinstance(key_value_list, list):
        # 处理简单的列表格式
        return key_value_list

    # 如果格式无法识别，则返回空列表
    return []


def parseRequirements(requirements):
    """
    解析并统一不同格式的 requirements。

    参数:
    requirements (dict or list): 原始的需求列表，可能有不同的嵌套格式。

    返回:
    list: 标准化后的需求列表。
    """
    if isinstance(requirements, dict):
        # 处理可能的字典格式
        if "Items" in requirements:
            items = requirements["Items"]
            if isinstance(items, list):
                return items
    elif isinstance(requirements, list):
        # 处理简单的列表格式
        return requirements

    # 如果格式无法识别，则返回空列表
    return []



#单方法循环一次function call
def pa_function(response,messages,text=''):
    if response.choices[0].message.tool_calls:
        tool_call = response.choices[0].message.tool_calls[0]
        args = tool_call.function.arguments
        if tool_call.function.name == "getComanyListInfoByKeyValueList":
            data=json.loads(args)
            function_result=getComanyListInfoByKeyValueList(parseKeyValueList(data['keyValueList']),parseRequirements(data['requirements']))
        if tool_call.function.name == "getNumOfCompanyByKeyValue":
            function_result = getNumOfCompanyBykeyValue(**json.loads(args))
        if tool_call.function.name == "getCaseListInfoByKeyValueList":
            data=json.loads(args)
            function_result=getCaseListInfoByKeyValueList(parseKeyValueList(data['keyValueList']),parseRequirements(data['requirements']))
        if tool_call.function.name == "getNumOfCaseByKeyValue":
            function_result = getNumOfCaseByKeyValue(**json.loads(args))
        messages.append({
                "role": "user",
                "content": f"补充一下，我知道的是{function_result}"

            })
        response2 = client.chat.completions.create(
                temperature=0,
                model="glm-4",  # 填写需要调用的模型名称
                messages=messages,
                tools=tools
            )
        print("循环的答案")
        logger.info("循环的答案")
        print(response2.choices[0].message.content)
        logger.info(response2.choices[0].message.content)
        print(str(messages))
        logger.info(str(messages))
        return response2, messages, text


#单循环的主方法
def main_cy_fu(text):
    messages=[]
    messages.append({"role": "system", "content": "你是一个法律专家，不能推测，分析用户实际意图,提取关键词的时候要注意逻辑关系，关键词不能为空，比如批发业不可能是公司名称，公司名称不能是数字。只需要回答用户的问题，必要时对已有消息计算。如果历史对话已经有信息，只需要整理一下再回答,一行内答完"})
    messages.append({"role": "user", "content": text})
    response = client.chat.completions.create(
        temperature=0,
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools
    )
    response2=response
    messages2=messages
    logger.info(text)
    logger.info(str(response))
    print(response)
    result=response.choices[0].message.content
    text2=text
    max=5
    count=0
    while(response2.choices[0].message.tool_calls):
        re,ms,te=pa_function(response2,messages2,text2)
        count=count+1
        response2=re
        messages2=ms
        text2=te
        print(str(response2))
        result=str(response2.choices[0].message.content)
        if count==max:
            return result

    print("最终结果："+str(result))
    return result
#
# main_cy_fu("350781100073458注册的企业名称。")


id2 =93
limit2 = 150


def submit():
    with open('D:\\pythonctest\\law\\data\\question(1).json', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            question_data = json.loads(line)
            if question_data['id'] >= id2 and question_data['id'] <= limit2:
                with open('output/answers6.json', 'a', encoding='utf-8') as output_file:
                    print(question_data['id'])
                    try:
                        answer = main_cy_fu(question_data['question'])
                    except:
                        answer = "不知道"
                    print("传入结果")
                    print(str(answer))
                    question_data['answer'] = str(answer).replace('根据您提供的信息,','')
                    json_str = json.dumps(question_data, ensure_ascii=False, separators=(',', ':'))
                    output_file.write(json_str + '\n')


submit()

