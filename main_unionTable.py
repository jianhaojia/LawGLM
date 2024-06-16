from zhipuai import ZhipuAI
import json
from baseUrl.offical_base import search_company_name_by_info, get_company_info, search_company_name_by_register, \
    get_company_register, search_company_name_by_sub_info, get_sub_company_info, search_case_num_by_legal_document, \
    get_legal_document, getcompanyinfo, getlegaldocument, getcompanyregisterinfo, getcompanysubinfo,getSpecialinfo,getCompanyInfoByCompanyName,getCompanyNameByKeyValue,getCompanyInfoByCompanyNameList,searchInto,getNumOfCompanyByKeyValue,getComanyInfoByKeyValue
from baseUrl.enhandtool import enhandceAndCall
from openai import OpenAI
import asyncio
client = ZhipuAI(api_key="") # 请填写您自己的APIKey
# client = ZhipuAI(api_key="") # 请填写您自己的APIKey

#属性名和只，
tools = [
 # {
 #        "type": "function",
 #        "function": {
 #            "name": "getCompanyInfoByCompanyNameList",
 #            "description": "根据公司名称列表和需要的信息列表，查询公司的需要的信息的值",
 #            "parameters": {
 #                "type": "object",
 #                "properties": {
 #                    "company_names": {
 #                    "description": "公司名称列表,不能为空，是列表",
 #                        "type": "array",
 #                        "company_name": {
 #                            "type": "string",
 #                            "enum": ["公司名称"]
 #                        }
 #                    },
 #                    "requirements": {
 #                        "description": "需要的信息列表，不能为空，是列表",
 #                        "type": "array",
 #                        "requirement": {
 #                            "type": "string",
 #                            "enum": ["公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期", "法人代表",
 #                                     "总经理", "董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱", "入选指数", "主营业务",
 #                                     "经营范围", "机构简介", "每股面值", "首发价格", "首发募资净额", '首发主承销商', "登记状态", "统一社会信用代码", "注册资本",
 #                                     "成立日期", "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名", "关联上市公司股票代码",
 #                                     "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额"]
 #                        }
 #                    }
 #                },
 #                "required": ["company_names","requirements"]
 #            },
 #        }
 #    },
    {
        "type": "function",
        "function": {
            "name": "getComanyInfoByKeyValue",
            "description": "根据属性名和他的值，以及需求字段查询相关的公司信息，类似select requirements from table where kay=value",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "属性名，不能为空。如果属性名的值是四个字，如'天味食品'，属性名不能为公司名称，只能是关联上市公司股票简称",
                        "type": "string",
                        "enum": ["公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期", "法人代表", "总经理","董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱", "入选指数", "主营业务", "经营范围","机构简介", "每股面值", "首发价格", "首发募资净额", '首发主承销商', "登记状态", "统一社会信用代码", "注册资本", "成立日期", "省份", "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名","关联上市公司股票代码", "关联上市公司股票简称", "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额"]
                    },
                    "value": {
                        "description": "属性名的值，不能为空",
                        "type": "string"
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
                "required": ["key", "value","requirements"]
            },
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
                        "description": "属性名的名",
                        "type": "string",
                        "enum": ["公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期", "法人代表", "总经理",
                                 "董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱", "入选指数", "主营业务", "经营范围",
                                 "机构简介", "每股面值", "首发价格", "首发募资净额", '首发主承销商', "登记状态", "统一社会信用代码", "注册资本", "成立日期", "省份",
                                 "城市", "区县", "注册号", "组织机构代码", "参保人数", "企业类型", "曾用名", "关联上市公司股票代码", "关联上市公司股票简称",
                                 "关联上市公司全称", "上市公司关系", "上市公司参股比例", "上市公司投资金额"]
                    },
                    "value": {
                        "description": "属性名的值",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "getlegaldocument",
            "description": "根据法律文书某个字段(key)是某个值(value)来查询法律文书信息，key的取值必须在下面其中一个：标题,案号,文书类型,原告,被告,原告律师,被告律师,案由,审理法条依据,涉案金额,判决结果,胜诉方,文件名",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "法律文书信息的某个字段",
                        "type": "string",
                        "enum": ["公司名称", "公司简称", "英文名称", "关联证券", "公司代码", "曾用简称", "所属市场", "所属行业", "上市日期", "法人代表", "总经理","董秘", "邮政编码", "注册地址", "办公地址", "联系电话", "传真", "官方网站", "电子邮箱", "入选指数", "主营业务", "经营范围","机构简介", "每股面值", "首发价格", "首发募资净额", '首发主承销商']

                    },
                    "value": {
                        "description": "法律文书信息的某个属性（key）的值，值必须是与key的值有逻辑关系",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            }
        }
    },
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

