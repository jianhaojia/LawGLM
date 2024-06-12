from zhipuai import ZhipuAI
import json
from baseUrl.offical_base  import search_company_name_by_info,get_company_info,search_company_name_by_register,get_company_register,search_company_name_by_sub_info,get_sub_company_info,search_case_num_by_legal_document,get_legal_document


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_company_info",
            "description": "根据公司名称获得该公司所有基本信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "description": "公司名称",
                        "type": "string"
                    }
                },
                "required": [ "company_name" ]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_info",
            "description": "根据公司基本信息某个字段是某个值来查询具体的公司名称",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "公司基本信息的某个属性",
                        "type": "string"
                    },
                    "value": {
                        "description": "公司基本信息的某个属性的值",
                        "type": "string"
                    }
                },
                "required": [ "key","value" ]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_company_register",
            "description": "根据公司名称获得该公司所有注册信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "description": "公司名称",
                        "type": "string"
                    }
                },
                "required": [ "company_name" ]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_register",
            "description": "根据公司注册信息某个字段是某个值来查询具体的公司名称",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "公司注册信息的某个属性",
                        "type": "string"
                    },
                    "value": {
                        "description": "公司注册信息的某个属性的值",
                        "type": "string"
                    }
                },
                "required": [ "key","value" ]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_sub_company_info",
            "description": "根据公司名称获得该公司所有关联子公司信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "description": "公司名称",
                        "type": "string"
                    }
                },
                "required": ["company_name"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_sub_info",
            "description": "根据关联子公司信息某个字段是某个值来查询具体的公司名称",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "关联子公司信息某个字段",
                        "type": "string"
                    },
                    "value": {
                        "description": "关联子公司信息某个字段的值",
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
            "name": "get_legal_document",
            "description": "根据案号获得该案所有基本信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "case_num": {
                        "description": "案号",
                        "type": "string"
                    }
                },
                "required": ["case_num"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_sub_info",
            "description": "根据法律文书某个字段是某个值来查询具体的案号",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "法律文书信息的某个字段",
                        "type": "string"
                    },
                    "value": {
                        "description": "法律文书信息的某个字段的值",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            },
        }
    }
]


def parse_function_call(input):
    try:
        messages = []
        # messages.append({"role": "system", "content": prompt})
        messages.append({"role": "system", "content": "你是一个法律咨询机器人，需要通过理解意图，参考例子的格式中找到实体名称和实体值的格式，解析实体名称和实体的值，并从相关方法里面寻找答案，返回答案。"})
        messages.append({"role": "user", "content": input})

        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=messages,
            tools=tools,
        )
        if response.choices[0].message.tool_calls:
            tool_call = response.choices[0].message.tool_calls[0]
            args = tool_call.function.arguments
            function_result = {}
            if tool_call.function.name == "search_company_name_by_info":
                function_result = search_company_name_by_info(**json.loads(args))
            if tool_call.function.name == "get_company_info":
                function_result = get_company_info(**json.loads(args))
            if tool_call.function.name == "get_company_register":
                function_result = get_company_register(**json.loads(args))
            if tool_call.function.name == "search_company_name_by_register":
                function_result = search_company_name_by_register(**json.loads(args))
            if tool_call.function.name == "get_sub_company_info":
                function_result = get_sub_company_info(**json.loads(args))
            if tool_call.function.name == "search_company_name_by_sub_info":
                function_result = search_company_name_by_sub_info(**json.loads(args))
            if tool_call.function.name == "search_case_num_by_legal_document":
                function_result = search_case_num_by_legal_document(**json.loads(args))
            if tool_call.function.name == "get_legal_document":
                function_result = get_legal_document(**json.loads(args))
            messages.append({
                "role": "tool",
                "content": f"{json.dumps(function_result)}",
                "tool_call_id":tool_call.id
            })
            response = client.chat.completions.create(
                model="glm-4",
                messages=messages,
                tools=tools,
            )
            print(response.choices[0].message.content)
            return response.choices[0].message.content
    except Exception as e:
        return '不知道'

# parse_function_call('找下注册号为320512400000458是哪个公司')

#submit
id=0
def submit():
    with open('D:\\pythonctest\\law\\data\\question(1).json', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            question_data = json.loads(line)
            if question_data['id']>=id:

                with open('answers2.json', 'a', encoding='utf-8') as output_file:
                    print(question_data['id'])
                    answer = parse_function_call(question_data['question'])
                    question_data['answer'] = answer
                    json_str = json.dumps(question_data, ensure_ascii=False, separators=(',', ':'))
                    output_file.write(json_str + '\n')