#完整问题
def enhanceQ(messages,memory=[]):
    messages2=[]
    messages2.append({"role": "system","content": "根据用户与系统的多伦对话，把这些，那些等待名称补充完整后，只返回完善后的问题"})
    messages2.append({"role": "user","content": "对话是:"+str(messages)+"完善下面问题:"+memory})
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages2

    )
    return response.choices[0].message.content

#不互相污染的pa_function1
def pa_function1(response):
    if response.choices[0].message.tool_calls:
        tool_call = response.choices[0].message.tool_calls[0]
        args = tool_call.function.arguments
        function_result = {}
        try:
            if tool_call.function.name == "getCompanyInfoByCompanyNameList":
                data=json.loads(args)
                function_result = getCompanyInfoByCompanyNameList(data["company_names"]["Items"],data["requirements"]["Items"])
            if tool_call.function.name == "getCompanyNameByKeyValue":
                function_result = getCompanyNameByKeyValue(**json.loads(args))
            if tool_call.function.name == "getlegaldocument":
                function_result = getlegaldocument(**json.loads(args))
            if tool_call.function.name == "getCompanyInfoByCompanyName":
                function_result = getCompanyInfoByCompanyName(**json.loads(args))
            if tool_call.function.name == "getNumOfCompanyByKeyValue":
                function_result = getNumOfCompanyByKeyValue(**json.loads(args))
        except:
            print("不是这个")

#单方法循环一次function call
def pa_function(response,messages,text=''):
    if response.choices[0].message.tool_calls:
        tool_call = response.choices[0].message.tool_calls[0]
        args = tool_call.function.arguments
        function_result = {}
        if tool_call.function.name == "getCompanyInfoByCompanyNameList":
            data=json.loads(args)
            function_result = getCompanyInfoByCompanyNameList(data["company_names"]["Items"],data["requirements"]["Items"])
        if tool_call.function.name == "getCompanyNameByKeyValue":
            function_result = getCompanyNameByKeyValue(**json.loads(args))
            # if function_result == [] or "查询错误" in str(function_result):
            #     print("名称匹配错误")
            #     data = json.loads(args)
            #     if function_result == [] and data["key"] == '公司名称':
            #         list = [ "关联上市公司股票简称", "关联上市公司全称","公司简称", "曾用简称", "曾用名"]
            #         for a in list:
            #             result = searchInto(a, data["value"])
            #             if result:
            #                 print("解析到:正确主键是："+str(a))
            #                 newtext = text.replace(data["value"], f"""{data["value"]}是一个{a},他""")
            #                 messages.append({"role": "system", "content": f"""找不到答案，请把问题问具体一点?"""})
            #                 messages.append({"role": "user", "content": f"""请理解我真实意图，一步一步来，{newtext}"""})
            #                 print(messages)
            #                 response2 = get_completion_with_tools(messages, tools)
            #                 print(response2)
            #                 pa_function(response2, messages, text)
        if tool_call.function.name == "getlegaldocument":
            function_result = getlegaldocument(**json.loads(args))
        if tool_call.function.name == "getCompanyInfoByCompanyName":
            function_result = getCompanyInfoByCompanyName(**json.loads(args))
            # if function_result == {} or "查询错误" in str(function_result):
            #     print("名称匹配错误")
            #     data = json.loads(args)
            #     key = next(iter(data))
            #     value = data[key]
            #     print(data)
            #     if function_result == {} and (key == 'company_name' or key == 'company_names'):
            #         list = [ "关联上市公司股票简称", "关联上市公司全称","公司简称", "曾用简称", "曾用名"]
            #         for a in list:
            #             result = searchInto(a, value)
            #             if result:
            #                 print("解析到:正确主键是："+str(a))
            #                 newtext=text.replace(value,f"""{value}是一个{a},他""")
            #                 messages.append({"role": "system", "content": f"""找不到答案，请把问题问具体一点?"""})
            #                 messages.append({"role": "user", "content": f"""请理解我真实意图，一步一步来，{newtext}"""})
            #                 print(messages)
            #                 response2 = get_completion_with_tools(messages, tools)
            #                 print(response2)
            #                 pa_function(response2, messages, text)

        if tool_call.function.name == "getNumOfCompanyByKeyValue":
            function_result = getNumOfCompanyByKeyValue(**json.loads(args))
        if tool_call.function.name != "getNumOfCompanyByKeyValue":
            messages.append({
                "role": "tool",
                "content": f"{json.dumps(function_result, ensure_ascii=False)}",
                "tool_call_id": tool_call.id
            })
            response = get_completion_with_tools(messages,tools)
            print(response)
            print(str(messages))
            return response,messages,text
        else:
            return '',function_result,text

#单循环的主方法
def main_cy_fu(text):
    messages=[]
    messages.append({"role": "system", "content": "你是一个法律的知识库，公司基本信息、公司注册信息以及公司关联信息的属性含义，以及取值范围，你的任务是识别用户法律问题，一步一步分析意图，识别好关键词，遇到计算或排序类问题，得分解成先是什么，再计算,再组合成完整的问题，找出答案"})
    messages.append({"role": "user", "content": text})
    response=get_completion_with_tools(messages,tools)
    response2=response
    messages2=messages
    print(response)
    result=response
    while(response2.choices[0].message.tool_calls):
        re,ms=pa_function(response2,messages2)
        response2=re
        messages2=ms
        result=str(response2)
    print("最终结果："+str(result))
    return result
#分解问题的单方法
def test_call(text,memory=''):
    messages=[]
    function_result=''
    messages.append({"role": "system","content": "你是一个法律专家，不能推测，分析用户实际意图,提取关键词的时候要注意逻辑关系，关键词不能为空，比如批发业不可能是公司名称，公司名称不能是数字，只需要回答用户的问题，必要时对已有消息计算和统计。如果历史对话已经有信息，只需要整理一下再回答"})
    prompt=text
    if memory:
      prompt=f"""目前已知{memory}想知道{text}"""
    messages.append({"role": "user", "content": prompt})
    print(messages)
    response = get_completion_with_tools(messages, tools)
    result=response.choices[0].message.content
    print(response)
    if response.choices[0].message.tool_calls:
        tool_call = response.choices[0].message.tool_calls[0]
        args = tool_call.function.arguments
        function_result = {}
        if tool_call.function.name == "getlegaldocument":
            function_result = getlegaldocument(**json.loads(args))
        if tool_call.function.name == "getComanyInfoByKeyValue":
            data = json.loads(args)
            print(data)
            print(data['key'])
            print(data['value'])
            if "Items" in str(data):
                print(data["requirements"]['Items'])
                function_result = getComanyInfoByKeyValue(key=data['key'],value=data['value'],requirements=data["requirements"]['Items'])
            else :
                print(data["requirements"])
                function_result = getComanyInfoByKeyValue(key=data['key'], value=data['value'],requirements=data["requirements"])
        if tool_call.function.name == "getNumOfCompanyByKeyValue":
            function_result = getNumOfCompanyByKeyValue(**json.loads(args))
        if tool_call.function.name != "getNumOfCompanyByKeyValue":
            messages.append({
                    "role": "user",
                    "content": f"{json.dumps(function_result, ensure_ascii=False)}",
            })
            messages.append({
                    "role": "user",
                    "content": "简要回答",
            })
            print("子message:"+str(messages))
            response = client.chat.completions.create(
                model="glm-4",  # 填写需要调用的模型名称
                messages=messages,
                tool_choice={"type": "function", "function": {"name": "getNumOfCompanyByKeyValue"}},
            )
            print(response)
            result=response.choices[0].message.content
        else:
            result=function_result

    print("子问题的答案："+str(result))

    return str(result)
#分解问题的单方法——无限循环
def test_call2(text,memory=''):
    messages=[]
    messages.append({"role": "system","content": "你是一个法律专家，不能随意猜测，不能传公司名称进来查公司名称，分析理解用户实际意图，只需要回答用户的问题，必要时对已有消息计算和统计"})
    prompt=text
    if memory:
      prompt=f"""目前已知{memory}想知道{text}"""

    print("子问题是：" + prompt)
    messages.append({"role": "user", "content": prompt})
    response = get_completion_with_tools(messages, tools)
    result=response.choices[0].message.content
    print(response)
    response2=response
    messages2=messages
    i=0
    while(response2.choices[0].message.tool_calls):
        i=i+1
        re,ms,text=pa_function(response2,messages2,prompt)
        print("进去了多少次"+str(i))
        response2=re
        messages2=ms
        prompt=text
        result=response2
        if response2 =='':
            return messages2

    print("子问题的答案："+str(result.choices[0].message.content))
    return result.choices[0].message.content
# 分解问题的主方法2
def multi_call(txet):
    instruction = """
     你的任务是识别用户实际的问题(question)需求是什么?并把问题补充得具体完整，需要一步一步分析意图
     
     包含字段可以为Q1,Q2,Q3等等，取决于有多个个问题,只返回答案不需要解释。
     """
    input_text = txet

    examples = """
     请问批发业注册资本最高的前3家公司的名称以及他们的注册资本（单位为万元）？：{"Q1":"所属行业是批发业公司的注册资本是多少？","Q2":"这些公司的注册资本最高的前3家公司的注册资本（单位为万元）是什么？"}

     请帮我查询一下上能电气股份有限公司的成立日期，同时请提供该公司的办公地点及联系方式：{"Q1":"电气股份有限公司的成立日期是什么？","Q2":"电气股份有限公司的办公地点是什么","Q3":"电气股份有限公司的联系方式是什么"}

     如何防止财务造假？:{"Q1":"如何防止财务造假？"}
     
     
     """
    prompt = f"""
     {instruction}



     例如：
     {examples}
     用户输入：
     {input_text}
     """
    response = get_completion_content(prompt)
    questions = json.loads(str(response))
    temp_message = []
    temp_message.append({
        'role': 'user',
        "content": txet
    })
    memory = ''
    print(questions)
    for q_key, q_value in questions.items():
        print(q_key)
        en_q_value=q_value
        q_result = test_call(en_q_value, memory=memory)
        temp_result = "资料：" + str(q_result) + ","
        memory = memory + temp_result

    prompt = f"""目前已知{temp_result}想知道{txet}"""
    print("问题是：" + prompt)
    result = get_completion(prompt, "从用户提供的信息里面提取答案,简明扼要,不要回答用户没问的问题")
    print("答案是：" + str(result.choices[0].message.content))
    return result.choices[0].message.content

# multi_call("请查询景津装备股份有限公司所属的行业类别，并告知在该行业分类下共有多少家公司？")
def is_jsonable(x):
    try:
        json.dumps(x, ensure_ascii=False)
        print("这是一个有效的JSON对象")
    except (TypeError, OverflowError):
        print("这B是一个有效的JSON对象")


count = 0


id = 123
limit = 150


def submit():
    with open('D:\\pythonctest\\law\\data\\question(1).json', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            question_data = json.loads(line)
            if question_data['id'] >= id and question_data['id'] <= limit:
                with open('output/answers4.json', 'a', encoding='utf-8') as output_file:
                    print(question_data['id'])
                    try:
                        answer = multi_call(question_data['question'])
                    except:
                        answer="不知道"
                    question_data['answer'] = answer
                    json_str = json.dumps(question_data, ensure_ascii=False, separators=(',', ':'))
                    output_file.write(json_str + '\n')

submit()
